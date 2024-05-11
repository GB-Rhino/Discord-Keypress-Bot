## PURELY FOR TESTING PURPOSES/LEARNING - USED TO DETERMINE PROCESS NAMES ##

import pygetwindow as gw
import logging
import unicodedata
import json




def get_current_window():
    processes = gw.getAllTitles()
    return processes

def get_active_window():
    active_window = gw.getActiveWindow()
    return active_window

def normalize_text(text):
    return unicodedata.normalize('NFKC', text)



def load_config_file():
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            return json.load(file)["games"]["Pokemon - Emerald Version (U) - VisualBoyAdvance-M 2.1.7"]
    except Exception as e:
        logging.error(f"Failed to load configuration: {e}")
        return {}
    
    

config = load_config_file()
print(config)


