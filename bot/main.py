import os
from pyrogram import Client, filters
from pyrogram.types import Message

bot = Client(
    'classplus_bot',
    api_id=int(os.getenv('21567814')),
    api_hash=os.getenv('cd7dc5431d449fd795683c550d7bfb7e'),
    bot_token=os.getenv('8078418472:AAHN802dzlaLZX2D9g3URDTlic6W7IX0Fb4')
)

@bot.on_message(filters.command('start'))
async def start_cmd(client, message: Message):
    await message.reply_text('👋 Welcome to Classplus Extractor Bot!')

# You would include /drm, /batch, /txt handlers here

bot.run()
