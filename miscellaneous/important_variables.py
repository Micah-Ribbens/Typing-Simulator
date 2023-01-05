from tkinter import Entry, Button, PhotoImage, Tk, OptionMenu, Menu, Frame, Label, Canvas, ttk
import json

from miscellaneous.colors import *

SCREEN_LENGTH = 2200
SCREEN_HEIGHT = 1300

BACKGROUND_COLOR = light_gray

# Window
WINDOW = Tk()
WINDOW.configure(bg=BACKGROUND_COLOR)
WINDOW.title('Auto GUI')
WINDOW.geometry(f'{SCREEN_LENGTH}x{SCREEN_HEIGHT}')

# Fonts
FONT_NAME = "Arial"
MINISCULE_FONT = [FONT_NAME, 5]
TINY_FONT = [FONT_NAME, 8]
SMALL_FONT = [FONT_NAME, 11]
NORMAL_FONT = [FONT_NAME, 16]
LARGE_FONT = [FONT_NAME, 20]

# Loading JSON File
configuration_file_path = json.load(open("configurations/current_configuration.json", "r")).get("currentConfigurationFile")
configuration_file = json.load(open(configuration_file_path, "r"))

BASE_FILE_DIRECTORY = configuration_file.get("baseFileDirectory")
FILE_WRITTEN_TO_DIRECTORY = BASE_FILE_DIRECTORY

