from pyrogram import Client, filters


@Client.on_message(filters.text & filters.incoming & filters.command("id"))
async def id(_, msg):
    await msg.reply(f"මෙන්න උබේ Chat ID එක : `{msg.chat.id}`", quote=True)
