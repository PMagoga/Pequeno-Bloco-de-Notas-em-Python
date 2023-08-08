import tkinter

class App:

    def __init__(self):

        self.window = tkinter.Tk()
        self.window.title("Marcador")
        self.window.minsize(width=360, height=640)
        self.window.maxsize(width=360, height=640)

        self.text = tkinter.Label(self.window, text="20", font="Arial 80 bold", pady=50)
        self.text.pack()

        self.frame = tkinter.Frame(self.window, bg="white")
        self.frame.pack()

        self.button_plus = tkinter.Button(self.frame, text="Up", bg="orange", width=20)
        self.button_plus.pack(side="left")

        self.button_down = tkinter.Button(self.frame, text="Down", bg="red", width=20)
        self.button_down.pack(side="left")

        self.window.mainloop()


App()

