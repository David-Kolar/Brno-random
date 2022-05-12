import tkinter as tk

class Game:
    def __init__(self):
        leva_palka = Palka(screen_width//6)
        prava_palka = Palka(5*screen_width//6)
        micek = Micek(100, 100)
        self.time = 10
    def play(self):
        pass

class HerniObjekt():
    def __init__(self, x, y, height, width,  name="Pong"):
        self.x_velocity = 10
        self.y_velocity = 10
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.window = tk.Toplevel()
        self.window.title(name)
        self.window.geometry(f"{self.height}x{self.width}+{self.x}+{self.y}")
    def move(self):
        pass
class Palka(HerniObjekt):
    def __init__(self, x):
        self.width = 400
        self.height = 100
        self.y = screen_width // 5
        self.x = x
        super().__init__(self.x, self.y, self.height, self.width,  "Palka")

class Micek(HerniObjekt):
    def __init__(self, x, y):
        self.width = 10
        self.height = 10
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, self.height, self.width,  "Micek")


root = tk.Tk()
root.title("Pong")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
button = tk.Button(root, text="Start Game", command=Game)
button.pack()
root.mainloop()