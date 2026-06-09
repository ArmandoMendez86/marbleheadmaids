<?php
require_once '_auth.php';

// Bootstrap del API para usar los modelos directamente
define('ROOT_PATH', dirname(__DIR__));
define('API_PATH', ROOT_PATH . '/api');
define('STORAGE_PATH', ROOT_PATH . '/storage');

$autoload = ROOT_PATH . '/vendor/autoload.php';
if (!file_exists($autoload)) {
    die('<p style="font-family:sans-serif;padding:20px;color:red">Error: Run <code>composer install</code> in the project root.</p>');
}
require_once $autoload;

$dotenv = Dotenv\Dotenv::createImmutable(ROOT_PATH);
$dotenv->load();

require_once API_PATH . '/config/database.php';

use App\Models\QuoteModel;

$model   = new QuoteModel();

// Filtros desde GET
$statusFilter = $_GET['status'] ?? '';
$searchFilter = $_GET['search'] ?? '';
$page         = max(1, (int)($_GET['page'] ?? 1));

$result = $model->all([
    'status' => $statusFilter,
    'search' => $searchFilter,
    'page'   => $page,
]);
$counts = $model->countByStatus();

$quotes    = $result['data'];
$total     = $result['total'];
$lastPage  = $result['last_page'];

$statusLabels = [
    'pending'   => 'Pendiente',
    'contacted' => 'Contactado',
    'quoted'    => 'Cotizado',
    'booked'    => 'Reservado',
    'closed'    => 'Cerrado',
    'cancelled' => 'Cancelado',
];

$pageTitle = 'Solicitudes';
include '_layout.php';
?>

<!-- Stats -->
<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-card__num"><?= $counts['all'] ?></div>
    <div class="stat-card__label">Total</div>
  </div>
  <?php foreach (QuoteModel::STATUSES as $s): ?>
  <div class="stat-card">
    <div class="stat-card__num"><?= $counts[$s] ?></div>
    <div class="stat-card__label"><?= $statusLabels[$s] ?></div>
  </div>
  <?php endforeach; ?>
</div>

<!-- Tabla -->
<div class="card">
  <div class="card__header">
    <span class="card__title">Solicitudes de cotización</span>
  </div>

  <!-- Filtros -->
  <div style="padding:14px 20px; border-bottom:1px solid var(--gray-200);">
    <form method="GET" action="index.php" class="filters">
      <input
        type="search"
        name="search"
        class="form-control filters__search"
        placeholder="Buscar por nombre, email, teléfono..."
        value="<?= htmlspecialchars($searchFilter) ?>"
      >
      <select name="status" class="form-control filters__select" onchange="this.form.submit()">
        <option value="">Todos los estados</option>
        <?php foreach (QuoteModel::STATUSES as $s): ?>
          <option value="<?= $s ?>" <?= $statusFilter === $s ? 'selected' : '' ?>><?= $statusLabels[$s] ?></option>
        <?php endforeach; ?>
      </select>
      <button type="submit" class="btn btn--dark">Buscar</button>
      <?php if ($statusFilter || $searchFilter): ?>
        <a href="index.php" class="btn btn--ghost">Limpiar</a>
      <?php endif; ?>
    </form>
  </div>

  <div class="table-wrap">
    <?php if (empty($quotes)): ?>
      <div class="empty-state">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        <p>No hay solicitudes<?= $statusFilter || $searchFilter ? ' con esos filtros' : '' ?>.</p>
      </div>
    <?php else: ?>
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Nombre</th>
          <th>Email</th>
          <th>Teléfono</th>
          <th>Zip</th>
          <th>Estado</th>
          <th>Fecha</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <?php foreach ($quotes as $q): ?>
        <tr>
          <td style="color:var(--gray-400);font-size:13px"><?= $q['id'] ?></td>
          <td style="font-weight:600;color:var(--dark)"><?= htmlspecialchars($q['first_name'] . ' ' . $q['last_name']) ?></td>
          <td><?= htmlspecialchars($q['email']) ?></td>
          <td><?= htmlspecialchars($q['phone']) ?></td>
          <td><?= htmlspecialchars($q['zip_code']) ?></td>
          <td><span class="badge badge--<?= $q['status'] ?>"><?= $statusLabels[$q['status']] ?? $q['status'] ?></span></td>
          <td style="color:var(--gray-400);font-size:13px;white-space:nowrap"><?= formatDate($q['created_at'], 'M j, Y') ?></td>
          <td>
            <div class="row-actions">
              <a href="detail.php?id=<?= $q['id'] ?>" class="btn btn--ghost btn--sm" title="Ver / Editar">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="width:14px;height:14px"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                Ver
              </a>
              <button class="btn btn--danger btn--sm" onclick="confirmDelete(<?= $q['id'] ?>, '<?= htmlspecialchars(addslashes($q['first_name'] . ' ' . $q['last_name'])) ?>')" title="Eliminar">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="width:14px;height:14px"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
              </button>
            </div>
          </td>
        </tr>
        <?php endforeach; ?>
      </tbody>
    </table>
    <?php endif; ?>
  </div>

  <!-- Paginación -->
  <?php if ($lastPage > 1): ?>
  <div class="pagination">
    <span class="pagination__info">Página <?= $page ?> de <?= $lastPage ?> (<?= $total ?> registros)</span>
    <?php
    $qs = http_build_query(array_filter(['status' => $statusFilter, 'search' => $searchFilter]));
    $qsPrefix = $qs ? $qs . '&' : '';
    ?>
    <a href="?<?= $qsPrefix ?>page=<?= max(1, $page - 1) ?>" class="page-btn <?= $page <= 1 ? 'disabled' : '' ?>">&lsaquo;</a>
    <?php for ($i = max(1, $page - 2); $i <= min($lastPage, $page + 2); $i++): ?>
      <a href="?<?= $qsPrefix ?>page=<?= $i ?>" class="page-btn <?= $i === $page ? 'active' : '' ?>"><?= $i ?></a>
    <?php endfor; ?>
    <a href="?<?= $qsPrefix ?>page=<?= min($lastPage, $page + 1) ?>" class="page-btn <?= $page >= $lastPage ? 'disabled' : '' ?>">&rsaquo;</a>
  </div>
  <?php endif; ?>
</div>

<!-- Modal confirmación eliminar -->
<div class="modal-overlay" id="deleteModal">
  <div class="modal-box">
    <h3>Eliminar solicitud</h3>
    <p id="deleteModalMsg">¿Estás seguro de que deseas eliminar esta solicitud? Esta acción no se puede deshacer.</p>
    <div class="modal-actions">
      <button class="btn btn--ghost" onclick="closeDeleteModal()">Cancelar</button>
      <button class="btn btn--danger" id="deleteConfirmBtn">Eliminar</button>
    </div>
  </div>
</div>

<script>
let deleteTargetId = null;

function confirmDelete(id, name) {
  deleteTargetId = id;
  document.getElementById('deleteModalMsg').textContent =
    '¿Eliminar la solicitud de ' + name + '? Esta acción no se puede deshacer.';
  document.getElementById('deleteModal').classList.add('open');
}

function closeDeleteModal() {
  document.getElementById('deleteModal').classList.remove('open');
  deleteTargetId = null;
}

document.getElementById('deleteConfirmBtn').addEventListener('click', async () => {
  if (!deleteTargetId) return;
  const btn = document.getElementById('deleteConfirmBtn');
  btn.textContent = 'Eliminando...';
  btn.disabled = true;

  try {
    const res = await fetch(SITE_BASE + '/api/index.php/admin/quotes/' + deleteTargetId, {
      method: 'DELETE',
      credentials: 'same-origin',
    });
    if (res.ok) {
      window.location.reload();
    } else {
      alert('Error al eliminar. Intenta de nuevo.');
      closeDeleteModal();
    }
  } catch(e) {
    alert('Error de red.');
    closeDeleteModal();
  }
});

document.getElementById('deleteModal').addEventListener('click', function(e) {
  if (e.target === this) closeDeleteModal();
});
</script>

<?php include '_layout_end.php'; ?>
