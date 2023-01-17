from pyrogram import filters, Client

from pyrogram.types import Message

import asyncio
from Bot import bot

@bot.on_message(filters.command('hack'))

async def command1(bot, message):

  message=await message.reply_text("Looking for WhatsApp databases in targeted person...")

  #asyncio.sleep(2)

  await message.edit(" User online: True\nTelegram access: True\nRead Storage: True ")

  #asyncio.sleep(2)

  await message.edit("Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 20s")

  #asyncio.sleep(2)

  await message.edit("Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 18s")

  #asyncio.sleep(2)

  await message.edit("Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s")  

  #asyncio.sleep(2)

  await message.edit("Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s")

  #asyncio.sleep(2)

  await message.edit("Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s")

  #asyncio.sleep(2)

  await message.edit("Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s")

  #asyncio.sleep(2)

  await message.edit("Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s")

  #asyncio.sleep(2)

  await message.edit("Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s")

  #asyncio.sleep(2)

  await message.edit("Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s")

  #asyncio.sleep(2)

  await message.edit("Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s")

  #asyncio.sleep(2)

  await message.edit("Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s")

  #asyncio.sleep(2)

  await message.edit("Hacking complete!\nUploading file...")

  #asyncio.sleep(2)

  await message.edit("Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`")
