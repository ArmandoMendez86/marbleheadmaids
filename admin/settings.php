<?php
require_once '_auth.php';

define('ROOT_PATH', dirname(__DIR__));
define('API_PATH', ROOT_PATH . '/api');
define('STORAGE_PATH', ROOT_PATH . '/storage');

$autoload = ROOT_PATH . '/vendor/autoload.php';
if (!file_exists($autoload)) { die('Run composer install'); }
require_once $autoload;

$dotenv = Dotenv\Dotenv::createImmutable(ROOT_PATH);
$dotenv->load();
require_once API_PATH . '/config/database.php';

use App\Models\SettingModel;

$model   = new SettingModel();
$success = '';
$error   = '';

// Lista curada de timezones comunes agrupadas por región
$timezoneGroups = [
    'UTC' => ['UTC'],
    'Estados Unidos / Canadá' => [
        'America/New_York',
        'America/Chicago',
        'America/Denver',
        'America/Phoenix',
        'America/Los_Angeles',
        'America/Anchorage',
        'Pacific/Honolulu',
        'America/Toronto',
        'America/Vancouver',
    ],
    'México / Centroamérica' => [
        'America/Mexico_City',
        'America/Cancun',
        'America/Monterrey',
        'America/Guatemala',
        'America/Costa_Rica',
    ],
    'Sudamérica' => [
        'America/Bogota',
        'America/Lima',
        'America/Caracas',
        'America/Santiago',
        'America/Sao_Paulo',
        'America/Argentina/Buenos_Aires',
    ],
    'Europa' => [
        'Europe/London',
        'Europe/Lisbon',
        'Europe/Madrid',
        'Europe/Paris',
        'Europe/Berlin',
        'Europe/Rome',
        'Europe/Amsterdam',
        'Europe/Warsaw',
        'Europe/Helsinki',
        'Europe/Moscow',
    ],
    'Asia / Pacífico' => [
        'Asia/Dubai',
        'Asia/Kolkata',
        'Asia/Bangkok',
        'Asia/Singapore',
        'Asia/Tokyo',
        'Asia/Shanghai',
        'Australia/Sydney',
        'Pacific/Auckland',
    ],
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['_action'] ?? 'general';

    if ($action === 'general') {
        $notifEmail = trim($_POST['notification_email'] ?? '');
        $timezone   = trim($_POST['timezone'] ?? 'UTC');

        // Validar email
        if ($notifEmail && !filter_var($notifEmail, FILTER_VALIDATE_EMAIL)) {
            $error = 'El email de notificación no es válido.';
        }
        // Validar timezone
        elseif (!in_array($timezone, \DateTimeZone::listIdentifiers(), true)) {
            $error = 'La zona horaria seleccionada no es válida.';
        }
        else {
            $model->set('notification_email', $notifEmail);
            $model->set('timezone', $timezone);
            $success = 'Configuración guardada correctamente.';
        }
    }
}

$settings     = $model->all();
$currentEmail = $settings['notification_email'] ?? ($_ENV['ADMIN_NOTIFICATION_EMAIL'] ?? '');
$currentTz    = $settings['timezone']            ?? 'UTC';

// Hora actual en la zona configurada (para previsualizar)
try {
    $nowUtc      = new \DateTime('now', new \DateTimeZone('UTC'));
    $nowLocal    = clone $nowUtc;
    $nowLocal->setTimezone(new \DateTimeZone($currentTz));
    $tzPreview   = $nowLocal->format('D, M j Y — g:i:s a (T)');
} catch (\Exception $e) {
    $tzPreview = '—';
}

$smtpInfo = [
    'Host'       => $_ENV['SMTP_HOST']       ?? '—',
    'Port'       => $_ENV['SMTP_PORT']       ?? '—',
    'Encryption' => strtoupper($_ENV['SMTP_ENCRYPTION'] ?? '—'),
    'User'       => $_ENV['SMTP_USER']       ?? '—',
    'From Name'  => $_ENV['SMTP_FROM_NAME']  ?? '—',
];

$pageTitle = 'Configuración';
include '_layout.php';
?>

<?php if ($success): ?>
  <div class="alert alert--success"><?= htmlspecialchars($success) ?></div>
<?php endif; ?>
<?php if ($error): ?>
  <div class="alert alert--error"><?= htmlspecialchars($error) ?></div>
<?php endif; ?>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start">

  <!-- Email + Timezone (mismo formulario) -->
  <div class="card">
    <div class="card__header">
      <span class="card__title">Notificaciones y zona horaria</span>
    </div>
    <div class="card__body">
      <form method="POST" action="settings.php">
        <input type="hidden" name="_action" value="general">

        <div class="form-group">
          <label class="form-label">Email receptor de notificaciones</label>
          <input
            type="email"
            name="notification_email"
            class="form-control"
            placeholder="admin@ejemplo.com"
            value="<?= htmlspecialchars($currentEmail) ?>"
          >
          <p style="font-size:12px;color:var(--gray-400);margin-top:5px">Dejar vacío para desactivar las notificaciones por email.</p>
        </div>

        <div class="form-group" style="margin-top:20px">
          <label class="form-label">Zona horaria</label>
          <select name="timezone" class="form-control" id="tzSelect" onchange="updateTzPreview()">
            <?php foreach ($timezoneGroups as $group => $zones): ?>
              <optgroup label="<?= htmlspecialchars($group) ?>">
                <?php foreach ($zones as $tz): ?>
                  <option value="<?= $tz ?>" <?= $currentTz === $tz ? 'selected' : '' ?>><?= $tz ?></option>
                <?php endforeach; ?>
              </optgroup>
            <?php endforeach; ?>
          </select>
          <p style="font-size:12px;color:var(--gray-400);margin-top:6px">
            Las fechas se guardan siempre en <strong>UTC</strong> y se convierten al mostrar.
          </p>
          <div id="tzPreviewBox" style="margin-top:8px;padding:8px 12px;background:var(--gray-50);border:1px solid var(--gray-200);border-radius:6px;font-size:13px;color:var(--dark)">
            <span style="color:var(--gray-400);font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.05em">Hora actual en la zona seleccionada</span><br>
            <span id="tzPreviewText"><?= htmlspecialchars($tzPreview) ?></span>
          </div>
        </div>

        <button type="submit" class="btn btn--primary" style="margin-top:4px">Guardar configuración</button>
      </form>
    </div>
  </div>

  <!-- Info SMTP (solo lectura desde .env) -->
  <div class="card">
    <div class="card__header">
      <span class="card__title">Configuración SMTP</span>
    </div>
    <div class="card__body">
      <p style="font-size:13px;color:var(--slate);margin-bottom:16px;line-height:1.6">
        La configuración SMTP se gestiona en el archivo <code style="background:var(--gray-100);padding:2px 5px;border-radius:4px;font-size:12px">.env</code> en la raíz del proyecto.
      </p>
      <table style="width:100%;border-collapse:collapse;font-size:13px">
        <?php foreach ($smtpInfo as $label => $value): ?>
        <tr style="border-bottom:1px solid var(--gray-100)">
          <td style="padding:8px 0;color:var(--gray-400);font-weight:600;width:110px"><?= $label ?></td>
          <td style="padding:8px 0;color:var(--dark);font-weight:600"><?= htmlspecialchars($value) ?></td>
        </tr>
        <?php endforeach; ?>
      </table>
      <div style="margin-top:16px;padding:12px;background:var(--yellow-bg);border-radius:6px;font-size:12px;color:#92400e;line-height:1.6">
        Para cambiar el servidor SMTP, edita el archivo <code>.env</code> y el password <code>SMTP_PASS</code> directamente en el servidor.
      </div>
    </div>
  </div>

</div>

<!-- Test de conexión SMTP -->
<div class="card" style="margin-top:20px">
  <div class="card__header">
    <span class="card__title">Probar envío de email</span>
  </div>
  <div class="card__body">
    <p style="font-size:13px;color:var(--slate);margin-bottom:16px">Envía un email de prueba para verificar que la configuración SMTP funciona correctamente.</p>
    <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
      <input type="email" id="testEmail" class="form-control" style="max-width:280px" placeholder="Enviar prueba a..." value="<?= htmlspecialchars($currentEmail) ?>">
      <button class="btn btn--dark" id="testEmailBtn" onclick="sendTestEmail()">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="width:15px;height:15px"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
        Enviar email de prueba
      </button>
      <span id="testEmailResult" style="font-size:13px"></span>
    </div>
  </div>
</div>

<script>
// Preview de hora en tiempo real al cambiar el selector
async function updateTzPreview() {
  const tz  = document.getElementById('tzSelect').value;
  const box = document.getElementById('tzPreviewText');
  try {
    const res  = await fetch(SITE_BASE + '/api/index.php/admin/timezone-preview?tz=' + encodeURIComponent(tz), {
      credentials: 'same-origin',
    });
    const data = await res.json();
    box.textContent = data.preview ?? '—';
  } catch(e) {
    box.textContent = '—';
  }
}

async function sendTestEmail() {
  const email  = document.getElementById('testEmail').value.trim();
  const btn    = document.getElementById('testEmailBtn');
  const result = document.getElementById('testEmailResult');

  if (!email) {
    result.textContent = 'Ingresa un email de destino.';
    result.style.color = '#dc2626';
    return;
  }

  btn.disabled    = true;
  btn.textContent = 'Enviando...';
  result.textContent = '';

  try {
    const res  = await fetch(SITE_BASE + '/api/index.php/admin/test-email', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'same-origin',
      body: JSON.stringify({ email }),
    });
    const data = await res.json();
    if (res.ok && data.success) {
      result.textContent = '✓ Email enviado correctamente.';
      result.style.color = '#16a34a';
    } else {
      result.textContent = '✗ Error: ' + (data.error || 'No se pudo enviar.');
      result.style.color = '#dc2626';
    }
  } catch(e) {
    result.textContent = '✗ Error de red.';
    result.style.color = '#dc2626';
  }

  btn.disabled  = false;
  btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="width:15px;height:15px"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg> Enviar email de prueba`;
}
</script>

<?php include '_layout_end.php'; ?>
