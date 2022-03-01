# file: mirror.py
from telethon import events
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import time
from config import (API_HASH, API_ID, SESSION_STRING,
                    CHANNELS_MAPPING, SOURCE_CHANNELS)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

# Обработчик новых сообщений
@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler_new_message(event):
    try:
        mirror_channel = CHANNELS_MAPPING.get(event.chat_id)
        if mirror_channel is None and len(mirror_channel) < 1:
            return
        sent = 0
        for c in mirror_channel:
            mirror_message_id = await client.send_message(c, event.message)
            sent += 1
            if sent > 50:
                sent = 0
                time.sleep(1)
    except Exception as e:
        print(e)

# Обработчик отредактированных сообщений

if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
