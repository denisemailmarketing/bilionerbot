# main.py — Ana bot dosyası

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import db
import config
from game_data import SCENES, ENDINGS, determine_ending
from keyboards import (
    start_keyboard,
    choices_keyboard,
    restart_keyboard,
    profile_keyboard,
    confirm_reset_keyboard,
    back_to_game_keyboard,
)

# ─── Loglama ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

# ─── Bot ve Dispatcher ─────────────────────────────────────────────────────────
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


# ══════════════════════════════════════════════════════════════════════════════
# YARDIMCI FONKSİYONLAR
# ══════════════════════════════════════════════════════════════════════════════

def format_stats_short(player: dict) -> str:
    """Kısa istatistik özeti (sahne sonrası gösterim)"""
    money = player.get("money", 0)
    if money >= 1_000_000_000:
        money_str = f"{money/1_000_000_000:.1f}B$"
    elif money >= 1_000_000:
        money_str = f"{money/1_000_000:.1f}M$"
    elif money >= 1_000:
        money_str = f"{money/1_000:.1f}K$"
    else:
        money_str = f"{money:.0f}$"

    return (
        f"📊 <b>Güncel durum:</b>\n"
        f"💰 Para: {money_str}\n"
        f"⭐ İtibar: {player.get('reputation', 0)}\n"
        f"⚠️ Risk: {player.get('risk', 0)}/100"
    )


def format_profile(player: dict) -> str:
    """Tam profil gösterimi"""
    money = player.get("money", 0)
    if money >= 1_000_000_000:
        money_str = f"{money/1_000_000_000:.2f}B$ 🤑"
    elif money >= 1_000_000:
        money_str = f"{money/1_000_000:.2f}M$"
    elif money >= 1_000:
        money_str = f"{money/1_000:.1f}K$"
    else:
        money_str = f"{money:.0f}$"

    risk = player.get("risk", 0)
    risk_bar = "🟥" * (risk // 20) + "⬜" * (5 - risk // 20)

    rep = player.get("reputation", 0)
    rep_emoji = "😇" if rep > 50 else "😐" if rep > 0 else "😈"

    return (
        f"👤 <b>Oyuncu Profili</b>\n"
        f"{'─' * 25}\n"
        f"💰 Para: {money_str}\n"
        f"⭐ İtibar: {rep} {rep_emoji}\n"
        f"🧠 Tecrübe: {player.get('experience', 0)}/100\n"
        f"🤝 Bağlantılar: {player.get('connections', 0)}/100\n"
        f"⚠️ Risk: {risk}/100  {risk_bar}\n"
        f"📍 Bölüm: {player.get('stage', 1)}/8\n"
        f"🎯 Sahne: #{player.get('current_scene', 1)}"
    )


def get_or_create_player(user_id: int, username: str = "") -> dict:
    """Oyuncuyu getir, yoksa oluştur"""
    player = db.get_player(user_id)
    if not player:
        player = db.create_player(user_id, username)
    return player


async def send_scene(chat_id: int, user_id: int, scene_id: int | str):
    """Belirtilen sahneyi kullanıcıya gönder"""

    # Final kontrolü
    if scene_id == "final_check":
        player = db.get_player(user_id)
        ending_key = determine_ending(player)
        ending = ENDINGS.get(ending_key)

        db.update_player(user_id, {"is_finished": 1})

        text = (
            f"{'═' * 30}\n"
            f"🏁 <b>OYUN BİTTİ!</b>\n"
            f"{'═' * 30}\n\n"
            f"{ending['text']}\n\n"
            f"{'─' * 25}\n"
            f"{format_stats_short(player)}"
        )
        await bot.send_message(
            chat_id,
            text,
            parse_mode="HTML",
            reply_markup=restart_keyboard()
        )
        return

    # Sahneyi bul
    scene = SCENES.get(scene_id)
    if not scene:
        await bot.send_message(
            chat_id,
            "⚠️ Sahne bulunamadı. /reset komutuyla yeniden başlayabilirsin.",
            reply_markup=back_to_game_keyboard()
        )
        return

    # Sahne numarasını güncelle
    db.update_player(user_id, {"current_scene": scene_id})

    # Bölüm başlığı varsa ekle
    chapter = scene.get("chapter", "")
    scene_text = scene["text"]

    full_text = f"<b>{chapter}</b>\n{'─' * 25}\n\n{scene_text}" if chapter else scene_text

    await bot.send_message(
        chat_id,
        full_text,
        parse_mode="HTML",
        reply_markup=choices_keyboard(scene["choices"], scene_id)
    )


# ══════════════════════════════════════════════════════════════════════════════
# KOMUT İŞLEYİCİLERİ
# ══════════════════════════════════════════════════════════════════════════════

@dp.message(Command("start"))
async def cmd_start(message: Message):
    """Hoş geldin ekranı"""
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name or ""

    get_or_create_player(user_id, username)

    welcome_text = (
        "💼 <b>ZERO → BILLION oyununa hoş geldin!</b>\n\n"
        "Sıfırdan başlayıp milyarder olmaya hazır mısın?\n"
        "Her kararın paranı, itibarını, risk seviyeni ve geleceğini etkileyecek.\n\n"
        "🎯 <b>Nasıl oynanır?</b>\n"
        "• Her sahnede bir metin okursun\n"
        "• 3 seçenek arasından birini seçersin\n"
        "• Seçimlerin parametrelerini değiştirir\n"
        "• Sonunda 10 farklı finalden birine ulaşırsın!\n\n"
        "Başlamak için aşağıdaki butona bas."
    )

    await message.answer(
        welcome_text,
        parse_mode="HTML",
        reply_markup=start_keyboard()
    )


@dp.message(Command("profile"))
async def cmd_profile(message: Message):
    """Oyuncu profilini göster"""
    user_id = message.from_user.id
    player = get_or_create_player(user_id, message.from_user.username or "")

    await message.answer(
        format_profile(player),
        parse_mode="HTML",
        reply_markup=profile_keyboard()
    )


@dp.message(Command("reset"))
async def cmd_reset(message: Message):
    """Sıfırlama onayı iste"""
    await message.answer(
        "⚠️ <b>Dikkat!</b>\n\n"
        "Tüm ilerleme, para ve geçmiş silinecek!\n"
        "Sıfırlamak istediğinden emin misin?",
        parse_mode="HTML",
        reply_markup=confirm_reset_keyboard()
    )


@dp.message(Command("help"))
async def cmd_help(message: Message):
    """Oyun kurallarını göster"""
    help_text = (
        "📖 <b>ZERO → BILLION — Oyun Kuralları</b>\n\n"
        "🎯 <b>Amaç:</b> Sıfırdan başlayıp milyarder olmak!\n\n"
        "📊 <b>Parametreler:</b>\n"
        "💰 <b>Para</b> — Servetinin büyüklüğü\n"
        "⭐ <b>İtibar</b> — Kamuoyundaki imajın (-100 / +100)\n"
        "🧠 <b>Tecrübe</b> — İş bilgin ve deneyimin (0-100)\n"
        "🤝 <b>Bağlantılar</b> — İş ağın ve ilişkilerin (0-100)\n"
        "⚠️ <b>Risk</b> — Tehlike seviyenin (0-100)\n\n"
        "🏁 <b>Finaller (10 farklı son):</b>\n"
        "🏆 Efsane Milyarder\n"
        "💸 İflas\n"
        "⚖️ Tutuklanma\n"
        "👑 Gizli Patron\n"
        "🎤 Medya Yıldızı\n"
        "🚀 Teknoloji Devi\n"
        "📊 Yatırımcı\n"
        "😈 Nefret Edilen Zengin\n"
        "🌍 Global Güç\n"
        "🏖️ Her Şeyi Satıp Kaybolan\n\n"
        "📌 <b>Komutlar:</b>\n"
        "/start — Oyuna giriş\n"
        "/profile — İstatistiklerim\n"
        "/reset — Sıfırla\n"
        "/help — Bu mesaj"
    )

    await message.answer(help_text, parse_mode="HTML", reply_markup=back_to_game_keyboard())


# ══════════════════════════════════════════════════════════════════════════════
# CALLBACK İŞLEYİCİLERİ
# ══════════════════════════════════════════════════════════════════════════════

@dp.callback_query(F.data == "start_game")
async def cb_start_game(callback: CallbackQuery):
    """Oyunu başlat"""
    user_id = callback.from_user.id
    player = get_or_create_player(user_id, callback.from_user.username or "")

    await callback.message.edit_reply_markup(reply_markup=None)

    # Zaten oynuyor mu?
    current_scene = player.get("current_scene", 1)
    if current_scene > 1 and not player.get("is_finished"):
        await callback.message.answer(
            f"⚡ Kaldığın yerden devam ediyorsun (Sahne #{current_scene})..."
        )
    else:
        db.update_player(user_id, {"current_scene": 1, "is_finished": 0})
        current_scene = 1

    await callback.answer()
    await send_scene(callback.message.chat.id, user_id, current_scene)


@dp.callback_query(F.data == "continue_game")
async def cb_continue_game(callback: CallbackQuery):
    """Oyuna devam et"""
    user_id = callback.from_user.id
    player = get_or_create_player(user_id, callback.from_user.username or "")

    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer()

    if player.get("is_finished"):
        await callback.message.answer(
            "🏁 Oyun bitti! Yeniden başlamak için /start komutunu kullan.",
            reply_markup=restart_keyboard()
        )
        return

    current_scene = player.get("current_scene", 1)
    await send_scene(callback.message.chat.id, user_id, current_scene)


@dp.callback_query(F.data.startswith("choice:"))
async def cb_choice(callback: CallbackQuery):
    """Oyuncu seçimi işle"""
    user_id = callback.from_user.id
    player = db.get_player(user_id)

    if not player:
        await callback.answer("⚠️ Oyuncu bulunamadı. /start ile başla.", show_alert=True)
        return

    # Oyun bitmişse eski butona basma koruması
    if player.get("is_finished"):
        await callback.answer("🏁 Oyun zaten bitti! Yeniden başla.", show_alert=True)
        return

    # Callback verisini ayrıştır: choice:scene_id:choice_index
    try:
        _, scene_id_str, choice_idx_str = callback.data.split(":")
        scene_id = int(scene_id_str)
        choice_idx = int(choice_idx_str)
    except (ValueError, IndexError):
        await callback.answer("⚠️ Geçersiz seçim.", show_alert=True)
        return

    # Eski sahne koruması: oyuncu farklı sahnedeyse
    current_scene = player.get("current_scene", 1)
    if current_scene != scene_id:
        await callback.answer(
            "⏭️ Bu sahne geçmişte kaldı. Devam ediyorsun...",
            show_alert=False
        )
        await callback.message.edit_reply_markup(reply_markup=None)
        await send_scene(callback.message.chat.id, user_id, current_scene)
        return

    # Sahne ve seçimi doğrula
    scene = SCENES.get(scene_id)
    if not scene or choice_idx >= len(scene["choices"]):
        await callback.answer("⚠️ Sahne bulunamadı.", show_alert=True)
        return

    choice = scene["choices"][choice_idx]
    effects = choice.get("effects", {})
    next_scene = choice.get("next")

    # Efektleri uygula
    updated_player = db.apply_effects(user_id, effects)

    # Geçmişe kaydet
    db.save_history(user_id, scene_id, choice["text"], effects)

    # Butonları kaldır (seçildi)
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer(f"✅ Seçim: {choice['text'][:30]}...")

    # Kısa durum özeti gönder
    stats_text = format_stats_short(updated_player)
    await callback.message.answer(
        f"▶️ <b>{choice['text']}</b>\n\n{stats_text}",
        parse_mode="HTML"
    )

    # Sonraki sahneyi gönder
    if next_scene:
        await send_scene(callback.message.chat.id, user_id, next_scene)
    else:
        # Sonraki sahne yok = final
        await send_scene(callback.message.chat.id, user_id, "final_check")


@dp.callback_query(F.data == "restart_game")
async def cb_restart(callback: CallbackQuery):
    """Oyunu yeniden başlat"""
    user_id = callback.from_user.id
    username = callback.from_user.username or callback.from_user.first_name or ""

    db.reset_player(user_id, username)

    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer("🔄 Oyun sıfırlandı!")

    await callback.message.answer(
        "🔁 <b>Yeni oyun başlıyor!</b>\n\nBaşlangıç sermayesi: 💰 500$",
        parse_mode="HTML"
    )
    await send_scene(callback.message.chat.id, user_id, 1)


@dp.callback_query(F.data == "show_profile")
async def cb_show_profile(callback: CallbackQuery):
    """Profili göster"""
    user_id = callback.from_user.id
    player = get_or_create_player(user_id, callback.from_user.username or "")

    await callback.answer()
    await callback.message.answer(
        format_profile(player),
        parse_mode="HTML",
        reply_markup=profile_keyboard()
    )


@dp.callback_query(F.data == "confirm_reset")
async def cb_confirm_reset(callback: CallbackQuery):
    """Sıfırlama onayı"""
    await callback.answer()
    await callback.message.edit_text(
        "⚠️ <b>Emin misin?</b>\n\nTüm ilerleme silinecek!",
        parse_mode="HTML",
        reply_markup=confirm_reset_keyboard()
    )


@dp.callback_query(F.data == "do_reset")
async def cb_do_reset(callback: CallbackQuery):
    """Sıfırlamayı gerçekleştir"""
    user_id = callback.from_user.id
    username = callback.from_user.username or callback.from_user.first_name or ""

    db.reset_player(user_id, username)

    await callback.answer("✅ Sıfırlandı!")
    await callback.message.edit_text(
        "✅ <b>Oyun sıfırlandı!</b>\n\n/start ile yeniden başlayabilirsin.",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "cancel_reset")
async def cb_cancel_reset(callback: CallbackQuery):
    """Sıfırlamayı iptal et"""
    await callback.answer("İptal edildi.")
    await callback.message.edit_text(
        "❌ Sıfırlama iptal edildi.",
        reply_markup=back_to_game_keyboard()
    )


# ══════════════════════════════════════════════════════════════════════════════
# BAŞLANGIÇ
# ══════════════════════════════════════════════════════════════════════════════

async def main():
    """Botu başlat"""
    logger.info("Veritabanı başlatılıyor...")
    db.init_db()

    logger.info("Bot başlatılıyor...")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
