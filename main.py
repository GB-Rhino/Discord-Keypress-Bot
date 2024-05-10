import discord
import pydirectinput
import logging
import os
import pygetwindow as gw
import json
import unicodedata
from discord.ext import commands


bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

def load_config():
    try:
        with open("config.json", "r", encoding='utf-8') as file:
            return json.load(file)["games"]
    except Exception as e:
        logging.error(f"Failed to load configuration: {e}")
        return {}


configurations = load_config()

def normalize_text(text):
    return unicodedata.normalize('NFKC', text)

def is_valid_game_window(configs):
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            active_window_title = normalize_text(active_window.title)
            logging.info(f"Currently focused window: '{active_window_title}'")
            for game_title in configs.keys():
                normalized_game_title = normalize_text(game_title)
                logging.info(f"Checking against config title: '{normalized_game_title}'")
                if normalized_game_title == active_window_title:
                    logging.info(f"Match found with config: '{game_title}'")
                    return True
            logging.info("No matching game found in configs for focused window.")
        else:
            logging.info("No window is currently focused.")
        return False
    except Exception as e:
        logging.error(f"Error during active window check: {e}")
        return False



def get_active_game(configs):
    try:
        windows = gw.getAllTitles()
       # logging.info(f"Windows currently open: {windows}")
        if windows:
            for title, config in configs.items():
                for window in windows:
                    if title in window:
                        logging.info(f"Active game configuration found: '{title}'")
                        return config
        logging.info("No matching game window is active.")
    except Exception as e:
        logging.error(f"Error fetching or processing window titles: {e}")
    return None


def handle_command(command_map, command):
    if command in command_map:
        print(command)
        action = command_map[command]
        if action == "left_mouse":
            pydirectinput.click()
            logging.info(f"Executed command: {command}, Key: left mouse click")
        else:
            pydirectinput.press(command_map[command])
            logging.info(f"Executed command: {command}, Key: {command_map[command]}")
            return f"Executed command: {command}"
    else:
        logging.warning(f"Command not recognized: {command}")
        return "Command not recognized."

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself

    if message.content.startswith('!cmd '):
        command_text = message.content[5:].strip().lower()  # Extract the command after '!cmd '
        
        if is_valid_game_window(configurations):  # Check if the active window is a valid game
            active_game_config = get_active_game(configurations)  # Fetch the active game configuration
            if active_game_config:
                response = handle_command(active_game_config['commands'], command_text)
                await message.channel.send(response)  # Pass the correct command map
            else:
                await message.channel.send("The game window is not recognized or not focused. Please focus on a valid game window to proceed.")
        else:
            await message.channel.send("The game window is not maximized or focused. Please maximize and focus the window to proceed.")
    else:
        print(f"Message not starting with '!cmd ': {message.content}")



token = os.getenv("DPG_DISCORD_TOKEN")
client.run(token)
