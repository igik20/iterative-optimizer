"""
Minimal Iterative Optimizer by Yvette Dimitrova and Igor Trujnara. MIT licence.
"""

import customtkinter as ctk
import sys
import matplotlib
from optimizer import Optimizer
from search import Midpoint_Search
from golden_search import G_Search


class OutputWindow(ctk.CTk):
    """
    This class contains the output window, along with plotting options.
    """

    """
    Constructor, accepts data and creates GUI.
    """

    def __init__(self, data):
        # some sample calculation output, for testing only
        self.TESTDATA = {
            "func": "-x**2+4x+1",
            "varname": "x",
            "lower": 0,
            "upper": 3,
            "mode": "Equal Interval",
            "limittype": "Absolute Tolerance:",
            "limitval": 0.1,
            # check the values below once optimizer is implemented
            "optpos": 2.01,
            "optval": 4.991,
        }

        self.data = data
        self.generations = self.data["generations"]

        matplotlib.use("TkAgg")

        # font settings
        if sys.platform.startswith("linux"):
            self.fontname = "Ubuntu"
        elif sys.platform.startswith("win"):
            self.fontname = "Segoe UI"
        elif sys.platform.startswith("darwin"):
            self.fontname = "Trebuchet MS"
        else:
            self.fontname = "Arial"  # probably fails, I don't expect to get here anyway

        self.headerfont = ctk.CTkFont(self.fontname, 24)
        self.labelfont = ctk.CTkFont(self.fontname, 16)
        self.smallfont = ctk.CTkFont(self.fontname, 12)

        # GUI handling
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.geometry("600x600")
        self.title("MItO Output")
        self.minsize(300, 300)

        self.grid_columnconfigure((0, 1), weight=1)

        self.header = ctk.CTkLabel(
            master=self, text="MItO Results", font=self.headerfont
        )
        self.header.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.func_label = ctk.CTkLabel(
            master=self, text="Optimized the function", font=self.labelfont
        )
        self.func_label.grid(row=1, column=0, padx=20, pady=20)

        self.func_content = ctk.CTkLabel(
            master=self, text=self.data["func"], font=self.labelfont
        )
        self.func_content.grid(row=1, column=1, padx=20, pady=20)

        self.bounds_label = ctk.CTkLabel(
            master=self, text="on the interval", font=self.labelfont
        )
        self.bounds_label.grid(row=2, column=0, padx=20, pady=20)

        self.bounds_content = ctk.CTkLabel(
            master=self,
            text=f"{self.data['lower']} to {self.data['upper']}",
            font=self.labelfont,
        )
        self.bounds_content.grid(row=2, column=1, padx=20, pady=20)

        self.mode_label = ctk.CTkLabel(
            master=self, text="using the", font=self.labelfont
        )
        self.mode_label.grid(row=3, column=0, padx=20, pady=20)

        self.mode_content = ctk.CTkLabel(
            master=self, text=f"{self.data['mode']} algorithm", font=self.labelfont
        )
        self.mode_content.grid(row=3, column=1, padx=20, pady=20)

        self.limit_label = ctk.CTkLabel(
            master=self, text="limited by", font=self.labelfont
        )
        self.limit_label.grid(row=4, column=0, padx=20, pady=20)

        self.func_content = ctk.CTkLabel(
            master=self,
            text=f"{self.data['limittype']} {self.data['limitval']}",
            font=self.labelfont,
        )
        self.func_content.grid(row=4, column=1, padx=20, pady=20)

        self.func_label = ctk.CTkLabel(
            master=self,
            text=f"Found the {self.data['target'].lower()}:",
            font=self.labelfont,
        )
        self.func_label.grid(row=5, column=0, padx=20, pady=20)

        self.func_content = ctk.CTkLabel(
            master=self,
            text=f"{round(float(self.data['optval']), 3)} at {self.data['varname']} = {round(float(self.data['optpos']), 3)}",
            font=self.labelfont,
        )
        self.func_content.grid(row=5, column=1, padx=20, pady=20)

        self.genlist = [
            f"Generation {i}" for i in list(self.generations.keys())[:-1]
        ] + ["Final result"]

        self.gen_menu = ctk.CTkOptionMenu(master=self, values=self.genlist)
        self.gen_menu.grid(row=6, column=0, columnspan=2, padx=20, pady=20)

        self.submit = ctk.CTkButton(
            master=self, text="Plot", command=self.plot, width=120
        )
        self.submit.grid(row=7, column=0, columnspan=2)

    def plot(self):
        """
        Callback function for plotting the requested generation or final result.
        """
        genname = self.gen_menu.get()
        if self.data["mode"] == "Equal Interval":
            if genname.startswith("Gen"):
                gen = self.generations[int(genname.split()[-1])]
                Midpoint_Search.plot_generation(
                    self.data["exec"], gen[0], gen[1], gen[2]
                )
            else:
                Midpoint_Search.plot_result(
                    self.data["exec"],
                    self.data["lower"],
                    self.data["upper"],
                    self.data["optpos"],
                    self.data["optval"],
                )
        else:
            pass


class InputWindow(ctk.CTk):
    """
    This class contains all code for the input window and its errors.
    """

    """
    Constructor, mainly lots of GUI code.
    """

    def __init__(self):
        # data container for output
        self.data = {}

        # GUI handling
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        if sys.platform.startswith("linux"):
            self.fontname = "Ubuntu"
        elif sys.platform.startswith("win"):
            self.fontname = "Segoe UI"
        elif sys.platform.startswith("darwin"):
            self.fontname = "Trebuchet MS"
        else:
            self.fontname = "Arial"  # probably fails, I don't expect to get here anyway

        self.headerfont = ctk.CTkFont(self.fontname, 24)
        self.labelfont = ctk.CTkFont(self.fontname, 16)
        self.smallfont = ctk.CTkFont(self.fontname, 12)

        self.geometry("600x620")
        self.title("MItO Input")
        self.minsize(300, 300)

        self.grid_columnconfigure((0, 1), weight=1)

        self.header = ctk.CTkLabel(
            master=self, text="Mini Iterative Optimizer", font=self.headerfont
        )
        self.header.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.func_label = ctk.CTkLabel(
            master=self, text="Function:", font=self.labelfont
        )
        self.func_label.grid(row=1, column=0, padx=20, pady=20)

        self.func_input = ctk.CTkEntry(master=self, placeholder_text="Insert formula")
        self.func_input.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        self.var_label = ctk.CTkLabel(
            master=self, text="Variable name:", font=self.labelfont
        )
        self.var_label.grid(row=2, column=0, padx=20, pady=20)

        self.var_input = ctk.CTkEntry(master=self, placeholder_text="Insert letter")
        self.var_input.grid(row=2, column=1, padx=20, pady=20)

        self.lower_label = ctk.CTkLabel(
            master=self, text="Lower bound:", font=self.labelfont
        )
        self.lower_label.grid(row=3, column=0, padx=20, pady=20)

        self.lower_input = ctk.CTkEntry(master=self, placeholder_text="Insert number")
        self.lower_input.grid(row=3, column=1, padx=20, pady=20)

        self.upper_label = ctk.CTkLabel(
            master=self, text="Upper bound:", font=self.labelfont
        )
        self.upper_label.grid(row=4, column=0, padx=20, pady=20)

        self.upper_input = ctk.CTkEntry(master=self, placeholder_text="Insert number")
        self.upper_input.grid(row=4, column=1, padx=20, pady=20)

        self.mode_label = ctk.CTkLabel(
            master=self, text="Optimization algorithm:", font=self.labelfont
        )
        self.mode_label.grid(row=5, column=0, padx=20, pady=20)

        self.mode_list = ctk.CTkOptionMenu(
            master=self, values=["Equal Interval", "Golden Search"], font=self.smallfont
        )
        self.mode_list.grid(row=5, column=1, padx=20, pady=20)

        self.target_label = ctk.CTkLabel(
            master=self, text="Optimization target:", font=self.labelfont
        )
        self.target_label.grid(row=6, column=0, padx=20, pady=20)

        self.target_list = ctk.CTkOptionMenu(
            master=self, values=["Minimum", "Maximum"], font=self.smallfont
        )
        self.target_list.grid(row=6, column=1, padx=20, pady=20)

        self.limit_list = ctk.CTkOptionMenu(
            master=self,
            values=[
                "Absolute Tolerance:",
                "Relative Tolerance:",
                "Number of Iterations:",
            ],
            font=self.smallfont,
        )
        self.limit_list.grid(row=7, column=0, padx=20, pady=20, sticky="ew")

        self.limit_input = ctk.CTkEntry(master=self, placeholder_text="Insert number")
        self.limit_input.grid(row=7, column=1, padx=20, pady=20)

        self.submit = ctk.CTkButton(
            master=self, text="Calculate", command=self.submit_data
        )
        self.submit.grid(row=8, column=0, columnspan=2, padx=20, pady=20)

    """
    Function for displaying error messages.
    """

    def show_error(self, title, message):
        msgbox = ctk.CTkToplevel(self)
        msgbox.title(title)
        msgbox.geometry("400x150")
        msgbox.resizable(False, False)

        error_label = ctk.CTkLabel(master=msgbox, text=message, font=self.labelfont)
        error_label.pack(padx=20, pady=20)

        okay = ctk.CTkButton(
            master=msgbox, text="OK", font=self.labelfont, command=msgbox.withdraw
        )
        okay.pack(padx=20, pady=20)

    """
    Callback for the submit button. Validates and packages data.
    """

    def submit_data(self):
        # format validaton
        # function expression - string
        func = self.func_input.get()
        if func:
            self.data["func"] = func
        else:
            self.show_error("Input Error", "You must provide a function!")
            return

        # variable name - "char"
        var = self.var_input.get()
        if len(var) > 1:  # too long
            self.show_error("Input Error", "Variable name must be a single letter!")
            return
        elif len(var) > 0 and not var.isalpha():  # disallowed characters
            self.show_error("Input Error", "Variable name must be a letter!")
            return
        elif len(var) == 0:  # nothing provided, use default
            self.data["varname"] = "x"
        else:
            self.data["varname"] = var

        # lower limit - float
        lower = self.lower_input.get()
        try:
            lower = float(lower)
        except ValueError:
            self.show_error("Input Error", "Lower bound must be a number!")
            return
        self.data["lower"] = lower

        # upper limit - float
        upper = self.upper_input.get()
        try:
            upper = float(upper)
        except ValueError:
            self.show_error("Input Error", "Upper bound must be a number!")
            return
        self.data["upper"] = upper

        # optimization mode - from list
        self.data["mode"] = self.mode_list.get()

        # optimization target - from list
        self.data["target"] = self.target_list.get()

        # limit type - from list
        self.data["limittype"] = self.limit_list.get()[:-1]

        # limit value - int or float
        limit = self.limit_input.get()
        if self.data["limittype"] == "Number of Iterations:":
            try:
                limit = int(limit)
            except ValueError:
                self.show_error(
                    "Input Error", "Number of iterations must be an integer!"
                )
                return
        else:
            try:
                limit = float(limit)
            except ValueError:
                self.show_error("Input Error", "Tolerance must be a number!")
                return
        self.data["limitval"] = limit

        # value validation
        # upper bound is above lower bound
        if self.data["lower"] >= self.data["upper"]:
            self.show_error(
                "Value Error", "Upper bound must be greater than lower bound!"
            )
            return

        # relative tolerance must be between 0 and 1
        if self.data["limittype"] == "Relative Tolerance":
            if not 0 < self.data["limitval"] <= 1:
                self.show_error(
                    "Value Error", "Relative tolerance must be between 0 and 1!"
                )
                return

        # absolute tolerance must be positive
        if self.data["limittype"] == "Absolute Tolerance":
            if not self.data["limitval"] > 0:
                self.show_error("Value Error", "Absolute tolerance must be positive!")
                return

        # number of iterations must be positive
        if self.data["limittype"] == "Number of Iterations":
            if not self.data["limitval"] > 0:
                self.show_error("Value Error", "Number of iterations must be positive!")

        # debug only
        print(self.data)

        # further action
        # optimizer
        self.opt = Optimizer(self.data)
        self.res = self.opt.get()
        # output
        self.outwin = OutputWindow(self.res)
        self.outwin.mainloop()


class GUIRenderer:
    def __init__(self):
        self.inpwin = InputWindow()

    def run(self):
        self.inpwin.mainloop()
