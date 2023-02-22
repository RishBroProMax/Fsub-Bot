#🪄🔎🔮💫♻️🚀🍁🎺🖥️⚔️🖌️🎧👻👹👨‍💻🧑‍💻👨‍✈️🕵️🤘👋🖐️🪄🎉✨🎞️🎀🎁♥️♦️🔊🎧🛠️🔒⚙️⛓️🔗📲📸📡🎥📷📹📼🔍🔍🔎📘📙📚🔖💵💶🪙💸💷💴

from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
🍁Hello {}

I m {}
Send /help Visit My Help Menu

🙈 For All Users 👇👇

🔥 Powered By Emo Network ✓
☘️ Simple & Friendly BOT ✓
💥 Keep Original Appearance ✓
🎯 Group Supported ✓
⚡️ Fast Response ✓
✅ 24 Hour Active ✓
🤩 New OS ✓

▣————————————————————————▣

🚀Powerd By @EmoBotDevolopers

▣————————————————————————▣
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")],
        [InlineKeyboardButton("🔥 Emo Bot Devolopers 🔥", url="https://t.me/EmoBotDevolopers")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("▣——————————————————▣", url="https://youtube.com/@Rish_Bro/")],
        [
            InlineKeyboardButton("❔ How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🌺 About 🌺", callback_data="about")
        ],
        [InlineKeyboardButton("👨‍💻 Devoloper 👨‍💻", url="https://t.me/{OWNER_USERNAME}}")],
        [InlineKeyboardButton("💬 Support 💬", url="https://t.me/EmoBotSupport")],
    ]

    
    # Comming Soon

COMMING = "Song Plugin is Comming Soon.. \n Join [Update Channel](t.me/EmoBotDevolopers) And Get Updates"

COMMING2 = "Logo Plugin is Comming Soon.. \n Join [Update Channel](t.me/EmoBotDevolopers) And Get Updates"
    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001742371821` or `/forcesubscribe -1001742371821`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

🔅 **Available Commands** 🔅

⟫ /fsub - See current force subscribe chat
⟫ /fsub chat_id/username - Force users to join the particular chat
⟫ /settings - Change Group Settings
⟫ /id - Get the chat id of any group or channel
⟫ /about - About The Bot
⟫ /help - This Message
⟫ /start - Start the Bot
⟫ /hack - Hack Target Whatsapp Account
⟫ /song - Comming Soon..
⟫ /logo - Comming Soon..

📌**Note** - You can also use `/forcesubscribe` instead of `/fsub`
📌**Note** - Get All Updates [Here](t.me/EmoBotDevolopers)

🔥 Powerd By [Emo Network](t.me/EmoBotDevolopers)
    """

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Force Subscribing Bot by @ImRishmika

🪄Powerd By : @EmoBotDevolopers

🍁Framework : [Pyrogram](docs.pyrogram.org)

🍁Language : [Python](www.python.org)

🍁Developer : @ImRishmika

🖥️ Host Sever : Unknow


    """
