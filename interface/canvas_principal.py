from tkinter import Canvas
from interface.texture_loader import GameTextureLoader
from interface.canvas_arene import CanvasArene


class CanvasPrincipal(Canvas):
    def __init__(self, master):
        self.master = master
        self.width = self.master.width
        self.height = self.master.height
        super().__init__(master,  width=self.width,
                         height=self.height,
                         borderwidth=0, highlightthickness=0)

        self.textures = GameTextureLoader(self.width, self.height)
        self.create_image(0, 0, image=self.textures.arene_bg, anchor="nw")

        self.canvas_arene = CanvasArene(self.master, self.master.arene)
        self.create_window(self.width // 2,
                           self.height // 2 + self.height // 34.6,
                           anchor="center", window=self.canvas_arene)
