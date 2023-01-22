from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Comming soon
@Client.on_message(filters.private & filters.incoming & filters.command("song"))
async def _help(bot, msg):
    await bot.send_message(
        msg.chat.id,
        "**Sorry !" + Data.COMMING,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )
    
# Comming Soon 
@Client.on_message(filters.private & filters.incoming & filters.command("logo"))
async def _help(bot, msg):
    await bot.send_message(
        msg.chat.id,
        "**Sorry !" + Data.COMMING2,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )
