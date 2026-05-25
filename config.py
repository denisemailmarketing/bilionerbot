# config.py — Ayarlar ve çevre değişkenleri

import os
from dotenv import load_dotenv

load_dotenv()

# Bot token — .env dosyasından alınır
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

if not BOT_TOKEN:
    raise ValueError(
        "BOT_TOKEN bulunamadı! Lütfen .env dosyasını oluşturun.\n"
        "Örnek: BOT_TOKEN=1234567890:ABCDefGhIJKlmNoPQRsTUVwxyZ"
    )

# Veritabanı yolu
DB_PATH: str = os.getenv("DB_PATH", "game.db")

# Log seviyesi
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
