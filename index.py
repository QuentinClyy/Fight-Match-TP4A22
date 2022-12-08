from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk


def resize_image(img_name, width, height):
    load_img = Image.open(f"./Images/{img_name}")
    res_img = load_img.resize((int(width), int(height)), resample=Image.NEAREST)
    return ImageTk.PhotoImage(res_img)


class MenuTextureLoader:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.menu_bg = resize_image("background.png", self.width, self.height)
        self.menu_left_char = resize_image("leftWarrior.png", self.width, self.height)
        self.menu_right_char = resize_image("rightWarrior.png", self.width, self.height)
        self.menu_title = resize_image("titleSecond.png", self.width, self.height)
        self.button_panel = PhotoImage(file="./Images/Panel.png")


class BaseMenu:

    def __init__(self, master, width, height):
        self.master = master
        self.width = width
        self.height = height
        self.textures = MenuTextureLoader(self.width, self.height)

        # creating canvases
        self.main_canvas = Canvas(self.master, width=self.width, height=self.height)
        self.main_canvas = Canvas(self.master, width=self.width, height=self.height)
        self.nb_players_canvas = Canvas(self.master, width=self.width, height=self.height)
        self.nb_dice_canvas = Canvas(self.master, width=self.width, height=self.height)

    def create_menu_button(self, text):
        created_button = Button(self.master,
                                height=int(self.height / 5),
                                width=int(self.width / 2.4),
                                borderwidth=0,
                                bg='#4d330f', activebackground='#4d330f',
                                fg='#ad2513', activeforeground='#63170d')
        created_button.config(image=self.textures.button_panel, text=text, compound="center")
        button_font = font.Font(family='Roman', size=50, weight='bold')
        created_button['font'] = button_font
        created_button.pack(padx=10, pady=10)
        return created_button


class MainMenu(BaseMenu):

    def __init__(self, master, width, height):
        BaseMenu.__init__(self, master, width, height)
        # creating buttons
        self.launch_button = self.create_menu_button("Play")
        self.launch_button.config(command=self.play_command)

        self.options_button = self.create_menu_button("Options")

        self.quit_button = self.create_menu_button("Quit")
        self.quit_button.config(command=self.master.quit)

    def main_menu_init(self):
        self.main_canvas.create_image(0, 0, image=self.textures.menu_bg, anchor="nw")
        self.main_canvas.create_image(0, 0, image=self.textures.menu_left_char, anchor="nw")
        self.main_canvas.create_image(0, 0, image=self.textures.menu_right_char, anchor="nw")
        self.main_canvas.create_image(0, 0, image=self.textures.menu_title, anchor="nw")

        self.main_canvas.create_window((self.width/2),
                                       (self.height - self.height / 1.75),
                                       anchor="center",
                                       window=self.launch_button)
        self.main_canvas.create_window((self.width/2),
                                       (self.height - (self.height / 2.8)),
                                       anchor="center",
                                       window=self.options_button)
        self.main_canvas.create_window((self.width/2),
                                       (self.height - (self.height / 7)),
                                       anchor="center",
                                       window=self.quit_button)
        self.main_canvas.pack(fill="both", expand=True)

    def play_command(self):
        self.main_canvas.delete("all")
        arena_sm = ArenaSizeMenu(self.master, self.width, self.height)
        arena_sm.arena_size_menu_init()


class ArenaSizeMenu(BaseMenu):

    def __init__(self, master, width, height):
        BaseMenu.__init__(self, master, width, height)

    def arena_size_menu_init(self):
        self.main_canvas.create_image(0, 0, image=self.textures.menu_bg, anchor="nw")
        self.main_canvas.create_image(0, 0, image=self.textures.menu_left_char, anchor="nw")
        self.main_canvas.create_image(0, 0, image=self.textures.menu_right_char, anchor="nw")
        self.main_canvas.create_image(0, 0, image=self.textures.menu_title, anchor="nw")
        self.main_canvas.pack(fill="both", expand=True)
