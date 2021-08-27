import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

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

@FayasNoushad.on_message(filters.channel & filters.edited & (filters.video | filters.document))
async def autopost(bot, update):
    media = update.video or update.document or update.audio
    if (update.chat.id == -1001264182630):
        try:
            if not "ghermez" in media.file_name:
                time.sleep(20)
                await update.copy(chat_id=-1001448973320)
        except Exception as error:
            print(error)
    
FayasNoushad.run()
