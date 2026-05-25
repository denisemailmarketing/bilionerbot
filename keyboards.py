# keyboards.py — Inline klavyeler ve butonlar

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keyboard() -> InlineKeyboardMarkup:
    """Başlangıç ekranı klavyesi"""
    builder = InlineKeyboardBuilder()
    builder.button(text="🚀 Oyuna Başla", callback_data="start_game")
    return builder.as_markup()


def choices_keyboard(choices: list, scene_id: int) -> InlineKeyboardMarkup:
    """Sahne seçenekleri klavyesi"""
    builder = InlineKeyboardBuilder()
    for i, choice in enumerate(choices):
        builder.button(
            text=choice["text"],
            callback_data=f"choice:{scene_id}:{i}"
        )
    builder.adjust(1)  # Her buton ayrı satırda
    return builder.as_markup()


def restart_keyboard() -> InlineKeyboardMarkup:
    """Oyun sonu - yeniden başla klavyesi"""
    builder = InlineKeyboardBuilder()
    builder.button(text="🔁 Yeniden Başla", callback_data="restart_game")
    builder.button(text="📊 Profili Gör", callback_data="show_profile")
    builder.adjust(1)
    return builder.as_markup()


def profile_keyboard() -> InlineKeyboardMarkup:
    """Profil ekranı altındaki butonlar"""
    builder = InlineKeyboardBuilder()
    builder.button(text="▶️ Oyuna Devam Et", callback_data="continue_game")
    builder.button(text="🔁 Sıfırla", callback_data="confirm_reset")
    builder.adjust(1)
    return builder.as_markup()


def confirm_reset_keyboard() -> InlineKeyboardMarkup:
    """Sıfırlama onayı klavyesi"""
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Evet, Sıfırla", callback_data="do_reset")
    builder.button(text="❌ Hayır, İptal", callback_data="cancel_reset")
    builder.adjust(2)
    return builder.as_markup()


def back_to_game_keyboard() -> InlineKeyboardMarkup:
    """Oyuna geri dön butonu"""
    builder = InlineKeyboardBuilder()
    builder.button(text="▶️ Oyuna Devam Et", callback_data="continue_game")
    return builder.as_markup()
