import logging

from telethon import events
from telethon import TelegramClient, Button
from telethon.tl.functions.users import GetFullUserRequest as us
from byte_config import *


logging.basicConfig(level=logging.INFO)


byte = TelegramClient(
        "whisper",
        api_id=BYTEAPI_KEY,
        api_hash=BYTEAPI_HASH
        ).start(
                bot_token=BYTE_TOKEN
                )
db = {}

@byte.on(events.NewMessage(pattern="^[!?/]start$"))
async def stsrt(event):
    await event.reply(
            START_TEXT)


@byte.on(events.NewMessage(pattern="^[!?/]help$"))
async def helep(event):
    await event.reply(
            HELP_TEXT,
            buttons=[
                [Button.switch_inline("Go Inline", query="")]
                ]
            )


@byte.on(events.NewMessage(pattern="^[!?/]repo$"))
async def repos(event):
    await event.reply(
            REPO_TEXT,
            buttons=[
                [Button.url("Click Here", "https://github.com/The-UnknownDev")]
                ]
            )

    
@byte.on(events.InlineQuery())
async def inline(event):
    me = (await null.get_me()).username
    try:
        inp = event.text.split(None, 1)[1]
        user, msg = inp.split("|")
    except IndexError:
        await event.answer(
                [], 
                switch_pm=f"@{me} [Username]|[Message]",
                switch_pm_param="start"
                )
    except ValueError:
        await event.answer(
                [],
                switch_pm=f"Give a message too!",
                switch_pm_param="start"
                )
    try:
        ui = await null(us(user))
    except BaseException:
        await event.answer(
                [],
                switch_pm="Invalid User ID/Username",
                switch_pm_param="start"
                )
        return
    db.update({"user_id": ui.user.id, "msg": msg, "xxx": event.sender.id})
    byte_text = f"""
A Whisper Has Been Sent To [{ui.user.first_name}](tg://user?id={ui.user.id})!
Click The Below Button To See The Message!\n
**Note:** __Only {ui.user.first_name} can open this!__
    """
    deon = event.builder.article(
            title="Send your secret message!",
            description=f"Powered by {BYTEBOT_NAME}",
            url="https://t.me/TheByteBots",
            text=null_text,
            buttons=[
                [Button.inline(" Show Message 🔓 ", data="byte_")]
                ]
            )
    await event.answer(
            [deon],
            switch_pm="Yahoo! A secret message.",
            switch_pm_param="start"
            )


@byte.on(events.CallbackQuery(data="byte_"))
async def ws(event):
    user = int(db["user_id"])
    Arpit = [int(db["xxx"])]
    Arpit.append(user)
    if event.sender.id not in Arpit:
        await event.answer("🔐 This message is not for you !", alert=True)
        return
    msg = db["msg"]
    if msg == []:
        await event.anwswer(
                "Oops!\nIt's looks like message got deleted from my server!", alert=True)
        return
    await event.answer(msg, alert=True)


byte_txt = 'By github.com/The-UnknownDev | t.me/Arpit_Chaurasiya\n'
byte_txt += 'Any questions? Say it at t.me/ByteBotsSupprt\n'
byte_txt += f'{BYTEBOT_NAME} started! Developed and Maintaned by Arpit\n'
print(byte_txt)
byte.run_until_disconnected()
