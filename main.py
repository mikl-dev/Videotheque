import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x400")
        self.creer_widgets()

    def creer_widgets(self):
        self.label = tk.Label(self, text="J'adore Python !")
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.label.pack()
        self.bouton.place (x=730, y=350)    
        





if __name__ == "__main__":
    app = Application()
    app.title("Videothèque")
    app.mainloop()
    