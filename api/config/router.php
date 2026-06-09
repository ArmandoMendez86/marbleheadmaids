<?php

declare(strict_types=1);

use App\Controllers\QuoteController;
use App\Controllers\AdminController;

function respond(int $code, array $data): never
{
    http_response_code($code);
    echo json_encode($data, JSON_UNESCAPED_UNICODE);
    exit;
}

function getRequestBody(): array
{
    $raw = file_get_contents('php://input');
    return json_decode($raw ?: '{}', true) ?? [];
}

function dispatch(): void
{
    $method = $_SERVER['REQUEST_METHOD'];

    // PATH_INFO es lo más portable: funciona en XAMPP (con index.php en la URL)
    // y en Hostinger con mod_rewrite. Fallback para otras configuraciones.
    if (!empty($_SERVER['PATH_INFO'])) {
        $path = $_SERVER['PATH_INFO'];
    } else {
        $uri  = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
        $base = rtrim(dirname($_SERVER['SCRIPT_NAME']), '/');
        $path = '/' . ltrim(substr($uri, strlen($base)), '/');
        // Eliminar /index.php del inicio si quedó
        $path = preg_replace('#^/index\.php#', '', $path) ?: '/';
    }

    // Separar segmentos
    $parts = array_values(array_filter(explode('/', $path)));
    // Quitar el primer segmento si es 'api' (por si mod_rewrite lo deja)
    if (isset($parts[0]) && $parts[0] === 'api') {
        array_shift($parts);
    }

    // Rutas públicas
    // POST /quotes
    if ($method === 'POST' && ($parts[0] ?? '') === 'quotes' && count($parts) === 1) {
        $ctrl = new QuoteController();
        $ctrl->store(getRequestBody());
        return;
    }

    // Rutas de admin  (/admin/*)
    if (($parts[0] ?? '') === 'admin') {
        $sub = $parts[1] ?? '';
        $id  = isset($parts[2]) ? (int)$parts[2] : null;

        $ctrl = new AdminController();

        // POST /admin/login
        if ($method === 'POST' && $sub === 'login') {
            $ctrl->login(getRequestBody());
            return;
        }

        // POST /admin/logout
        if ($method === 'POST' && $sub === 'logout') {
            $ctrl->logout();
            return;
        }

        // GET /admin/me — verificar sesión
        if ($method === 'GET' && $sub === 'me') {
            $ctrl->me();
            return;
        }

        // Todo lo demás requiere autenticación
        $ctrl->requireAuth();

        // GET /admin/quotes
        if ($method === 'GET' && $sub === 'quotes' && $id === null) {
            $ctrl->indexQuotes();
            return;
        }

        // GET /admin/quotes/{id}
        if ($method === 'GET' && $sub === 'quotes' && $id !== null) {
            $ctrl->showQuote($id);
            return;
        }

        // PATCH /admin/quotes/{id}  — editar campos + status + notas
        if ($method === 'PATCH' && $sub === 'quotes' && $id !== null) {
            $ctrl->updateQuote($id, getRequestBody());
            return;
        }

        // DELETE /admin/quotes/{id}
        if ($method === 'DELETE' && $sub === 'quotes' && $id !== null) {
            $ctrl->deleteQuote($id);
            return;
        }

        // GET /admin/settings
        if ($method === 'GET' && $sub === 'settings') {
            $ctrl->getSettings();
            return;
        }

        // PUT /admin/settings
        if ($method === 'PUT' && $sub === 'settings') {
            $ctrl->saveSettings(getRequestBody());
            return;
        }

        // POST /admin/test-email
        if ($method === 'POST' && $sub === 'test-email') {
            $ctrl->sendTestEmail(getRequestBody());
            return;
        }

        // GET /admin/timezone-preview?tz=America/New_York
        if ($method === 'GET' && $sub === 'timezone-preview') {
            $ctrl->timezonePreview();
            return;
        }
    }

    respond(404, ['error' => 'Endpoint not found']);
}
