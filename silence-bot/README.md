---
description: Checking microphone and send audio message to Telegram
---

# Silence bot

## Get started
1. Go to [@BotFather](https://t.me/BotFather)
2. Create a bot
3. Get the token
4. Go to **api.telegram.org/bot`{TOKEN}`/getMe** where `{TOKEN}` is your token
5. Add your bot as admin in `chanel` or as member in `dialog`

## Python 2
Requirements:
```shellsession
$ pip install pyaudio
$ pip install requests
```

Run:
```shellsession
$ python __init__.py
```
