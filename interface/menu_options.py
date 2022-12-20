from tkinter import Frame, Scale, Label
from interface.menu import Menu


class FrameOptions(Frame):
    def __init__(self, master):
        super().__init__(master, background='#d8c0a5', highlightthickness=4, highlightbackground='#664524')

        self.scale_volume = Scale(self, from_=0, to=50, label="Music volume",
                                  orient="horizontal", width=20,
                                  relief="ridge", length=300,
                                  background='#d8c0a5', activebackground='#d8c0a5',
                                  command=self.master.change_volume)
        self.scale_volume.set(50)
        self.scale_volume.grid(row=0)

        self.label_credit = Label(self, text="Credits : MASK OFF (Bardcore Version) - Beedle The Bardcore",
                                  background='#d8c0a5')
        self.label_credit.grid(row=1)

        self.scale_useless = Scale(self, from_=0, to=9000, label="Useless Setting",
                                   orient="horizontal", width=20,
                                   relief="ridge", length=300,
                                   background='#d8c0a5', activebackground='#d8c0a5',
                                   command=self.populer)
        self.scale_useless.grid(row=2)

        self.label_useless = Label(self, text="You can play with the slider, it won't change anything \n"
                                              "I swear !",
                                   background='#d8c0a5')
        self.label_over_9000 = Label(self, text='',
                                     background='#d8c0a5')
        self.label_useless.grid(row=3)
        self.label_over_9000.grid(row=4)

    def populer(self, valeur):
        if int(valeur) in range(8500, 9000):
            self.label_over_9000.config(text="It can't go over 9000, Vegeta, just stop it")
        # See ? it doesn't do anything



class MenuOptions(Menu):
    def __init__(self, master):
        super().__init__(master)
        self.frame_options = FrameOptions(self)

        self.back_button = self.create_back_button("Back", self.textures)
        self.back_button.config(command=lambda: self.master.switch_menu_canvas("MainMenu"))

        self.bg_init()

        self.create_window(self.master.width // 2,
                           self.master.height // 2,
                           anchor="center",
                           window=self.frame_options)

        self.create_window((self.master.width - self.master.width // 38.4),
                           (self.master.height - self.master.height // 21.6),
                           anchor="se",
                           window=self.back_button)

    def change_volume(self, volume):
        self.master.music_player.player.set_volume(float(volume) / float(100))
