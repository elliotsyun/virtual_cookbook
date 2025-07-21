from Constants import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import tkinter as tk


class AppHeader():

    # 'parent' is the Frame that the footer will be drawn on, while controller should always be AppController to allow for frame switching control
    def __init__(self, parent, controller):
        
        # ---------- CODE FOR HEADER ----------
        self.header = tk.Frame(parent, bg=HEADER_BACKGROUND_COLOR, width=WINDOW_WIDTH, height=HEADER_HEIGHT, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)
        self.header.grid(sticky="n")
        self.header.grid_propagate(False)
        self.controller = controller

        self.header_menu_image = Image.open(HEADER_MENU_ICON_PATH)
        self.header_menu_image = self.header_menu_image.resize(HEADER_MENU_BUTTON_SIZE, Image.LANCZOS)
        self.header_menu_image = ImageTk.PhotoImage(self.header_menu_image)        
        self.header_menu_button = tk.Button(self.header, image=self.header_menu_image, height=HEADER_HEIGHT, width=HEADER_ICON_WIDTH, command=lambda: self.controller.showFrame(1), bg=HEADER_BACKGROUND_COLOR, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        # NOTE: the logo image button is NOT shrunk to HEADER_ICON_WIDTH, as it is meant to be larger than the other 2 buttons
        self.header_logo_image = Image.open(HEADER_LOGO_ICON_PATH)
        self.header_logo_image = self.header_logo_image.resize(HEADER_LOGO_BUTTON_SIZE, Image.LANCZOS)
        self.header_logo_image = ImageTk.PhotoImage(self.header_logo_image)        
        self.header_logo_button = tk.Button(self.header, image=self.header_logo_image, height=HEADER_HEIGHT, command=lambda: self.controller.showFrame(1), bg=HEADER_BACKGROUND_COLOR, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)
        
        self.header_profile_image = Image.open(HEADER_PROFILE_ICON_PATH)
        self.header_profile_image = self.header_profile_image.resize(HEADER_PROFILE_BUTTON_SIZE, Image.LANCZOS)
        self.header_profile_image = ImageTk.PhotoImage(self.header_profile_image)        
        self.header_profile_button = tk.Button(self.header, image=self.header_profile_image, height=HEADER_HEIGHT, width=HEADER_ICON_WIDTH, command=lambda: self.controller.showFrame(1), bg=HEADER_BACKGROUND_COLOR, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        self.header_buttons = [self.header_menu_button, self.header_logo_button, self.header_profile_button]

        for column, button in enumerate(self.header_buttons):
            self.header.grid_columnconfigure(column, weight=2)
            button.grid(row=0, column=column, sticky="nsew", padx=HEADER_BUTTON_PADDING)     

