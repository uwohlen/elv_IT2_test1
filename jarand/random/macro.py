from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
from pynput.keyboard import Controller
from pynput import mouse
from pynput import keyboard

mouse = pynput.mouse.Controller()
keyboard = Controller()

while True:
    if keyboard.is_pressed('u'):
        keyboard.press('w')
        keyboard.release('w')