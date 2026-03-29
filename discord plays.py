import pydirectinput
import discord
import asyncio


intents = discord.Intents.default()
intents.message_content = True
commands = ['w', 'a', 's', 'd', 'lA', 'lW', 'lS', 'lD', 'qW', 'qA', 'qS', 'qD', 'z', 'x', 'c',]

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    user_message = message.content

    print(f"{user_message}")
    if not user_message.startswith(tuple(commands)):
        await message.channel.send("Command Invalid.")  
    elif user_message.startswith('w') and not user_message.startswith('l') and not user_message.startswith('q'):
        pydirectinput.keyDown('up')
        await asyncio.sleep(0.3)
        pydirectinput.keyUp('up')
    elif user_message.startswith('a') and not user_message.startswith('l') and not user_message.startswith('q'):
        pydirectinput.keyDown('left')
        await asyncio.sleep(0.3)
        pydirectinput.keyUp('left')
    elif user_message.startswith('s') and not user_message.startswith('l') and not user_message.startswith('q'):
        pydirectinput.keyDown('down')
        await asyncio.sleep(0.3)
        pydirectinput.keyUp('down')
    elif user_message.startswith('d') and not user_message.startswith('l') and not user_message.startswith('q'):
        pydirectinput.keyDown('right')
        await asyncio.sleep(0.3)
        pydirectinput.keyUp('right')
    elif user_message.startswith('lW'):
        pydirectinput.keyDown('up')
        await asyncio.sleep(2.5)
        pydirectinput.keyUp('up')
    elif user_message.startswith('lA'):
        pydirectinput.keyDown('left')
        await asyncio.sleep(2.5)
        pydirectinput.keyUp('left')
    elif user_message.startswith('lS'):
        pydirectinput.keyDown('down')
        await asyncio.sleep(2.5)
        pydirectinput.keyUp('down')
    elif user_message.startswith('lD'):
        pydirectinput.keyDown('right')
        await asyncio.sleep(2.5)
        pydirectinput.keyUp('right')
    elif user_message.startswith('qW'):
        pydirectinput.keyDown('up')
        await asyncio.sleep(0.1)
        pydirectinput.keyUp('up')
    elif user_message.startswith('qA'):
        pydirectinput.keyDown('left')
        await asyncio.sleep(0.1)
        pydirectinput.keyUp('left')
    elif user_message.startswith('qS'):
        pydirectinput.keyDown('down')
        await asyncio.sleep(0.1)
        pydirectinput.keyUp('down')
    elif user_message.startswith('qD'):
        pydirectinput.keyDown('right')
        await asyncio.sleep(0.1)
        pydirectinput.keyUp('right')
    elif user_message.startswith('z'):
        pydirectinput.press('z', presses=1, interval=0.0)
    elif user_message.startswith('x'):
        pydirectinput.press('x', presses=1, interval=0.0)
    elif user_message.startswith('c'):
        pydirectinput.press('c', presses=1, interval=0.0)

client.run("PUT YOUR BOTS TOKEN HERE (still in these quotes)")