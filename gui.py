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
        self.header.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 20)

        self.func_label = ctk.CTkLabel(master=self, text="Function:",font=("Ubuntu", 16))
        self.func_label.grid(row = 1, column = 0, padx = 20, pady = 20)

        self.func_input = ctk.CTkEntry(master=self, placeholder_text="Insert formula")
        self.func_input.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = "ew")



class GUIRenderer():
    def __init__(self):
        self.inpwin = InputWindow()


    def run(self):
        self.inpwin.mainloop()
