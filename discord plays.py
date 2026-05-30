import pydirectinput
import discord
import asyncio


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    user_message = message.content

    print(f"{user_message}")
    user_message = user_message.lower()
    if user_message.startswith('lw'):
        pydirectinput.keyDown('up')
        await asyncio.sleep(2.5)
        pydirectinput.keyUp('up')
    elif user_message.startswith('la'):
        pydirectinput.keyDown('left')
        await asyncio.sleep(2.5)
        pydirectinput.keyUp('left')
    elif user_message.startswith('ls'):
        pydirectinput.keyDown('down')
        await asyncio.sleep(2.5)
        pydirectinput.keyUp('down')
    elif user_message.startswith('ld'):
        pydirectinput.keyDown('right')
        await asyncio.sleep(2.5)
        pydirectinput.keyUp('right')
    elif user_message.startswith('qw'):
        pydirectinput.keyDown('up')
        await asyncio.sleep(0.1)
        pydirectinput.keyUp('up')
    elif user_message.startswith('qa'):
        pydirectinput.keyDown('left')
        await asyncio.sleep(0.1)
        pydirectinput.keyUp('left')
    elif user_message.startswith('qs'):
        pydirectinput.keyDown('down')
        await asyncio.sleep(0.1)
        pydirectinput.keyUp('down')
    elif user_message.startswith('qd'):
        pydirectinput.keyDown('right')
        await asyncio.sleep(0.1)
        pydirectinput.keyUp('right')
    elif user_message.startswith('w'):
        pydirectinput.keyDown('up')
        await asyncio.sleep(0.3)
        pydirectinput.keyUp('up')
    elif user_message.startswith('a'):
        pydirectinput.keyDown('left')
        await asyncio.sleep(0.3)
        pydirectinput.keyUp('left')
    elif user_message.startswith('s'):
        pydirectinput.keyDown('down')
        await asyncio.sleep(0.3)
        pydirectinput.keyUp('down')
    elif user_message.startswith('d'):
        pydirectinput.keyDown('right')
        await asyncio.sleep(0.3)
        pydirectinput.keyUp('right')
    elif user_message.startswith('z'):
        pydirectinput.press('z', presses=1, interval=0.0)
    elif user_message.startswith('x'):
        pydirectinput.press('x', presses=1, interval=0.0)
    elif user_message.startswith('c'):
        pydirectinput.press('c', presses=1, interval=0.0)
    else:
        pass

client.run("PUT YOUR BOTS TOKEN HERE (still in these quotes)")
