<?php

declare(strict_types=1);

function getDB(): PDO
{
    static $pdo = null;

    if ($pdo !== null) {
        return $pdo;
    }

    $dbPath = STORAGE_PATH . '/quotes.db';

    $pdo = new PDO('sqlite:' . $dbPath);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    $pdo->exec('PRAGMA journal_mode=WAL');
    $pdo->exec('PRAGMA foreign_keys=ON');

    migrate($pdo);

    return $pdo;
}

function migrate(PDO $pdo): void
{
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS quotes (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name  TEXT    NOT NULL,
            last_name   TEXT    NOT NULL DEFAULT '',
            email       TEXT    NOT NULL,
            phone       TEXT    NOT NULL,
            address     TEXT    NOT NULL DEFAULT '',
            zip_code    TEXT    NOT NULL,
            marketing_consent INTEGER NOT NULL DEFAULT 0,
            status      TEXT    NOT NULL DEFAULT 'pending',
            notes       TEXT    NOT NULL DEFAULT '',
            created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
            updated_at  TEXT    NOT NULL DEFAULT (datetime('now'))
        )
    ");

    $pdo->exec("
        CREATE TABLE IF NOT EXISTS settings (
            key   TEXT PRIMARY KEY,
            value TEXT NOT NULL DEFAULT ''
        )
    ");

    // Valores por defecto de settings
    $notifEmail = $_ENV['ADMIN_NOTIFICATION_EMAIL'] ?? '';
    $stmt = $pdo->prepare("INSERT OR IGNORE INTO settings (key, value) VALUES ('notification_email', ?)");
    $stmt->execute([$notifEmail]);

    $pdo->exec("INSERT OR IGNORE INTO settings (key, value) VALUES ('timezone', 'UTC')");
}
