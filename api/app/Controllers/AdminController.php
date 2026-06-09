<?php

declare(strict_types=1);

namespace App\Controllers;

use App\Models\QuoteModel;
use App\Models\SettingModel;
use App\Services\MailService;

class AdminController
{
    // ── Autenticación ──────────────────────────────────────────

    public function login(array $body): void
    {
        $username = trim($body['username'] ?? '');
        $password = $body['password'] ?? '';

        $validUser = $_ENV['ADMIN_USERNAME'] ?? 'admin';
        $validPass = $_ENV['ADMIN_PASSWORD'] ?? '';

        if ($username === $validUser && $password === $validPass) {
            $_SESSION['admin_logged_in'] = true;
            $_SESSION['admin_user']      = $username;
            respond(200, ['success' => true, 'user' => $username]);
        }

        respond(401, ['error' => 'Invalid credentials.']);
    }

    public function logout(): void
    {
        $_SESSION = [];
        session_destroy();
        respond(200, ['success' => true]);
    }

    public function me(): void
    {
        if (!empty($_SESSION['admin_logged_in'])) {
            respond(200, ['authenticated' => true, 'user' => $_SESSION['admin_user']]);
        }
        respond(401, ['authenticated' => false]);
    }

    public function requireAuth(): void
    {
        if (empty($_SESSION['admin_logged_in'])) {
            respond(401, ['error' => 'Unauthorized. Please log in.']);
        }
    }

    // ── Quotes ─────────────────────────────────────────────────

    public function indexQuotes(): void
    {
        $model   = new QuoteModel();
        $filters = [
            'status' => $_GET['status'] ?? '',
            'search' => $_GET['search'] ?? '',
            'page'   => $_GET['page']   ?? 1,
        ];

        $result  = $model->all($filters);
        $counts  = $model->countByStatus();

        respond(200, array_merge($result, ['counts' => $counts]));
    }

    public function showQuote(int $id): void
    {
        $model = new QuoteModel();
        $quote = $model->find($id);

        if (!$quote) {
            respond(404, ['error' => 'Quote not found.']);
        }

        respond(200, $quote);
    }

    public function updateQuote(int $id, array $body): void
    {
        $model = new QuoteModel();
        $quote = $model->find($id);

        if (!$quote) {
            respond(404, ['error' => 'Quote not found.']);
        }

        // Validar status si viene en el body
        if (isset($body['status']) && !in_array($body['status'], QuoteModel::STATUSES, true)) {
            respond(422, ['error' => 'Invalid status.']);
        }

        $updated = $model->update($id, $body);
        respond(200, $updated);
    }

    public function deleteQuote(int $id): void
    {
        $model   = new QuoteModel();
        $deleted = $model->delete($id);

        if (!$deleted) {
            respond(404, ['error' => 'Quote not found.']);
        }

        respond(200, ['success' => true, 'message' => 'Quote deleted.']);
    }

    // ── Settings ───────────────────────────────────────────────

    public function getSettings(): void
    {
        $model    = new SettingModel();
        $settings = $model->all();
        respond(200, $settings);
    }

    public function saveSettings(array $body): void
    {
        $model = new SettingModel();

        $allowed = ['notification_email', 'timezone'];
        foreach ($allowed as $key) {
            if (array_key_exists($key, $body)) {
                $model->set($key, (string)$body[$key]);
            }
        }

        respond(200, ['success' => true, 'settings' => $model->all()]);
    }

    public function timezonePreview(): void
    {
        $tz = trim($_GET['tz'] ?? 'UTC');
        if (!in_array($tz, \DateTimeZone::listIdentifiers(), true)) {
            respond(422, ['error' => 'Invalid timezone.']);
        }
        try {
            $now     = new \DateTime('now', new \DateTimeZone('UTC'));
            $local   = clone $now;
            $local->setTimezone(new \DateTimeZone($tz));
            respond(200, ['preview' => $local->format('D, M j Y — g:i:s a (T)')]);
        } catch (\Exception $e) {
            respond(422, ['error' => 'Invalid timezone.']);
        }
    }

    public function sendTestEmail(array $body): void
    {
        $to = filter_var(trim($body['email'] ?? ''), FILTER_VALIDATE_EMAIL);
        if (!$to) {
            respond(422, ['error' => 'Invalid email address.']);
        }

        $fakeQuote = [
            'id'         => 0,
            'first_name' => 'Test',
            'last_name'  => 'User',
            'email'      => $to,
            'phone'      => '+1 000-000-0000',
            'address'    => '123 Test St',
            'zip_code'   => '00000',
            'marketing_consent' => 0,
            'created_at' => date('Y-m-d H:i:s'),
        ];

        $mail = new MailService();
        $sent = $mail->sendNewQuoteNotification($fakeQuote, $to);

        if ($sent) {
            respond(200, ['success' => true, 'message' => 'Test email sent to ' . $to]);
        } else {
            respond(500, ['error' => $mail->getLastError() ?: 'Failed to send email. Check SMTP config in .env.']);
        }
    }
}
