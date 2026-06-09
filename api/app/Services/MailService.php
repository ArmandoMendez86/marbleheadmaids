<?php

declare(strict_types=1);

namespace App\Services;

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception as MailException;

class MailService
{
    private string $lastError = '';

    public function getLastError(): string
    {
        return $this->lastError;
    }

    private function mailer(): PHPMailer
    {
        $mail = new PHPMailer(true);
        $mail->isSMTP();
        $mail->SMTPDebug  = SMTP::DEBUG_OFF;
        $mail->Host       = $_ENV['SMTP_HOST'];
        $mail->SMTPAuth   = true;
        $mail->Username   = $_ENV['SMTP_USER'];
        $mail->Password   = $_ENV['SMTP_PASS'];

        $enc = strtolower($_ENV['SMTP_ENCRYPTION'] ?? 'ssl');
        if ($enc === 'tls') {
            $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        } elseif ($enc === 'ssl') {
            $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;
        } else {
            // Sin cifrado (solo para desarrollo local con Mailpit, etc.)
            $mail->SMTPSecure = '';
            $mail->SMTPAutoTLS = false;
        }

        $mail->Port    = (int)($_ENV['SMTP_PORT'] ?? 465);
        $mail->CharSet = 'UTF-8';
        $mail->Timeout = 10;
        $mail->setFrom($_ENV['SMTP_USER'], $_ENV['SMTP_FROM_NAME'] ?? 'Marblehead Maids');
        return $mail;
    }

    public function sendNewQuoteNotification(array $quote, string $toEmail): bool
    {
        try {
            $mail = $this->mailer();
            $mail->addAddress($toEmail);
            $mail->Subject = 'Nueva solicitud de cotización — ' . $quote['first_name'] . ' ' . $quote['last_name'];
            $mail->isHTML(true);
            $mail->Body    = $this->buildAdminEmailHtml($quote);
            $mail->AltBody = $this->buildAdminEmailText($quote);
            $mail->send();
            return true;
        } catch (MailException $e) {
            $this->lastError = $e->getMessage();
            error_log('MailService error: ' . $e->getMessage());
            return false;
        }
    }

    public function sendConfirmationToCustomer(array $quote): bool
    {
        try {
            $mail = $this->mailer();
            $mail->addAddress($quote['email'], $quote['first_name'] . ' ' . $quote['last_name']);
            $mail->Subject = 'We received your quote request — Marblehead Maids';
            $mail->isHTML(true);
            $mail->Body    = $this->buildCustomerEmailHtml($quote);
            $mail->AltBody = $this->buildCustomerEmailText($quote);
            $mail->send();
            return true;
        } catch (MailException $e) {
            $this->lastError = $e->getMessage();
            error_log('MailService customer email error: ' . $e->getMessage());
            return false;
        }
    }

    private function buildAdminEmailHtml(array $q): string
    {
        $consent = $q['marketing_consent'] ? 'Yes' : 'No';
        $date    = $q['created_at'] ?? date('Y-m-d H:i:s');
        return "
        <div style='font-family:Manrope,sans-serif;max-width:600px;margin:0 auto;background:#fff;border:1px solid #e5e7eb;border-radius:8px;overflow:hidden'>
          <div style='background:#12284b;padding:24px 32px'>
            <h1 style='color:#ffc52f;margin:0;font-size:20px'>Marblehead Maids</h1>
            <p style='color:#fff;margin:4px 0 0;font-size:14px'>Nueva solicitud de cotización</p>
          </div>
          <div style='padding:32px'>
            <table style='width:100%;border-collapse:collapse;font-size:15px'>
              <tr><td style='padding:8px 0;color:#4a4a4a;font-weight:600;width:140px'>Nombre:</td><td style='padding:8px 0;color:#12284b'>{$q['first_name']} {$q['last_name']}</td></tr>
              <tr style='background:#f5f7fa'><td style='padding:8px 4px;color:#4a4a4a;font-weight:600'>Email:</td><td style='padding:8px 4px;color:#12284b'>{$q['email']}</td></tr>
              <tr><td style='padding:8px 0;color:#4a4a4a;font-weight:600'>Teléfono:</td><td style='padding:8px 0;color:#12284b'>{$q['phone']}</td></tr>
              <tr style='background:#f5f7fa'><td style='padding:8px 4px;color:#4a4a4a;font-weight:600'>Dirección:</td><td style='padding:8px 4px;color:#12284b'>{$q['address']}</td></tr>
              <tr><td style='padding:8px 0;color:#4a4a4a;font-weight:600'>Zip Code:</td><td style='padding:8px 0;color:#12284b'>{$q['zip_code']}</td></tr>
              <tr style='background:#f5f7fa'><td style='padding:8px 4px;color:#4a4a4a;font-weight:600'>Marketing:</td><td style='padding:8px 4px;color:#12284b'>{$consent}</td></tr>
              <tr><td style='padding:8px 0;color:#4a4a4a;font-weight:600'>Fecha:</td><td style='padding:8px 0;color:#12284b'>{$date}</td></tr>
            </table>
            <div style='margin-top:24px;padding-top:24px;border-top:1px solid #e5e7eb'>
              <a href='" . ($_ENV['APP_BASE_URL'] ?? '') . "/admin/' style='display:inline-block;background:#ffc52f;color:#12284b;font-weight:700;padding:12px 24px;border-radius:6px;text-decoration:none'>Ver en el panel admin</a>
            </div>
          </div>
        </div>";
    }

    private function buildAdminEmailText(array $q): string
    {
        $consent = $q['marketing_consent'] ? 'Yes' : 'No';
        return "Nueva solicitud de cotización\n\nNombre: {$q['first_name']} {$q['last_name']}\nEmail: {$q['email']}\nTeléfono: {$q['phone']}\nDirección: {$q['address']}\nZip Code: {$q['zip_code']}\nMarketing: {$consent}\nFecha: {$q['created_at']}";
    }

    private function buildCustomerEmailHtml(array $q): string
    {
        return "
        <div style='font-family:Manrope,sans-serif;max-width:600px;margin:0 auto;background:#fff;border:1px solid #e5e7eb;border-radius:8px;overflow:hidden'>
          <div style='background:#12284b;padding:24px 32px'>
            <h1 style='color:#ffc52f;margin:0;font-size:20px'>Marblehead Maids</h1>
          </div>
          <div style='padding:32px'>
            <h2 style='color:#12284b;margin:0 0 16px'>Hi {$q['first_name']}, we got your request!</h2>
            <p style='color:#4a4a4a;line-height:1.6'>Thank you for reaching out to Marblehead Maids. We've received your quote request and will contact you shortly to discuss your cleaning needs.</p>
            <p style='color:#4a4a4a;margin-top:16px;line-height:1.6'>In the meantime, if you have any questions, feel free to call us at <strong>(617) 686-6805</strong>.</p>
            <p style='color:#4a4a4a;margin-top:24px'>— The Marblehead Maids Team</p>
          </div>
        </div>";
    }

    private function buildCustomerEmailText(array $q): string
    {
        return "Hi {$q['first_name']},\n\nThank you for reaching out to Marblehead Maids. We've received your quote request and will contact you shortly.\n\nIf you have questions, call us at (617) 686-6805.\n\n— The Marblehead Maids Team";
    }
}
