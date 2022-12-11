import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk


class MenuTextureLoader:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.menu_bg = resize_image("background.png", self.width, self.height)
        self.menu_left_char = resize_image("leftWarrior.png", self.width, self.height)
        self.menu_right_char = resize_image("rightWarrior.png", self.width, self.height)
        self.menu_title = resize_image("titleSecond.png", self.width, self.height)
        self.button_panel = resize_image("Panel.png", int(self.width/2.367), int(self.height/5))


def create_menu_button(master, text, width, height, textures):
    created_button = tk.Button(master,
                               height=int(height / 5),
                               width=int(width / 2.4),
                               borderwidth=0,
                               bg='#4d330f', activebackground='#4d330f',
                               fg='#ad2513', activeforeground='#63170d')
    created_button.config(image=textures.button_panel, text=text, compound="center")
    button_font = font.Font(family='Roman', size=50, weight='bold')
    created_button['font'] = button_font
    created_button.pack(padx=10, pady=10)
    return created_button


def resize_image(img_name, width, height):
    load_img = Image.open(f"./Images/{img_name}")
    res_img = load_img.resize((int(width), int(height)), resample=Image.NEAREST)
    return ImageTk.PhotoImage(res_img)