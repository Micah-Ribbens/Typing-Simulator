from tkinter import Entry, Button, PhotoImage, Tk, OptionMenu, Menu, Frame, Label, Canvas, ttk
import json

from miscellaneous.colors import *

SCREEN_LENGTH = 860
SCREEN_HEIGHT = 750

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
configuration_file = json.load(open(configuration_file_path))

BASE_FILE_DIRECTORY = configuration_file.get("baseFileDirectory")
FILE_WRITTEN_TO_DIRECTORY = configuration_file.get("fileWrittenToDirectory")
DEFAULT_STOP_CHARACTER = configuration_file.get("defaultStopCharacter")
DEFAULT_TIME_NEEDED_FOR_NEW_CHARACTER = configuration_file.get("defaultTimeNeededForNewCharacter")
DEFAULT_BASE_FILE = configuration_file.get("defaultBaseFile")
DEFAULT_FILE_WRITTEN_TO = configuration_file.get("defaultFileWrittenTo")


