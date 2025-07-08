import os
from pyrogram import Client, filters
from pyrogram.types import Message

bot = Client(
    'classplus_bot',
    api_id=int(os.getenv('API_ID')),
    api_hash=os.getenv('API_HASH'),
    bot_token=os.getenv('BOT_TOKEN')
)

@bot.on_message(filters.command('start'))
async def start_cmd(client, message: Message):
    await message.reply_text('👋 Welcome to Classplus Extractor Bot!')

# You would include /drm, /batch, /txt handlers here

bot.run()
