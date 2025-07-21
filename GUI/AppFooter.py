from Constants import *
from tkinter import PhotoImage
import tkinter as tk

class AppFooter():

    # 'parent' is the Frame that the footer will be drawn on, while controller should always be AppController to allow for frame switching control
    def __init__(self, parent, controller):
        
        # ---------- CODE FOR FOOTER ----------
        self.footer = tk.Frame(parent, bg="gray", width=WINDOW_WIDTH, height=WINDOW_FOOTER_HEIGHT, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)
        self.footer.grid(sticky="ew")
        self.footer.grid_propagate(False)

        self.controller = controller

        self.home_button_image = PhotoImage(file=HOME_ICON_PATH)
        self.home_button = tk.Button(self.footer, image=self.home_button_image, height=WINDOW_FOOTER_HEIGHT, width=FOOTER_ICON_WIDTH, command=lambda: self.controller.showFrame(1), bg="gray", bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        self.recipes_button_image = PhotoImage(file=RECIPES_ICON_PATH)
        self.recipes_button = tk.Button(self.footer, image=self.recipes_button_image, height=WINDOW_FOOTER_HEIGHT, width=FOOTER_ICON_WIDTH, command=lambda: self.controller.showFrame(2), bg="gray", bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        # NOTE: the add recipe button is NOT shrunk to FOOTER_ICON_WIDTH, as it is meant to be larger than the other 4 buttons
        self.add_recipe_button_image = PhotoImage(file=ADD_RECIPE_ICON_PATH)
        self.add_recipe_button = tk.Button(self.footer, image=self.add_recipe_button_image, height=WINDOW_FOOTER_HEIGHT, command=lambda: self.controller.showFrame(2), bg="gray", bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        self.discover_button_image = PhotoImage(file=DISCOVER_ICON_PATH)
        self.discover_button = tk.Button(self.footer, image=self.discover_button_image, height=WINDOW_FOOTER_HEIGHT, width=FOOTER_ICON_WIDTH, command=lambda: self.controller.showFrame(2), bg="gray", bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        self.category_button_image = PhotoImage(file=CATEGORY_ICON_PATH)
        self.category_button = tk.Button(self.footer, image=self.category_button_image, height=WINDOW_FOOTER_HEIGHT, width=FOOTER_ICON_WIDTH, command=lambda: self.controller.showFrame(2), bg="gray", bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)

        self.footer_buttons = [self.home_button, self.recipes_button, self.add_recipe_button, self.discover_button, self.category_button]

        for column, button in enumerate(self.footer_buttons):
            self.footer.grid_columnconfigure(column, weight=1)
            button.grid(row=0, column=column, sticky="nsew", padx=FOOTER_BUTTON_PADDING)     
 
