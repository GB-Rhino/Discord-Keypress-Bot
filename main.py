import discord
import pydirectinput
import logging
import os

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
def handle_command(command):
    
    if command in command_map:
        pydirectinput.press(command_map[command])
        logging.info(f"Executed command: {command}, Key: {command_map[command]}")
        return f"Executed command: {command}"
    logging.warning(f"Command not recognized: {command}")
    return "Command not recognized."

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print("Ready and listening...")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    print(f"Received message: '{message.content}' from {message.author}")

    
    if message.content.startswith('!cmd '):
        command = message.content[5:].strip()  
        response = handle_command(command)
        await message.channel.send(response)
    else:
        print("Message did not start with '!cmd '")


token = os.getenv("DPG_DISCORD_TOKEN")

client.run(token)