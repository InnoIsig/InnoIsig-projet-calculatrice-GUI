import tkinter as tk

# TODO 1 : ici c'est une classe qui doit permettre d'initialiser la fenetre window
WHITE = "#000080"
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
LIGHT_GRAY = "#F5F5F5"
RED = "#800000"
BLACK = "#000000"
GREEN = "#008000"
LABEL_COLOR = "#25265E"
LABEL_COLOR1 = "#FFFFFF"
DEFAULT_FONT_STYLE = ("Arial", 20)
OFF_WHITE = "#F8FAFF"
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculatrice")
        self.total_expression = ""
        self.current_expression = ""

        # TODO 2 : Ici je cree le frame
        self.display_frame = self.creat_display_frame()
        self.total_label, self.label = self.creat_display_label()

        # TODO 4 : Je cree un dictionnaire qui doit prendre en compte touts les bouttons
        self.digits = {
            7:(1, 1), 8:(1, 2), 9:(1, 3),
            4:(2, 1), 5:(2, 2), 6:(2, 3),
            1:(3, 1), 2:(3, 2), 3:(3, 3),
            0:(4, 1), '.':(4, 2),
        }
        # TODO 5 : Dictionnaire des operations
        self.operations = {
            "/":"\u00F7", "*":"\u00D7", "-":"-", "+":"+"
        }
        self.button_frame = self.creat_button_frame()
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)
        self.creat_digit_button()
        self.creat_operations_buttons()
        self.creat_special_button()
        self.bind_keys()

    # TODO 3 : Ici j'ajoute les labeles

    def bind_keys(self):
        self.window.bind("<Return>", lambda event:self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda  vent, digit=key:self.add_to_express(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key:self.append_operator(operator))



    def creat_special_button(self):
        self.creat_clear_button()
        self.creat_equals_button()
        self.creat_square_button()
        self.creat_sqrt_button()

    def creat_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")

        return total_label, label

    def creat_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_express(self, value):
        self.current_expression += str(value)
        self.update_label()

    def creat_digit_button(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR1, font=DIGIT_FONT_STYLE,
                               command=lambda x=digit: self.add_to_express(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()



    def creat_button_frame(self):
        button = tk.Frame(self.window)
        button.pack(expand=True, fill="both")
        return button
    def creat_operations_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=symbol, bg=WHITE, fg=LABEL_COLOR1, font=DEFAULT_FONT_STYLE,
                               command=lambda x=operator:self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_label()
        self.update_label()

    def creat_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=RED, fg=LABEL_COLOR1, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval((f"{self.current_expression}**2")))
        self.update_label()

    def creat_square_button(self):
        button = tk.Button(self.button_frame, text="x\u00b2", bg=WHITE, fg=LABEL_COLOR1, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval((f"{self.current_expression}**0.5")))
        self.update_label()

    def creat_sqrt_button(self):
        button = tk.Button(self.button_frame, text="\u221ax", bg=WHITE, fg=LABEL_COLOR1, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression= "Erreur"
        finally:
            self.update_label()

    def creat_equals_button(self):
        button = tk.Button(self.button_frame, text="=", bg=GREEN, fg=LABEL_COLOR1, font=DEFAULT_FONT_STYLE,
                           command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()




