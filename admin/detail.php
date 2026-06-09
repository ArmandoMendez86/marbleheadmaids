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

use App\Models\QuoteModel;

$model = new QuoteModel();
$id    = (int)($_GET['id'] ?? 0);
$quote = $id ? $model->find($id) : null;

if (!$quote) {
    header('Location: index.php');
    exit;
}

$success = '';
$error   = '';

// Procesar formulario de edición
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['_action'] ?? '';

    if ($action === 'update') {
        $data = [
            'first_name'  => trim($_POST['first_name'] ?? ''),
            'last_name'   => trim($_POST['last_name'] ?? ''),
            'email'       => strtolower(trim($_POST['email'] ?? '')),
            'phone'       => trim($_POST['phone'] ?? ''),
            'address'     => trim($_POST['address'] ?? ''),
            'zip_code'    => trim($_POST['zip_code'] ?? ''),
            'status'      => $_POST['status'] ?? $quote['status'],
            'notes'       => trim($_POST['notes'] ?? ''),
            'marketing_consent' => isset($_POST['marketing_consent']) ? 1 : 0,
        ];

        if (empty($data['first_name']) || empty($data['email']) || empty($data['phone']) || empty($data['zip_code'])) {
            $error = 'First Name, Email, Phone y Zip Code son requeridos.';
        } else {
            $quote   = $model->update($id, $data);
            $success = 'Solicitud actualizada correctamente.';
        }
    }
}

$statusLabels = [
    'pending'   => 'Pendiente',
    'contacted' => 'Contactado',
    'quoted'    => 'Cotizado',
    'booked'    => 'Reservado',
    'closed'    => 'Cerrado',
    'cancelled' => 'Cancelado',
];

$pageTitle = 'Solicitud #' . $id;
include '_layout.php';
?>

<div style="margin-bottom:16px">
  <a href="index.php" class="btn btn--ghost btn--sm">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="width:14px;height:14px"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
    Volver
  </a>
</div>

<?php if ($success): ?>
  <div class="alert alert--success"><?= htmlspecialchars($success) ?></div>
<?php endif; ?>
<?php if ($error): ?>
  <div class="alert alert--error"><?= htmlspecialchars($error) ?></div>
<?php endif; ?>

<div style="display:grid;grid-template-columns:1fr 320px;gap:20px;align-items:start">

  <!-- Formulario de edición -->
  <div class="card">
    <div class="card__header">
      <span class="card__title">Datos del cliente</span>
      <span class="badge badge--<?= $quote['status'] ?>"><?= $statusLabels[$quote['status']] ?? $quote['status'] ?></span>
    </div>
    <div class="card__body">
      <form method="POST" action="detail.php?id=<?= $id ?>">
        <input type="hidden" name="_action" value="update">

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
          <div class="form-group">
            <label class="form-label">First Name *</label>
            <input type="text" name="first_name" class="form-control" required value="<?= htmlspecialchars($quote['first_name']) ?>">
          </div>
          <div class="form-group">
            <label class="form-label">Last Name</label>
            <input type="text" name="last_name" class="form-control" value="<?= htmlspecialchars($quote['last_name']) ?>">
          </div>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
          <div class="form-group">
            <label class="form-label">Email *</label>
            <input type="email" name="email" class="form-control" required value="<?= htmlspecialchars($quote['email']) ?>">
          </div>
          <div class="form-group">
            <label class="form-label">Phone *</label>
            <input type="text" name="phone" class="form-control" required value="<?= htmlspecialchars($quote['phone']) ?>">
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Address</label>
          <input type="text" name="address" class="form-control" value="<?= htmlspecialchars($quote['address']) ?>">
        </div>

        <div class="form-group">
          <label class="form-label">Zip Code *</label>
          <input type="text" name="zip_code" class="form-control" required value="<?= htmlspecialchars($quote['zip_code']) ?>">
        </div>

        <div class="form-group">
          <label class="form-label">Estado</label>
          <select name="status" class="form-control">
            <?php foreach (QuoteModel::STATUSES as $s): ?>
              <option value="<?= $s ?>" <?= $quote['status'] === $s ? 'selected' : '' ?>><?= $statusLabels[$s] ?></option>
            <?php endforeach; ?>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Notas internas</label>
          <textarea name="notes" class="form-control"><?= htmlspecialchars($quote['notes']) ?></textarea>
        </div>

        <div class="form-group" style="display:flex;align-items:center;gap:8px">
          <input type="checkbox" id="marketing_consent" name="marketing_consent" <?= $quote['marketing_consent'] ? 'checked' : '' ?> style="width:16px;height:16px;accent-color:#ffc52f">
          <label for="marketing_consent" class="form-label" style="margin:0;cursor:pointer">Acepta recibir mensajes de marketing</label>
        </div>

        <div style="display:flex;gap:10px;margin-top:4px">
          <button type="submit" class="btn btn--primary">Guardar cambios</button>
          <a href="index.php" class="btn btn--ghost">Cancelar</a>
        </div>
      </form>
    </div>
  </div>

  <!-- Sidebar de info -->
  <div style="display:flex;flex-direction:column;gap:16px">

    <!-- Metadata -->
    <div class="card">
      <div class="card__header"><span class="card__title">Información</span></div>
      <div class="card__body" style="font-size:13px;display:flex;flex-direction:column;gap:10px">
        <div>
          <div style="color:var(--gray-400);font-weight:600;text-transform:uppercase;font-size:11px;letter-spacing:0.05em;margin-bottom:2px">ID</div>
          <div style="color:var(--dark);font-weight:700">#<?= $quote['id'] ?></div>
        </div>
        <div>
          <div style="color:var(--gray-400);font-weight:600;text-transform:uppercase;font-size:11px;letter-spacing:0.05em;margin-bottom:2px">Recibida</div>
          <div style="color:var(--dark)"><?= formatDate($quote['created_at'], 'M j, Y \a\t g:i a') ?></div>
        </div>
        <div>
          <div style="color:var(--gray-400);font-weight:600;text-transform:uppercase;font-size:11px;letter-spacing:0.05em;margin-bottom:2px">Actualizada</div>
          <div style="color:var(--dark)"><?= formatDate($quote['updated_at'], 'M j, Y \a\t g:i a') ?></div>
        </div>
        <div>
          <div style="color:var(--gray-400);font-weight:600;text-transform:uppercase;font-size:11px;letter-spacing:0.05em;margin-bottom:2px">Marketing</div>
          <div><?= $quote['marketing_consent'] ? '<span style="color:#16a34a;font-weight:600">Sí</span>' : '<span style="color:#9ca3af">No</span>' ?></div>
        </div>
      </div>
    </div>

    <!-- Acciones rápidas de status -->
    <div class="card">
      <div class="card__header"><span class="card__title">Cambiar estado rápido</span></div>
      <div class="card__body" style="display:flex;flex-direction:column;gap:8px">
        <?php foreach (QuoteModel::STATUSES as $s): ?>
          <?php if ($s !== $quote['status']): ?>
          <form method="POST" action="detail.php?id=<?= $id ?>">
            <input type="hidden" name="_action" value="update">
            <input type="hidden" name="first_name"  value="<?= htmlspecialchars($quote['first_name']) ?>">
            <input type="hidden" name="last_name"   value="<?= htmlspecialchars($quote['last_name']) ?>">
            <input type="hidden" name="email"       value="<?= htmlspecialchars($quote['email']) ?>">
            <input type="hidden" name="phone"       value="<?= htmlspecialchars($quote['phone']) ?>">
            <input type="hidden" name="address"     value="<?= htmlspecialchars($quote['address']) ?>">
            <input type="hidden" name="zip_code"    value="<?= htmlspecialchars($quote['zip_code']) ?>">
            <input type="hidden" name="notes"       value="<?= htmlspecialchars($quote['notes']) ?>">
            <?php if ($quote['marketing_consent']): ?><input type="hidden" name="marketing_consent" value="1"><?php endif; ?>
            <input type="hidden" name="status" value="<?= $s ?>">
            <button type="submit" class="btn btn--ghost btn--sm" style="width:100%;justify-content:center">
              → <?= $statusLabels[$s] ?>
            </button>
          </form>
          <?php endif; ?>
        <?php endforeach; ?>
      </div>
    </div>

    <!-- Eliminar -->
    <div class="card" style="border-color:#fecaca">
      <div class="card__header" style="border-bottom-color:#fecaca"><span class="card__title" style="color:#dc2626">Zona de peligro</span></div>
      <div class="card__body">
        <p style="font-size:13px;color:var(--slate);margin-bottom:12px">Eliminar esta solicitud de forma permanente. Esta acción no se puede deshacer.</p>
        <button class="btn btn--danger btn--sm" onclick="document.getElementById('deleteModal').classList.add('open')">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="width:14px;height:14px"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
          Eliminar solicitud
        </button>
      </div>
    </div>

  </div>
</div>

<!-- Modal de confirmación de eliminación -->
<div class="modal-overlay" id="deleteModal">
  <div class="modal-box">
    <h3>Eliminar solicitud</h3>
    <p>¿Estás seguro de que deseas eliminar la solicitud de <strong><?= htmlspecialchars($quote['first_name'] . ' ' . $quote['last_name']) ?></strong>? Esta acción no se puede deshacer.</p>
    <div class="modal-actions">
      <button class="btn btn--ghost" onclick="document.getElementById('deleteModal').classList.remove('open')">Cancelar</button>
      <button class="btn btn--danger" id="deleteConfirmBtn">Eliminar</button>
    </div>
  </div>
</div>

<script>
document.getElementById('deleteConfirmBtn').addEventListener('click', async () => {
  const btn = document.getElementById('deleteConfirmBtn');
  btn.textContent = 'Eliminando...';
  btn.disabled = true;

  try {
    const res = await fetch(SITE_BASE + '/api/index.php/admin/quotes/<?= $id ?>', {
      method: 'DELETE',
      credentials: 'same-origin',
    });
    if (res.ok) {
      window.location.href = 'index.php?deleted=1';
    } else {
      alert('Error al eliminar. Intenta de nuevo.');
      btn.textContent = 'Eliminar';
      btn.disabled = false;
    }
  } catch(e) {
    alert('Error de red.');
    btn.textContent = 'Eliminar';
    btn.disabled = false;
  }
});

document.getElementById('deleteModal').addEventListener('click', function(e) {
  if (e.target === this) this.classList.remove('open');
});
</script>

<?php include '_layout_end.php'; ?>
