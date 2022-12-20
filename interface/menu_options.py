from interface.menu import Menu


class MenuOptions(Menu):
    def __init__(self, master):
        super().__init__(master)
        self.frame_options = FrameOptions(master)

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
