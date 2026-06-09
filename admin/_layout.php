<?php
// Uso: include '_layout.php'; al inicio de cada página del admin
// Variables esperadas: $pageTitle (string)
$pageTitle = $pageTitle ?? 'Admin';
$adminUser = $_SESSION['admin_user'] ?? 'Admin';
$currentPage = basename($_SERVER['PHP_SELF']);

// ── Helpers de timezone ───────────────────────────────────────
if (!function_exists('getAdminTimezone')) {
    function getAdminTimezone(): string
    {
        static $tz = null;
        if ($tz !== null) return $tz;
        try {
            $stmt = getDB()->prepare("SELECT value FROM settings WHERE key = 'timezone'");
            $stmt->execute();
            $row = $stmt->fetch();
            $tz  = ($row && $row['value']) ? $row['value'] : 'UTC';
        } catch (\Exception $e) {
            $tz = 'UTC';
        }
        return $tz;
    }

    function formatDate(string $utcDate, string $format = 'M j, Y g:i a'): string
    {
        try {
            $dt = new \DateTime($utcDate, new \DateTimeZone('UTC'));
            $dt->setTimezone(new \DateTimeZone(getAdminTimezone()));
            return $dt->format($format);
        } catch (\Exception $e) {
            return $utcDate;
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><?= htmlspecialchars($pageTitle) ?> — Marblehead Maids Admin</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script>
    // Base URL del sitio leída desde .env — solo cambia APP_BASE_URL en .env al desplegar
    const SITE_BASE = '<?= rtrim($_ENV['APP_BASE_URL'] ?? '', '/') ?>';
  </script>
  <style>
    :root {
      --primary: #ffc52f;
      --dark: #12284b;
      --slate: #4a4a4a;
      --gray-50: #f9fafb;
      --gray-100: #f3f4f6;
      --gray-200: #e5e7eb;
      --gray-400: #9ca3af;
      --gray-600: #4b5563;
      --green: #16a34a;
      --green-bg: #dcfce7;
      --blue: #2563eb;
      --blue-bg: #dbeafe;
      --yellow-bg: #fef9c3;
      --red: #dc2626;
      --red-bg: #fee2e2;
      --orange: #ea580c;
      --orange-bg: #ffedd5;
      --purple: #7c3aed;
      --purple-bg: #ede9fe;
      --white: #fff;
      --sidebar-w: 220px;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Manrope', sans-serif; background: var(--gray-50); color: var(--slate); min-height: 100vh; display: flex; }
    a { text-decoration: none; color: inherit; }
    button { font-family: inherit; cursor: pointer; border: none; background: none; }

    /* Sidebar */
    .sidebar {
      width: var(--sidebar-w);
      background: var(--dark);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      position: fixed;
      top: 0; left: 0; bottom: 0;
      z-index: 10;
    }
    .sidebar__brand {
      padding: 20px 20px 16px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }
    .sidebar__brand-name { color: var(--primary); font-weight: 800; font-size: 15px; line-height: 1.2; }
    .sidebar__brand-sub  { color: rgba(255,255,255,0.5); font-size: 11px; margin-top: 2px; }
    .sidebar__nav { padding: 12px 0; flex: 1; }
    .sidebar__link {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 20px;
      color: rgba(255,255,255,0.65);
      font-size: 14px;
      font-weight: 500;
      transition: color 0.15s, background 0.15s;
    }
    .sidebar__link:hover, .sidebar__link.active {
      color: #fff;
      background: rgba(255,255,255,0.07);
    }
    .sidebar__link.active { border-left: 3px solid var(--primary); }
    .sidebar__link svg { width: 17px; height: 17px; flex-shrink: 0; opacity: 0.7; }
    .sidebar__link.active svg, .sidebar__link:hover svg { opacity: 1; }
    .sidebar__footer {
      padding: 12px 20px 20px;
      border-top: 1px solid rgba(255,255,255,0.08);
    }
    .sidebar__user { color: rgba(255,255,255,0.5); font-size: 12px; margin-bottom: 10px; }
    .sidebar__user strong { color: rgba(255,255,255,0.85); display: block; font-size: 13px; }
    .btn-logout {
      display: flex; align-items: center; gap: 8px;
      color: rgba(255,255,255,0.55);
      font-size: 13px; font-weight: 500;
      padding: 8px 0;
      transition: color 0.15s;
    }
    .btn-logout:hover { color: #fff; }
    .btn-logout svg { width: 15px; height: 15px; }

    /* Main */
    .main { margin-left: var(--sidebar-w); flex: 1; display: flex; flex-direction: column; min-height: 100vh; }
    .topbar {
      background: var(--white);
      border-bottom: 1px solid var(--gray-200);
      padding: 0 28px;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky; top: 0; z-index: 5;
    }
    .topbar__title { font-weight: 700; color: var(--dark); font-size: 17px; }
    .page-content { padding: 28px; flex: 1; }

    /* Cards */
    .card {
      background: var(--white);
      border: 1px solid var(--gray-200);
      border-radius: 10px;
      overflow: hidden;
    }
    .card__header {
      padding: 16px 20px;
      border-bottom: 1px solid var(--gray-200);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }
    .card__title { font-weight: 700; color: var(--dark); font-size: 15px; }
    .card__body { padding: 20px; }

    /* Stats */
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 14px; margin-bottom: 24px; }
    .stat-card {
      background: var(--white);
      border: 1px solid var(--gray-200);
      border-radius: 10px;
      padding: 16px;
      text-align: center;
    }
    .stat-card__num { font-size: 26px; font-weight: 800; color: var(--dark); line-height: 1; }
    .stat-card__label { font-size: 12px; color: var(--gray-400); margin-top: 4px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; }

    /* Table */
    .table-wrap { overflow-x: auto; }
    table { width: 100%; border-collapse: collapse; font-size: 14px; }
    thead th {
      text-align: left;
      padding: 10px 14px;
      background: var(--gray-50);
      color: var(--gray-600);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid var(--gray-200);
      white-space: nowrap;
    }
    tbody tr { border-bottom: 1px solid var(--gray-100); transition: background 0.1s; }
    tbody tr:hover { background: var(--gray-50); }
    tbody td { padding: 12px 14px; vertical-align: middle; }
    tbody tr:last-child { border-bottom: none; }

    /* Badges */
    .badge {
      display: inline-flex;
      align-items: center;
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      text-transform: capitalize;
      white-space: nowrap;
    }
    .badge--pending    { background: var(--yellow-bg); color: #92400e; }
    .badge--contacted  { background: var(--blue-bg);   color: var(--blue); }
    .badge--quoted     { background: var(--purple-bg); color: var(--purple); }
    .badge--booked     { background: var(--green-bg);  color: var(--green); }
    .badge--closed     { background: var(--gray-100);  color: var(--gray-600); }
    .badge--cancelled  { background: var(--red-bg);    color: var(--red); }

    /* Buttons */
    .btn {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 14px;
      font-weight: 600;
      transition: background 0.15s, color 0.15s;
      white-space: nowrap;
    }
    .btn svg { width: 15px; height: 15px; }
    .btn--primary  { background: var(--primary); color: var(--dark); }
    .btn--primary:hover { background: #e6b12a; }
    .btn--dark     { background: var(--dark); color: var(--white); }
    .btn--dark:hover { background: #0a1a30; }
    .btn--danger   { background: var(--red); color: var(--white); }
    .btn--danger:hover { background: #b91c1c; }
    .btn--ghost    { background: transparent; color: var(--slate); border: 1px solid var(--gray-200); }
    .btn--ghost:hover { background: var(--gray-50); }
    .btn--sm { padding: 5px 10px; font-size: 13px; }
    .btn--icon { padding: 6px; border-radius: 6px; }

    /* Forms */
    .form-group { margin-bottom: 16px; }
    .form-label { display: block; font-size: 13px; font-weight: 600; color: var(--dark); margin-bottom: 5px; }
    .form-control {
      width: 100%;
      padding: 9px 12px;
      border: 1px solid var(--gray-200);
      border-radius: 6px;
      font-size: 14px;
      font-family: inherit;
      color: var(--dark);
      background: var(--white);
      transition: border-color 0.15s;
    }
    .form-control:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(255,197,47,0.15); }
    textarea.form-control { resize: vertical; min-height: 90px; }
    select.form-control { cursor: pointer; }

    /* Filters row */
    .filters { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; margin-bottom: 16px; }
    .filters__search { flex: 1; min-width: 180px; max-width: 320px; }
    .filters__select { min-width: 140px; width: auto; }

    /* Pagination */
    .pagination { display: flex; align-items: center; gap: 6px; justify-content: flex-end; padding: 14px 20px; border-top: 1px solid var(--gray-100); }
    .pagination__info { font-size: 13px; color: var(--gray-400); margin-right: 8px; }
    .page-btn {
      width: 34px; height: 34px;
      display: flex; align-items: center; justify-content: center;
      border-radius: 6px;
      font-size: 13px; font-weight: 600;
      border: 1px solid var(--gray-200);
      color: var(--slate);
      transition: background 0.1s;
    }
    .page-btn:hover:not(:disabled) { background: var(--gray-100); }
    .page-btn.active { background: var(--dark); color: var(--white); border-color: var(--dark); }
    .page-btn:disabled { opacity: 0.4; cursor: not-allowed; }

    /* Alerts */
    .alert { padding: 12px 16px; border-radius: 6px; font-size: 14px; margin-bottom: 16px; }
    .alert--success { background: var(--green-bg); color: #14532d; }
    .alert--error   { background: var(--red-bg);   color: #7f1d1d; }

    /* Empty state */
    .empty-state { text-align: center; padding: 48px 20px; color: var(--gray-400); }
    .empty-state svg { width: 40px; height: 40px; margin: 0 auto 12px; opacity: 0.4; display: block; }
    .empty-state p { font-size: 15px; }

    /* Action buttons in table */
    .row-actions { display: flex; gap: 6px; }

    /* Modal confirm */
    .modal-overlay {
      display: none;
      position: fixed; inset: 0;
      background: rgba(0,0,0,0.45);
      z-index: 100;
      align-items: center;
      justify-content: center;
    }
    .modal-overlay.open { display: flex; }
    .modal-box {
      background: var(--white);
      border-radius: 10px;
      padding: 28px;
      max-width: 400px;
      width: 90%;
      box-shadow: 0 20px 60px rgba(0,0,0,0.18);
    }
    .modal-box h3 { color: var(--dark); font-size: 17px; margin-bottom: 10px; }
    .modal-box p  { color: var(--slate); font-size: 14px; line-height: 1.6; margin-bottom: 20px; }
    .modal-actions { display: flex; gap: 10px; justify-content: flex-end; }

    @media (max-width: 768px) {
      .sidebar { transform: translateX(-100%); transition: transform 0.25s; }
      .sidebar.open { transform: translateX(0); }
      .main { margin-left: 0; }
      .topbar { padding: 0 16px; }
      .page-content { padding: 16px; }
    }
  </style>
</head>
<body>

<aside class="sidebar" id="sidebar">
  <div class="sidebar__brand">
    <div class="sidebar__brand-name">Marblehead Maids</div>
    <div class="sidebar__brand-sub">Admin Panel</div>
  </div>
  <nav class="sidebar__nav">
    <a href="index.php" class="sidebar__link <?= $currentPage === 'index.php' ? 'active' : '' ?>">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7h18M3 12h18M3 17h18"/></svg>
      Solicitudes
    </a>
    <a href="settings.php" class="sidebar__link <?= $currentPage === 'settings.php' ? 'active' : '' ?>">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
      Configuración
    </a>
    <a href="../index.html" class="sidebar__link" target="_blank">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
      Ver sitio
    </a>
  </nav>
  <div class="sidebar__footer">
    <div class="sidebar__user">Sesión activa<strong><?= htmlspecialchars($adminUser) ?></strong></div>
    <form method="POST" action="logout.php">
      <button type="submit" class="btn-logout">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/></svg>
        Cerrar sesión
      </button>
    </form>
  </div>
</aside>

<div class="main">
  <div class="topbar">
    <span class="topbar__title"><?= htmlspecialchars($pageTitle) ?></span>
  </div>
  <div class="page-content">
