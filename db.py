# db.py — SQLite veritabanı yönetimi

import sqlite3
import json
import logging
from typing import Optional

logger = logging.getLogger(__name__)

DB_PATH = "game.db"


def get_connection() -> sqlite3.Connection:
    """Veritabanı bağlantısı al"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Veritabanı tablolarını oluştur"""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS players (
                user_id     INTEGER PRIMARY KEY,
                username    TEXT,
                money       REAL    DEFAULT 500,
                reputation  INTEGER DEFAULT 0,
                experience  INTEGER DEFAULT 0,
                connections INTEGER DEFAULT 0,
                risk        INTEGER DEFAULT 0,
                stage       INTEGER DEFAULT 1,
                current_scene INTEGER DEFAULT 1,
                is_finished INTEGER DEFAULT 0,
                created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL,
                scene_id    INTEGER NOT NULL,
                choice_text TEXT,
                effects     TEXT,
                timestamp   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES players(user_id)
            )
        """)
        conn.commit()
    logger.info("Veritabanı başlatıldı.")


def get_player(user_id: int) -> Optional[dict]:
    """Oyuncu bilgilerini getir"""
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM players WHERE user_id = ?", (user_id,)
        ).fetchone()
        return dict(row) if row else None


def create_player(user_id: int, username: str = "") -> dict:
    """Yeni oyuncu oluştur"""
    with get_connection() as conn:
        conn.execute("""
            INSERT OR IGNORE INTO players (user_id, username)
            VALUES (?, ?)
        """, (user_id, username or ""))
        conn.commit()
    return get_player(user_id)


def update_player(user_id: int, updates: dict):
    """Oyuncu parametrelerini güncelle"""
    if not updates:
        return

    # Geçerli alanlar
    valid_fields = {
        "money", "reputation", "experience",
        "connections", "risk", "stage",
        "current_scene", "is_finished", "username"
    }
    filtered = {k: v for k, v in updates.items() if k in valid_fields}
    if not filtered:
        return

    filtered["updated_at"] = "CURRENT_TIMESTAMP"
    set_clause = ", ".join(
        f"{k} = CURRENT_TIMESTAMP" if v == "CURRENT_TIMESTAMP" else f"{k} = ?"
        for k, v in filtered.items()
    )
    values = [v for v in filtered.values() if v != "CURRENT_TIMESTAMP"]
    values.append(user_id)

    with get_connection() as conn:
        conn.execute(
            f"UPDATE players SET {set_clause} WHERE user_id = ?",
            values
        )
        conn.commit()


def apply_effects(user_id: int, effects: dict) -> dict:
    """
    Sahne efektlerini oyuncuya uygula.
    Parametreleri artır/azalt, sınır kontrolleri yap.
    Güncellenmiş oyuncu bilgisini döndür.
    """
    player = get_player(user_id)
    if not player:
        return {}

    new_vals = {}

    if "money" in effects:
        new_vals["money"] = max(0, player["money"] + effects["money"])

    if "reputation" in effects:
        new_vals["reputation"] = max(-100, min(100, player["reputation"] + effects["reputation"]))

    if "experience" in effects:
        new_vals["experience"] = max(0, min(100, player["experience"] + effects["experience"]))

    if "connections" in effects:
        new_vals["connections"] = max(0, min(100, player["connections"] + effects["connections"]))

    if "risk" in effects:
        new_vals["risk"] = max(0, min(100, player["risk"] + effects["risk"]))

    if new_vals:
        set_parts = ", ".join(f"{k} = ?" for k in new_vals)
        values = list(new_vals.values()) + [user_id]
        with get_connection() as conn:
            conn.execute(
                f"UPDATE players SET {set_parts}, updated_at = CURRENT_TIMESTAMP WHERE user_id = ?",
                values
            )
            conn.commit()

    return get_player(user_id)


def save_history(user_id: int, scene_id: int, choice_text: str, effects: dict):
    """Oyuncu seçimini geçmişe kaydet"""
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO history (user_id, scene_id, choice_text, effects)
            VALUES (?, ?, ?, ?)
        """, (user_id, scene_id, choice_text, json.dumps(effects, ensure_ascii=False)))
        conn.commit()


def reset_player(user_id: int, username: str = ""):
    """Oyuncu ilerlemesini sıfırla"""
    with get_connection() as conn:
        conn.execute("""
            UPDATE players
            SET money=500, reputation=0, experience=0,
                connections=0, risk=0, stage=1,
                current_scene=1, is_finished=0,
                updated_at=CURRENT_TIMESTAMP
            WHERE user_id = ?
        """, (user_id,))
        conn.execute(
            "DELETE FROM history WHERE user_id = ?", (user_id,)
        )
        conn.commit()


def get_player_history(user_id: int, limit: int = 10) -> list:
    """Oyuncunun son seçimlerini getir"""
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT scene_id, choice_text, timestamp
            FROM history
            WHERE user_id = ?
            ORDER BY id DESC
            LIMIT ?
        """, (user_id, limit)).fetchall()
        return [dict(r) for r in rows]
