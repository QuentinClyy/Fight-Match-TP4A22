from tkinter import *
from PIL import Image, ImageTk


class MainMenu:

    def __init__(self, master, width, height):

        self.master = master
        self.width = width
        self.height = height

        self.loadbg = Image.open("./Images/background.png")
        self.resbg = self.loadbg.resize((self.width, self.height))
        self.bg = ImageTk.PhotoImage(self.resbg)

        self.canvas1 = Canvas(self.master, width=self.width,
                              height=self.height)

        self.launch = Button(self.master, text="Play")
        self.options = Button(self.master, text="Options")
        self.quit = Button(self.master, text="Quit", command=self.master.quit)

        self.launch_canvas = self.canvas1.create_window(100, 10,
                                                        anchor="nw",
                                                        window=self.launch)
        self.options_canvas = self.canvas1.create_window(100, 40,
                                                         anchor="nw",
                                                         window=self.options)
        self.quit_canvas = self.canvas1.create_window(100, 70,
                                                      anchor="nw",
                                                      window=self.quit)

    def create_background(self):

        self.canvas1.pack(fill="both", expand=True)

        self.canvas1.create_image(0, 0, image=self.bg,
                                  anchor="nw")
