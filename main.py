import discord
import pydirectinput
import logging
import os
import pygetwindow as gw

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)


command_map = {
    "roll": "space",  
    "up": "up",  
    "down": "down",
    "left": "left",
    "right": "right",
    "roll": "space",
    "forward": "w",
    "back": "s",
    "strafe_left": "a",
    "strafe_right": "d",
    "item": "r",
    "jump": "f",
    "crouch": "x",


}
## TITLE NEEDS TO BE CHANGED TO THE TITLE OF GAME WINDOW
def is_window_focused(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        return window.isActive
    except IndexError:
        print(f"No window found with the title '{window_title}'.")
        return False
    
def handle_command(command):
    if command in command_map:
        pydirectinput.press(command_map[command])
        logging.info(f"Executed command: {command}, Key: {command_map[command]}")
        return f"Executed command: {command}"
    logging.warning(f"Command not recognized: {command}")
    return "Command not recognized."

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!cmd '):
        if is_window_focused('ELDEN RING™'):
            command_text = message.content[5:].strip().lower()
            response = handle_command(command_text)
            await message.channel.send(response)
        else:
            await message.channel.send("The game window is not maximized. Please maximize the window to proceed.")
    else:
        print(f"Message not starting with '!cmd ': {message.content}")


token = os.getenv("DPG_DISCORD_TOKEN")

client.run(token)