<?php

declare(strict_types=1);

namespace App\Controllers;

use App\Models\QuoteModel;
use App\Models\SettingModel;
use App\Services\MailService;

class QuoteController
{
    public function store(array $body): void
    {
        // Validación
        $errors = $this->validate($body);
        if ($errors) {
            respond(422, ['errors' => $errors]);
        }

        $data = [
            'first_name'         => trim($body['first_name']),
            'last_name'          => trim($body['last_name'] ?? ''),
            'email'              => strtolower(trim($body['email'])),
            'phone'              => trim($body['phone']),
            'address'            => trim($body['address'] ?? ''),
            'zip_code'           => trim($body['zip_code']),
            'marketing_consent'  => !empty($body['marketing_consent']),
        ];

        $model = new QuoteModel();
        $quote = $model->create($data);

        // Enviar emails (no bloqueantes: si fallan, igual respondemos OK)
        $settings     = new SettingModel();
        $notifEmail   = $settings->get('notification_email', $_ENV['ADMIN_NOTIFICATION_EMAIL'] ?? '');
        $mail         = new MailService();

        if ($notifEmail) {
            $mail->sendNewQuoteNotification($quote, $notifEmail);
        }
        $mail->sendConfirmationToCustomer($quote);

        respond(201, [
            'success' => true,
            'message' => 'Your request has been received. We\'ll contact you shortly!',
        ]);
    }

    private function validate(array $body): array
    {
        $errors = [];

        if (empty(trim($body['first_name'] ?? ''))) {
            $errors['first_name'] = 'First name is required.';
        }

        $email = trim($body['email'] ?? '');
        if (empty($email)) {
            $errors['email'] = 'Email is required.';
        } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $errors['email'] = 'Please enter a valid email.';
        }

        if (empty(trim($body['phone'] ?? ''))) {
            $errors['phone'] = 'Phone is required.';
        }

        if (empty(trim($body['zip_code'] ?? ''))) {
            $errors['zip_code'] = 'Zip code is required.';
        }

        return $errors;
    }
}
