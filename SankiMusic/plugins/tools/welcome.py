import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SankiMusic import app  

photo = [
    "https://telegra.ph/file/7483763c4d8dc3f2720cb.jpg",
    "https://telegra.ph/file/0c87c715c94cee2322a4b.jpg",
    "https://telegra.ph/file/1eb67c100ff8029ae585a.jpg",
    "https://telegra.ph/file/7a6b51ee0077724254ca7.jpg",
    "https://telegra.ph/file/c3ad58ec96bdce6969512.jpg",
    "https://telegra.ph/file/df9be8d763debc674b871.jpg",
    "https://telegra.ph/file/2b5b66c9a0989afa0779a.jpg",
    "https://telegra.ph/file/4500be253b16522c8d8f1.jpg",
    "https://telegra.ph/file/ab7d958d707ef649bc3c3.jpg",
    "https://telegra.ph/file/8ca939f4bb175f9ad1791.jpg",
    "https://telegra.ph/file/ecefaa3e00fb911826673.jpg",
    "https://telegra.ph/file/164fe8bb16dd1e77bfd85.jpg",
    "https://telegra.ph/file/1eb67c100ff8029ae585a.jpg",
    "https://telegra.ph/file/0c87c715c94cee2322a4b.jpg",
    "https://telegra.ph/file/7483763c4d8dc3f2720cb.jpg",
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🌷ʜᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
                f"**📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🔐𝐂ʜᴀᴛ 𝐔.𝐍:** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**💖𝐔ʀ 𝐈d:** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**✍️𝐔ʀ 𝐔.𝐍:** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🥳ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛ🥳", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
