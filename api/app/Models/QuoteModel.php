<?php

declare(strict_types=1);

namespace App\Models;

class QuoteModel
{
    public const STATUSES = ['pending', 'contacted', 'quoted', 'booked', 'closed', 'cancelled'];

    public function create(array $data): array
    {
        $db = getDB();
        $sql = "
            INSERT INTO quotes
                (first_name, last_name, email, phone, address, zip_code, marketing_consent)
            VALUES
                (:first_name, :last_name, :email, :phone, :address, :zip_code, :marketing_consent)
        ";
        $stmt = $db->prepare($sql);
        $stmt->execute([
            ':first_name'          => $data['first_name'],
            ':last_name'           => $data['last_name'] ?? '',
            ':email'               => $data['email'],
            ':phone'               => $data['phone'],
            ':address'             => $data['address'] ?? '',
            ':zip_code'            => $data['zip_code'],
            ':marketing_consent'   => $data['marketing_consent'] ? 1 : 0,
        ]);
        return $this->find((int)$db->lastInsertId());
    }

    public function find(int $id): ?array
    {
        $stmt = getDB()->prepare('SELECT * FROM quotes WHERE id = ?');
        $stmt->execute([$id]);
        $row = $stmt->fetch();
        return $row ?: null;
    }

    public function all(array $filters = []): array
    {
        $where  = [];
        $params = [];

        if (!empty($filters['status'])) {
            $where[]  = 'status = :status';
            $params[':status'] = $filters['status'];
        }

        if (!empty($filters['search'])) {
            $like = '%' . $filters['search'] . '%';
            $where[]  = '(first_name LIKE :s OR last_name LIKE :s OR email LIKE :s OR phone LIKE :s OR zip_code LIKE :s)';
            $params[':s'] = $like;
        }

        $sql  = 'SELECT * FROM quotes';
        if ($where) {
            $sql .= ' WHERE ' . implode(' AND ', $where);
        }
        $sql .= ' ORDER BY created_at DESC';

        // Paginación
        $page    = max(1, (int)($filters['page'] ?? 1));
        $perPage = 20;
        $offset  = ($page - 1) * $perPage;

        $countSql = str_replace('SELECT *', 'SELECT COUNT(*) as total', $sql);
        $countStmt = getDB()->prepare($countSql);
        $countStmt->execute($params);
        $total = (int)$countStmt->fetchColumn();

        $sql .= " LIMIT {$perPage} OFFSET {$offset}";
        $stmt = getDB()->prepare($sql);
        $stmt->execute($params);

        return [
            'data'       => $stmt->fetchAll(),
            'total'      => $total,
            'page'       => $page,
            'per_page'   => $perPage,
            'last_page'  => (int)ceil($total / $perPage),
        ];
    }

    public function update(int $id, array $data): ?array
    {
        $allowed = ['first_name', 'last_name', 'email', 'phone', 'address', 'zip_code', 'status', 'notes', 'marketing_consent'];
        $sets    = [];
        $params  = [];

        foreach ($allowed as $field) {
            if (array_key_exists($field, $data)) {
                $sets[]          = "{$field} = :{$field}";
                $params[":{$field}"] = $data[$field];
            }
        }

        if (empty($sets)) {
            return $this->find($id);
        }

        $sets[]      = "updated_at = datetime('now')";
        $params[':id'] = $id;

        $sql  = 'UPDATE quotes SET ' . implode(', ', $sets) . ' WHERE id = :id';
        $stmt = getDB()->prepare($sql);
        $stmt->execute($params);

        return $this->find($id);
    }

    public function delete(int $id): bool
    {
        $stmt = getDB()->prepare('DELETE FROM quotes WHERE id = ?');
        $stmt->execute([$id]);
        return $stmt->rowCount() > 0;
    }

    public function countByStatus(): array
    {
        $stmt = getDB()->query(
            "SELECT status, COUNT(*) as total FROM quotes GROUP BY status"
        );
        $rows   = $stmt->fetchAll();
        $result = array_fill_keys(self::STATUSES, 0);
        foreach ($rows as $row) {
            $result[$row['status']] = (int)$row['total'];
        }
        $result['all'] = array_sum($result);
        return $result;
    }
}
