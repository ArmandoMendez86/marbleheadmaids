<?php

declare(strict_types=1);

define('ROOT_PATH', dirname(__DIR__, 2));
define('API_PATH', dirname(__DIR__));
define('STORAGE_PATH', ROOT_PATH . '/storage');

// Autoload Composer (PHPMailer, phpdotenv, PSR-4 de App\)
$autoload = ROOT_PATH . '/vendor/autoload.php';
if (!file_exists($autoload)) {
    http_response_code(500);
    header('Content-Type: application/json');
    echo json_encode(['error' => 'Vendor not found. Run composer install.']);
    exit;
}
require_once $autoload;

// Cargar .env
$dotenv = Dotenv\Dotenv::createImmutable(ROOT_PATH);
$dotenv->load();

// Headers CORS + JSON para la API
header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

$origin = $_ENV['APP_BASE_URL'] ?? '*';
header("Access-Control-Allow-Origin: {$origin}");
header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');
header('Access-Control-Allow-Credentials: true');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

// Iniciar sesión para autenticación del admin
if (session_status() === PHP_SESSION_NONE) {
    session_name('mm_admin_session');
    session_start();
}
