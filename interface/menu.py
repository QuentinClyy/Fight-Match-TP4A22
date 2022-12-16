from interface.texture_loader import MenuTextureLoader
from tkinter import Canvas, Button
import tkinter.font as font


class Menu(Canvas):

    def __init__(self, master):
        super().__init__(master)
        self.textures = MenuTextureLoader(self.master.width, self.master.height)

    def bg_init(self):
        self.create_image(0, 0, image=self.textures.menu_bg, anchor="nw")
        self.create_image(0, 0, image=self.textures.menu_left_char, anchor="nw")
        self.create_image(0, 0, image=self.textures.menu_right_char, anchor="nw")
        self.create_image(0, 0, image=self.textures.menu_title, anchor="nw")

    def create_menu_button(self, text, command):
        created_button = Button(self,
                                width=int(self.master.width // 2.4),
                                height=int(self.master.height // 5),
                                borderwidth=0,
                                bg='#4d330f', activebackground='#4d330f',
                                fg='#ad2513', activeforeground='#63170d',
                                command=command)
        created_button.config(image=self.textures.button_panel, text=text, compound="center")
        button_font = font.Font(family='Roman', size=50)
        created_button['font'] = button_font
        return created_button

    def create_back_button(self, text, textures):
        created_button = Button(self,
                                height=50,
                                width=50,
                                borderwidth=0,
                                bg='#4d330f', activebackground='#4d330f',
                                fg='#ad2513', activeforeground='#63170d')
        created_button.config(image=textures.small_button_panel, text=text, compound="center")
        button_font = font.Font(family='Roman', size=10, weight='bold')
        created_button['font'] = button_font
        return created_button

    def create_player_button(self, text, command):
        created_button = Button(self, text=text,
                                width=int(self.master.width // 4.7),
                                height=int(self.master.height // 5.6),
                                borderwidth=0,
                                bg='#4d330f', activebackground='#4d330f',
                                fg='#ad2513', activeforeground='#63170d',
                                command=command)
        created_button.config(image=self.textures.mid_button_panel, text=text, compound="center")
        button_font = font.Font(family='Roman', size=30, weight='bold')
        created_button['font'] = button_font
        return created_button
