# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Channel-Auto-Post-Bot/blob/main/LICENSE

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


FayasNoushad = Client(
    "Channel Auto Post Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
Hello {}, I am a channel auto post telegram bot.

Made by @FayasNoushad
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
        InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
        ],[
        InlineKeyboardButton('Source Code', url='https://github.com/FayasNoushad/Channel-Auto-Post-Bot')
        ]]
    )

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@FayasNoushad.on_message(filters.channel & (filters.video | filters.document))
async def autopost(bot, update):
    if (update.chat_id == -1001457054266):
    try:
        if "Ghermez" in update.file_name:
            await update.copy(chat_id=-1001166919373)
        elif "Chukurova" in update.file_name:
            await update.copy(chat_id=-1001437520825)
        elif "Mojeze" in update.file_name:
            await update.copy(chat_id=-1001071120514)
        elif "Yek Jonun Yek Eshgh" in update.file_name:
            await update.copy(chat_id=-1001546442991)
        elif "2020" in update.file_name:
            await update.copy(chat_id=-1001322014891)
        elif "Eshghe Mashroot" in update.file_name:
            await update.copy(chat_id=-1001409508844)
    except Exception as error:
        print(error)
