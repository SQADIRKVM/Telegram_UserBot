from pyrogram import Client, filters
from Userbot import Config
from pyrogram.types.messages_and_media.message import Message
from Userbot.plugins.info import info

app = Client(Config.stringSession,
             api_id=Config.apiId,
             api_hash=Config.apiHash)

@app.on_message(filters.all)
async def main(bot: Client, event: Message):
    if event.from_user.is_self and event.text[0] == '.':
        # Bot command control
        # to avoid others from executing the bot

        cmd = event.text.replace('.', '')

        if cmd == 'info':
            await info(bot, event)
          # await event.edit(text=cmd)

    else:
        print('This from somebody')


app.run()
