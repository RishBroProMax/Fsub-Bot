import os
import pyrogram
from config import Config
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions
from pyrogram.types import (Message, InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent,
                            InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)

from ForceSubscribeBot import bot as app
from ForceSubscribeBot.dbase import (
    get_served_users,
    add_served_user,
    remove_served_user,
    get_served_chats,
    add_served_chat,
    remove_served_chat
)

async def broadcast_messages(user_id, message):
    try:
        await message.forward(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        await remove_served_user(user_id)
        return False, "Deleted"
    except UserIsBlocked:
        await remove_served_user(user_id)
        return False, "Blocked"
    except PeerIdInvalid:
        await remove_served_user(user_id)
        return False, "Error"
    except Exception as e:
        return False, "Error"

@app.on_message(filters.private & filters.command("bcast") & filters.user({OWNER_ID}) & filters.reply)
async def broadcast_message(_, message):
    b_msg = message.reply_to_message
    chats = await get_served_users()
    m = await message.reply_text("❤️‍🔥 | Broadcast in progress... 😴")
    for chat in chats:
        try:
            await broadcast_messages(int(chat['bot_users']), b_msg)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await m.edit(f"""▰▰""")
    await m.edit(f"""▰▰▰▰""")
    await m.edit(f"""▰▰▰▰▰▰""")
    await m.edit(f"""▰▰▰▰▰▰▰▰""")
    await m.edit(f"""▰▰▰▰▰▰▰▰▰▰""")
    await m.edit(f"""⌜Sending Your Messege..⌟""")
    await m.edit(f"""❤️‍🔥 | Broadcast !""")
    await m.edit(f"""❤️‍🔥 | Broadcast Completed. ☘️""")
    
