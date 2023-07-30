-import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app

@app.on_message(
    command(["صورص","سورس","السورس"])
)
async def huhh(client: Client, message: Message): 
    await message.reply_photo(
        photo=f"https://telegra.ph/file/641d9d6083e743c9b8e91.jpg",
        caption=f"""
╭──── • ◈ • ────╮ 
么  [- 𝐒𝐨𝐔𝐑𝐂𝐞 𝐒𝐩𝐨𝐓𝐢𝐅𝐘 ‌.](https://t.me/MF_CD)
么 [- 𝐃𝐞𝐕 𝐒𝐨𝐔𝐑𝐂𝐞  .](t.me/B_U_P) 
╰──── • ◈ • ────╯ 
  
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- 𝐒𝐨𝐔𝐑𝐂𝐞 𝐒𝐩𝐨𝐓𝐢𝐅𝐘 ‌.", url=f"https://t.me/MF_CD"),
                ],[
                    InlineKeyboardButton(
                        "- 𝐃𝐞𝐕 𝐒𝐨𝐔𝐑𝐂𝐞  .", user_id=1892491797),
                ],

            ]

        ),

    )