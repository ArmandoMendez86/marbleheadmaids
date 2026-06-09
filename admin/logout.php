<?php
if (session_status() === PHP_SESSION_NONE) {
    session_name('mm_admin_session');
    session_start();
}
$_SESSION = [];
session_destroy();
header('Location: login.php');
exit;
