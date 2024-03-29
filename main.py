import json
import os
import tkinter

from gui_components.grid_items import GridItems
from gui_components.input_field import InputField
from gui_components.titled_input_field import TitledInputField

from tkinter import filedialog

from tkinter import *
from gui_components.grid import Grid

from miscellaneous.utility_functions import *
import time


class MainScreen:
    """The Main Screen of the application"""

    base_file_field = TitledInputField(WINDOW, SMALL_FONT, DEFAULT_BASE_FILE, "Base File")
    file_written_to_field = TitledInputField(WINDOW, SMALL_FONT, DEFAULT_FILE_WRITTEN_TO, "File Written To")
    code_start_line_field = TitledInputField(WINDOW, SMALL_FONT, "START", "Code Start Line")
    code_end_line_field = TitledInputField(WINDOW, SMALL_FONT, "END", "Code End Line")
    time_needed_for_new_ch_field = TitledInputField(WINDOW, SMALL_FONT, DEFAULT_TIME_NEEDED_FOR_NEW_CHARACTER, "Time for New Ch")
    stop_ch_field = TitledInputField(WINDOW, SMALL_FONT, DEFAULT_STOP_CHARACTER, "Stop Character")

    select_base_file_button = Button(WINDOW, compound=tkinter.CENTER, text="Select Base File", bg=pleasing_green, fg=white, font=SMALL_FONT)
    select_file_written_to_button = Button(WINDOW, compound=tkinter.CENTER, text="Select File Written To", bg=pleasing_green, fg=white, font=SMALL_FONT)
    start_button = Button(WINDOW, compound=tkinter.CENTER, text="Start Button", bg=pleasing_green, fg=white, font=SMALL_FONT)

    all_fields = [select_file_written_to_button, select_base_file_button, base_file_field, code_start_line_field, code_end_line_field, file_written_to_field, time_needed_for_new_ch_field, stop_ch_field]

    start_button_height = get_measurement(SCREEN_HEIGHT, 10)
    start_button_length = SCREEN_LENGTH
    main_grid = None

    continue_button = Button(WINDOW, compound=tkinter.CENTER, text="Continue", bg=red, fg=white, font=SMALL_FONT)
    back_button = Button(WINDOW, compound=tkinter.CENTER, text="Back", bg=purple, fg=white, font=SMALL_FONT)
    restart_previous_section_button = Button(WINDOW, compound=tkinter.CENTER, text="Restart", bg=dodger_blue, fg=white, font=SMALL_FONT)

    # File Writing Stuff
    current_character_index = -1  # So it grabs the first ch of the file
    time_needed_for_new_ch = 0
    previous_start_index = 0
    previous_file_contents = ""
    current_file_contents = ""
    start_code = ""
    all_code_needing_writing = ""
    stop_ch = "&"
    file = None
    enter = """
"""
    valid_chs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#%^*()_-+=][{}|''/><.,`~:;" + enter + '/""\\ '

    def __init__(self):
        """Initializes the application"""

        self.set_up_start_screen()
        self.select_file_written_to_button.configure(command=lambda: self.select_file(self.file_written_to_field))
        self.select_base_file_button.configure(command=lambda: self.select_file(self.base_file_field))
        self.start_button.configure(command=self.start)

    def select_file(self, file_field):
        directory = BASE_FILE_DIRECTORY if file_field == self.base_file_field else FILE_WRITTEN_TO_DIRECTORY
        file_path = filedialog.askopenfilename(initialdir=directory)

        if file_path is not None and file_path != "":
            file_field.set_text(file_path)

    def start(self):
        """Starts running all the code that writes the files"""

        self.file = open(self.file_written_to_field.get_text(), "w+")
        self.time_needed_for_new_ch = float(self.time_needed_for_new_ch_field.get_text())
        self.stop_ch = self.stop_ch_field.get_text()

        file_lines = self.get_lines(self.base_file_field.get_text())
        start_code_index = self.get_number_text_value(self.code_start_line_field.get_text(), len(file_lines))
        end_code_index = self.get_number_text_value(self.code_end_line_field.get_text(), len(file_lines))

        self.all_code_needing_writing = get_string(file_lines[start_code_index:end_code_index + 1])
        start_code = get_string(file_lines[0:start_code_index])
        start_code = get_string_without_valid_chs(start_code, self.valid_chs)
        self.current_file_contents = start_code
        self.file.write(start_code)
        self.file.flush()

        for field in self.all_fields + [self.start_button]:
            field.place(x=0, y=0, width=0, height=0)

        self.continue_button.place(x=0, y=0, width=SCREEN_LENGTH, height=SCREEN_HEIGHT * .45)
        self.restart_previous_section_button.place(x=0, y=SCREEN_HEIGHT * .45, width=SCREEN_LENGTH, height=SCREEN_HEIGHT * .45)
        self.back_button.place(x=0, y=SCREEN_HEIGHT * .9, width=SCREEN_LENGTH, height=SCREEN_HEIGHT * .1)

        self.back_button.configure(command=self.go_back_to_editing_menu)
        self.continue_button.configure(command=self.continue_writing, bg=red)
        self.restart_previous_section_button.configure(command=self.restart_previous_section)


    def continue_writing(self):
        """Continues the writing of the file"""

        self.continue_button.configure(bg=pleasing_green)
        self.run_code_writing()
    
    def restart_previous_section(self):
        """Restarts the previous section, so you can record again"""

        self.current_character_index = self.previous_start_index
        self.previous_file_contents = get_string_without_valid_chs(self.previous_file_contents, self.valid_chs)

        self.file.close()
        self.file = open(self.file_written_to_field.get_text(), "w+")
        self.file.write(self.previous_file_contents)
        self.file.flush()
        self.current_file_contents = self.previous_file_contents

        self.continue_writing()

    def set_up_start_screen(self):
        """Shows all the start screen components"""

        self.main_grid = Grid([0, 0, SCREEN_LENGTH, SCREEN_HEIGHT - self.start_button_height], 2, None)
        self.main_grid.turn_into_grid(self.all_fields, None, None)

        self.start_button.place(x=0, y=SCREEN_HEIGHT - self.start_button_height, width=self.start_button_length, height=self.start_button_height)

    def go_back_to_editing_menu(self):
        """Makes the application go back to the original menu"""

        self.continue_button.place(x=0, y=0, width=0, height=0)
        self.back_button.place(x=0, y=0, width=0, height=0)
        self.restart_previous_section_button.place(x=0, y=0, width=0, height=0)
        self.current_character_index = -1
        self.set_up_start_screen()

    def get_number_text_value(self, text_value, number_of_lines_in_file):
        """:returns: int the value of the text (includes the special numbers like START and END"""

        special_numbers = {"START": 0, "END": number_of_lines_in_file}

        if special_numbers.__contains__(text_value):
            text_value = special_numbers.get(text_value)

        return int(text_value)

    def get_lines(self, file_path):
        enter = """
"""
        file = open(file_path, "r")
        lines = get_items(file.read(), enter)
        file.close()
        return lines

    def run_code_writing(self):
        """Runs the writing of all the code"""

        start_time = time.time()
        self.previous_start_index = self.current_character_index
        self.previous_file_contents = self.current_file_contents

        while True:
            should_write_ch = time.time() - start_time >= self.time_needed_for_new_ch
            ch = self.all_code_needing_writing[self.current_character_index + 1]
            
            if should_write_ch and (ch == self.stop_ch or self.current_character_index >= len(self.all_code_needing_writing) - 1):
                self.continue_button.configure(bg=red)
                self.current_character_index += 1
                break

            if not self.valid_chs.__contains__(ch) and ch != self.stop_ch:
                self.current_character_index += 1
                continue



            elif should_write_ch:
                start_time = time.time()
                self.current_character_index += 1
                self.file.write(ch)
                self.file.flush()
                self.current_file_contents += ch


MainScreen()
WINDOW.mainloop()