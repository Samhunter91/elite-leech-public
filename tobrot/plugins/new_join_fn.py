import logging

import pyrogram
from tobrot import AUTH_CHANNEL, LOGGER

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            f"""<b>🙋🏻‍♂️ Hello friend!\n\n Welcome to the group</b>\n\n<b>Current CHAT ID: <code>{message.chat.id}</code>""",
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Index Link', url='snowy-mountain.hikari-drive.workers.dev/')
                    ]
                ]
               )
            )
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    await message.reply_text(
        """Available Commands:
        /leech - Reply to supported link to upload it o Telegram.
        /savethumbnail - Reply to a photo to use it as thumbnail
        /clearthumbnail - To clear current thumbnail
        /extract - To extract from a archive link [Does't work with Telegram files]
        /rename- To rename a Telegram file. Be sure to add file extension too
        /renewme - To delete cached downloads in Heroku 
        """,
        disable_web_page_preview=True
        )
