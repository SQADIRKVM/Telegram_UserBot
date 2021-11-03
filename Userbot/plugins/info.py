from pyrogram import Client
from pyrogram.types.messages_and_media.message import Message
async def info(bot: Client, event: Message):
    try:
        info = event.reply_to_message.from_user
    except:
        info = event.chat

    # print(info)

    userInfo = f"""
      **User Details**
      **Username: ** {info.username}
      **Id: ** {info.id}
      **First Name: ** {info.first_name}
      **Second Name: ** {info.last_name}
      **DC ID:** {info.dc_id}
      **Status: ** {info.status}
      **Contact: ** {info.is_contact}
      **Bot: ** {info.is_bot}
      **Fake: ** {info.is_fake}
      **Mutual: ** {info.is_mutual_contact}
      **Scam: ** {info.is_scam}
      **Verified: ** {info.is_verified}
    """
    try:
        dpImage=await bot.download_media(message=info.photo.big_file_id)
        await bot.send_photo(caption=userInfo,chat_id='me',photo=dpImage)
    except:
        await bot.send_message(chat_id='me',text=userInfo)
    await event.edit(text=" `Check Saved Messages for User Details` ")