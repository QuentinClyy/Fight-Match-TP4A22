from tkinter import *
from PIL import Image, ImageTk


def resize_image(img, width, height):
    load_img = Image.open(f"./Images/{img}")
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

        self.launch = Button(self.master, text="Play")
        self.options = Button(self.master, text="Options")
        self.quit = Button(self.master, text="Quit", command=self.master.quit)

        self.launch_canvas = self.canvas1.create_window((self.width/2),
                                                        (self.height-self.height/2),
                                                        anchor="center",
                                                        window=self.launch)
        self.options_canvas = self.canvas1.create_window((self.width/2),
                                                         (self.height-2*(self.height/7)),
                                                         anchor="center",
                                                         window=self.options)
        self.quit_canvas = self.canvas1.create_window((self.width/2),
                                                      (self.height-self.height/8),
                                                      anchor="center",
                                                      window=self.quit)

    def create_background(self):

        self.canvas1.create_image(0, 0, image=self.bg,
                                  anchor="nw")

    def load_characters(self):

        self.canvas1.create_image(0, 0,  image=self.lc,
                                  anchor="nw")
        self.canvas1.create_image(0, 0, image=self.rc,
                                  anchor="nw")

    def load_title(self):

        self.canvas1.create_image(0, 0, image=self.title_img,
                                  anchor="nw")
