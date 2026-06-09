<?php
// Verificar sesión del admin — incluir al inicio de cada página protegida
if (session_status() === PHP_SESSION_NONE) {
    session_name('mm_admin_session');
    session_start();
}
if (empty($_SESSION['admin_logged_in'])) {
    header('Location: login.php');
    exit;
}
