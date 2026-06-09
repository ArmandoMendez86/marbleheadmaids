<?php
if (session_status() === PHP_SESSION_NONE) {
    session_name('mm_admin_session');
    session_start();
}
// Ya logueado → redirigir
if (!empty($_SESSION['admin_logged_in'])) {
    header('Location: index.php');
    exit;
}

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Cargar .env y validar manualmente (sin Composer en la página de login para mayor compatibilidad)
    $envPath = dirname(__DIR__) . '/.env';
    $envVars = [];
    if (file_exists($envPath)) {
        foreach (file($envPath, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) as $line) {
            if (str_starts_with(trim($line), '#') || !str_contains($line, '=')) continue;
            [$k, $v] = explode('=', $line, 2);
            $envVars[trim($k)] = trim($v);
        }
    }

    $validUser = $envVars['ADMIN_USERNAME'] ?? 'admin';
    $validPass = $envVars['ADMIN_PASSWORD'] ?? '';

    $username = trim($_POST['username'] ?? '');
    $password = $_POST['password'] ?? '';

    if ($username === $validUser && $password === $validPass) {
        $_SESSION['admin_logged_in'] = true;
        $_SESSION['admin_user']      = $username;
        header('Location: index.php');
        exit;
    } else {
        $error = 'Usuario o contraseña incorrectos.';
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin Login — Marblehead Maids</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Manrope', sans-serif;
      background: #12284b;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .login-card {
      background: #fff;
      border-radius: 12px;
      padding: 40px 36px;
      width: 100%;
      max-width: 380px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.25);
    }
    .login-brand { text-align: center; margin-bottom: 28px; }
    .login-brand__name { font-weight: 800; font-size: 22px; color: #12284b; }
    .login-brand__name span { color: #ffc52f; }
    .login-brand__sub { font-size: 13px; color: #4a4a4a; margin-top: 4px; }
    .form-group { margin-bottom: 16px; }
    .form-label { display: block; font-size: 13px; font-weight: 600; color: #12284b; margin-bottom: 5px; }
    .form-control {
      width: 100%;
      padding: 10px 13px;
      border: 1px solid #e5e7eb;
      border-radius: 7px;
      font-size: 14px;
      font-family: inherit;
      color: #12284b;
      transition: border-color 0.15s;
    }
    .form-control:focus { outline: none; border-color: #ffc52f; box-shadow: 0 0 0 3px rgba(255,197,47,0.18); }
    .btn-submit {
      width: 100%;
      padding: 11px;
      background: #ffc52f;
      color: #12284b;
      font-weight: 700;
      font-size: 15px;
      border: none;
      border-radius: 7px;
      cursor: pointer;
      transition: background 0.15s;
      margin-top: 4px;
    }
    .btn-submit:hover { background: #e6b12a; }
    .alert-error {
      background: #fee2e2;
      color: #7f1d1d;
      padding: 10px 14px;
      border-radius: 6px;
      font-size: 13px;
      margin-bottom: 16px;
    }
  </style>
</head>
<body>
  <div class="login-card">
    <div class="login-brand">
      <div class="login-brand__name">Marblehead <span>Maids</span></div>
      <div class="login-brand__sub">Panel Administrativo</div>
    </div>

    <?php if ($error): ?>
      <div class="alert-error"><?= htmlspecialchars($error) ?></div>
    <?php endif; ?>

    <form method="POST" action="login.php">
      <div class="form-group">
        <label class="form-label" for="username">Usuario</label>
        <input
          type="text"
          id="username"
          name="username"
          class="form-control"
          autocomplete="username"
          required
          value="<?= htmlspecialchars($_POST['username'] ?? '') ?>"
        >
      </div>
      <div class="form-group">
        <label class="form-label" for="password">Contraseña</label>
        <input
          type="password"
          id="password"
          name="password"
          class="form-control"
          autocomplete="current-password"
          required
        >
      </div>
      <button type="submit" class="btn-submit">Iniciar sesión</button>
    </form>
  </div>
</body>
</html>
