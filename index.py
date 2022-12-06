from tkinter import *
from PIL import Image, ImageTk


def resize_image(img_name, width, height):
    load_img = Image.open(f"./Images/{img_name}")
    res_img = load_img.resize((width, height))
    return ImageTk.PhotoImage(res_img)


class MainMenu:

    def __init__(self, master, width, height):
        self.master = master
        self.width = width
        self.height = height

        self.bg = resize_image("background.png", self.width, self.height)

        self.lc = resize_image("leftWarrior.png", self.width, self.height)

        self.rc = resize_image("rightWarrior.png", self.width, self.height)

        self.title_img = resize_image("titleSecond.png", self.width, self.height)

        self.canvas1 = Canvas(self.master, width=self.width,
                              height=self.height)
        self.canvas1.pack(fill="both", expand=True)

        #creating buttons
        self.panel = PhotoImage(file="./Images/Panel.png")

        self.launch = Button(self.master, text="Play",
                             height=int(self.height/5),
                             width=int(self.width/2.4))
        self.launch.config(image=self.panel)

        self.options = Button(self.master, text="Options",
                              height=int(self.height/7),
                              width=int(self.width/3))
        self.options.config(image=self.panel)

        self.quit = Button(self.master, text="Quit", command=self.master.quit,
                           height=int(self.height/7),
                           width=int(self.width/3))
        self.quit.config(image=self.panel)

    def main_menu_init(self):
        #load background
        self.canvas1.create_image(0, 0, image=self.bg,
                                  anchor="nw")
        #load characters
        self.canvas1.create_image(0, 0,  image=self.lc,
                                  anchor="nw")
        self.canvas1.create_image(0, 0, image=self.rc,
                                  anchor="nw")
        #load title
        self.canvas1.create_image(0, 0, image=self.title_img,
                                  anchor="nw")
        #display buttons
        self.canvas1.create_window((self.width/2),
                                   (self.height-self.height/2),
                                   anchor="center",
                                   window=self.launch)
        self.canvas1.create_window((self.width/2),
                                   (self.height-2*(self.height/6.75)),
                                   anchor="center",
                                   window=self.options)
        self.canvas1.create_window((self.width/2),
                                   (self.height-self.height/8),
                                   anchor="center",
                                   window=self.quit)
