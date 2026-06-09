<?php

declare(strict_types=1);

namespace App\Models;

class SettingModel
{
    public function get(string $key, string $default = ''): string
    {
        $stmt = getDB()->prepare('SELECT value FROM settings WHERE key = ?');
        $stmt->execute([$key]);
        $row = $stmt->fetch();
        return $row ? $row['value'] : $default;
    }

    public function set(string $key, string $value): void
    {
        $stmt = getDB()->prepare(
            'INSERT INTO settings (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value'
        );
        $stmt->execute([$key, $value]);
    }

    public function all(): array
    {
        $stmt = getDB()->query('SELECT key, value FROM settings');
        $result = [];
        foreach ($stmt->fetchAll() as $row) {
            $result[$row['key']] = $row['value'];
        }
        return $result;
    }
}
