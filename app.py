import tkinter as tk
from controller import SpotifyController
from model import SpotifyModel
from view import SpotifyView

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.model = SpotifyModel()
        self.view = SpotifyView(self.root)
        self.controller = SpotifyController(self.model, self.view)

    def run(self):
        self.root.mainloop()


# Entry point to run the app
def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()