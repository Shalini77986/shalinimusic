from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from SankiMusic.utilities.config import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✴️ᴄᴏᴍᴍᴀɴᴅs✴️",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="✮ sᴇᴛᴛɪɴɢs ✮", callback_data="settings_helper"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs✭", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ᴜᴘᴅᴀᴛᴇs ✭", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="✭ sᴜᴘᴘᴏʀᴛ ✭", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="✮💞 ᴍᴀɪɴᴛᴀɪɴᴇʀ 💞✮", url=f"https://t.me/Shalini_shalu_69"
            )
        ]
     ]
    return buttons
