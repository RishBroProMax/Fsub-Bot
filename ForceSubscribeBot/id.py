from pyrogram import Client, filters


@Client.on_message(filters.text & filters.incoming & filters.command("id"))
async def id(_, msg):
    await msg.reply(f"Chat ID : `{msg.chat.id}` \n Chat ID :- `{msg.user.id}`", quote=True)
