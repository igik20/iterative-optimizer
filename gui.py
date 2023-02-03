import customtkinter as ctk


class InputWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.geometry("600x800")
        self.title("MItO Input")
        self.minsize(300, 400)

        self.grid_columnconfigure((0, 1), weight = 1)

        self.header = ctk.CTkLabel(master=self, text="Minimal Iterative Optimizer", font=("Ubuntu", 24))
        self.header.grid(row = 0, column = 0, columnspan = 2)



class GUIRenderer():
    def __init__(self):
        self.inpwin = InputWindow()


    def run(self):
        self.inpwin.mainloop()
