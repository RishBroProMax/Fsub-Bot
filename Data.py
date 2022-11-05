#🪄🔎🔮💫♻️🚀🍁🎺🖥️⚔️🖌️🎧👻👹👨‍💻🧑‍💻👨‍✈️🕵️🤘👋🖐️🪄🎉✨🎞️🎀🎁♥️♦️🔊🎧🛠️🔒⚙️⛓️🔗📲📸📡🎥📷📹📼🔍🔍🔎📘📙📚🔖💵💶🪙💸💷💴

from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
🍁Hello {}

Welcome to {}

I m Force Subscribe Bot !
Send /help Visit My Help Menu

🚀Powerd By @groupmoviex

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")],
        [InlineKeyboardButton("☣ Emo Bot Devolopers ☣", url="@groupmoviex")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🪄Demo Bot", url="@groupmoviex")],
        [
            InlineKeyboardButton("❔ How to Use ❔", callback_data="help"),
            InlineKeyboardButton("♾️ About ♾️", callback_data="about")
        ],
        [InlineKeyboardButton("👨‍💻 Devoloper 👨‍💻", url="@groupmoviex")],
        [InlineKeyboardButton("💬 Support 💬", url=""@groupmoviex )],
    ]
    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001742371821` or `/forcesubscribe -1001742371821`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

🔅 **Available Commands** 🔅

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`

Powerd By [Emo Network](@groupmoviex)
    """

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Force Subscribing Bot by @ImRishmika

🪄Powerd By : @groupmoviex

🍁Framework : [Pyrogram](docs.pyrogram.org)

🍁Language : [Python](www.python.org)

🍁Developer : @Riswan_x

🖥️Host Sever : Heroku
    """
