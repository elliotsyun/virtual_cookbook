from Constants import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import tkinter as tk

class AppFooter():

    # 'parent' is the Frame that the footer will be drawn on, while controller should always be AppController to allow for frame switching control
    def __init__(self, parent, controller):
        
        # ---------- CODE FOR FOOTER ----------
        self.footer = tk.Frame(parent, bg=FOOTER_BACKGROUND_COLOR, width=WINDOW_WIDTH, height=WINDOW_FOOTER_HEIGHT, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)
        self.footer.grid(sticky="ew")
        self.footer.grid_propagate(False)
        self.controller = controller

        self.home_button_image = Image.open(HOME_ICON_PATH)
        self.home_button_image = self.home_button_image.resize(FOOTER_HOME_BUTTON_SIZE, Image.LANCZOS)
        self.home_button_image = ImageTk.PhotoImage(self.home_button_image)        
        self.home_button = tk.Button(self.footer, image=self.home_button_image, height=WINDOW_FOOTER_HEIGHT, width=FOOTER_ICON_WIDTH, command=lambda: self.controller.showFrame(1), bg=FOOTER_BACKGROUND_COLOR, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        self.recipes_button_image = Image.open(RECIPES_ICON_PATH)
        self.recipes_button_image = self.recipes_button_image.resize(FOOTER_RECIPES_BUTTON_SIZE, Image.LANCZOS)
        self.recipes_button_image = ImageTk.PhotoImage(self.recipes_button_image)
        self.recipes_button = tk.Button(self.footer, image=self.recipes_button_image, height=WINDOW_FOOTER_HEIGHT, width=FOOTER_ICON_WIDTH, command=lambda: self.controller.showFrame(2), bg=FOOTER_BACKGROUND_COLOR, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        self.add_recipe_button_image = Image.open(ADD_RECIPE_ICON_PATH)
        self.add_recipe_button_image = self.add_recipe_button_image.resize(FOOTER_ADD_BUTTON_SIZE, Image.LANCZOS)
        self.add_recipe_button_image = ImageTk.PhotoImage(self.add_recipe_button_image)
        self.add_recipe_button = tk.Button(self.footer, image=self.add_recipe_button_image, height=WINDOW_FOOTER_HEIGHT, command=lambda: self.controller.showFrame(2), bg=FOOTER_BACKGROUND_COLOR, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        self.discover_button_image = Image.open(DISCOVER_ICON_PATH)
        self.discover_button_image = self.discover_button_image.resize(FOOTER_DISCOVER_BUTTON_SIZE, Image.LANCZOS)
        self.discover_button_image = ImageTk.PhotoImage(self.discover_button_image)        
        self.discover_button = tk.Button(self.footer, image=self.discover_button_image, height=WINDOW_FOOTER_HEIGHT, width=FOOTER_ICON_WIDTH, command=lambda: self.controller.showFrame(2), bg=FOOTER_BACKGROUND_COLOR, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        self.category_button_image = Image.open(CATEGORY_ICON_PATH)
        self.category_button_image = self.category_button_image.resize(FOOTER_CATEGORY_BUTTON_SIZE, Image.LANCZOS)
        self.category_button_image = ImageTk.PhotoImage(self.category_button_image)            
        self.category_button = tk.Button(self.footer, image=self.category_button_image, height=WINDOW_FOOTER_HEIGHT, width=FOOTER_ICON_WIDTH, command=lambda: self.controller.showFrame(2), bg=FOOTER_BACKGROUND_COLOR, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        self.footer_buttons = [self.home_button, self.recipes_button, self.add_recipe_button, self.discover_button, self.category_button]

        for column, button in enumerate(self.footer_buttons):
            self.footer.grid_columnconfigure(column, weight=1)
            button.grid(row=0, column=column, sticky="nsew", padx=FOOTER_BUTTON_PADDING)     

 
