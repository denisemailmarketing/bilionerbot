# 💼 ZERO → BILLION — Telegram Oyun Botu

Sıfırdan milyarder olma yolculuğu! İş kararları, riskler ve stratejilerle dolu bir metin RPG.

---

## 🎮 Özellikler

- **33 oyun sahnesi** + 10 farklı final
- **8 bölüm**: Başlangıç → İmparatorluk
- **5 parametre**: Para, İtibar, Tecrübe, Bağlantılar, Risk
- SQLite ile ilerleme ve geçmiş kaydı
- Tam Türkçe arayüz
- Inline butonlarla kolay oynanış

---

## 🚀 Kurulum

### 1. Repoyu klonla veya dosyaları indir

```bash
git clone <repo-url>
cd billionaire_bot
```

### 2. Python ortamı oluştur (önerilen)

```bash
python -m venv venv

# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Bağımlılıkları yükle

```bash
pip install -r requirements.txt
```

### 4. .env dosyasını oluştur

```bash
cp .env.example .env
```

`.env` dosyasını aç ve `BOT_TOKEN` değerini gir:

```
BOT_TOKEN=1234567890:ABCDefGhIJKlmNoPQRsTUVwxyZ
```

> **Token nereden alınır?**
> Telegram'da [@BotFather](https://t.me/BotFather)'a git → `/newbot` → token al

### 5. Botu başlat

```bash
python main.py
```

---

## 📁 Proje Yapısı

```
billionaire_bot/
│
├── main.py          # Ana bot — handler'lar, komutlar
├── db.py            # SQLite veritabanı işlemleri
├── game_data.py     # Tüm sahneler ve final sonuçları
├── keyboards.py     # Inline klavye tanımları
├── config.py        # .env okuma ve ayarlar
├── requirements.txt # Python bağımlılıkları
├── .env.example     # Örnek ortam değişkenleri
└── README.md        # Bu dosya
```

---

## 🎯 Oyun Komutları

| Komut | Açıklama |
|-------|----------|
| `/start` | Oyuna hoş geldin ekranı |
| `/profile` | Parametrelerini gör |
| `/reset` | İlerlemeyi sıfırla |
| `/help` | Kurallar ve finaller |

---

## 🏁 10 Final

| Final | Koşul |
|-------|-------|
| 🏆 Efsane Milyarder | Para ≥ 1B$, İtibar > 50, Risk < 60 |
| 💸 İflas | Para ≤ 0 |
| ⚖️ Tutuklanma | Risk ≥ 90 |
| 👑 Gizli Patron | Bağlantılar > 80, İtibar < 20 |
| 🎤 Medya Yıldızı | İtibar > 80, Para < 1B$ |
| 🚀 Teknoloji Devi | Tecrübe > 80, Para > 500M$ |
| 📊 Yatırımcı | Para > 400M$, Bağlantılar > 60 |
| 😈 Nefret Edilen Zengin | Para ≥ 1B$, İtibar < 0 |
| 🌍 Global Güç | Bağlantılar > 80, Para ≥ 500M$ |
| 🏖️ Her Şeyi Satıp Kaybolan | Para ≥ 1B$, Risk > 60 |

---

## 🛠 Gereksinimler

- Python 3.11+
- aiogram 3.x
- SQLite (Python ile birlikte gelir)

---

## 📝 Notlar

- Veritabanı `game.db` dosyasında saklanır
- Her kullanıcının ayrı ilerleme kaydı vardır
- `/reset` komutu tüm geçmişi siler
- Bot çalışırken `Ctrl+C` ile durdurulabilir
