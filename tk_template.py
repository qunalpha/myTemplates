from tkinter import *
from tkinter  import messagebox

class App(Tk):
    def __init__(self, width: int = 480, height: int = 360, title: str = "CTK Window", iconpath: str = None, fullscreen: bool = False, close_confirmation: bool = False):
        super().__init__()

        self._width = width
        self._height = height
        self._title = title
        self._iconpath = iconpath

        self._fullscreen = fullscreen
        self._close_confirmation = close_confirmation

        self.geometry(f"{self._width}x{self._height}")
        self.minsize(self._width, self._height)

        if self._iconpath:
            self.iconbitmap(self._iconpath)

        self.title(self._title)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.attributes("-fullscreen", self._fullscreen)

        self.bind("<Escape>", self.exit_fullscreen)
        self.bind("<F11>", self.enter_fullscreen)

    def enter_fullscreen(self, event=None):
        self.attributes("-fullscreen", True)

    def exit_fullscreen(self, event=None):
        self.attributes("-fullscreen", False)

    def on_closing(self):
        # Prompt the user for confirmation
        if self._close_confirmation and messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
        else:
            self.destroy()

if __name__ == "__main__":
    App().mainloop()