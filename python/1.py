import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.current_value = tk.StringVar(value="0")

        self.create_display()
        self.create_buttons()

    def create_display(self):
        display = tk.Entry(self.root, textvariable=self.current_value,
                           font=("Arial", 18), justify="right")
        display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(
                self.root,
                text=text,
                font=("Arial", 14),
                width=5,
                height=2,
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, padx=2, pady=2)

    def on_button_click(self, value):
        if value == 'C':
            self.current_value.set("0")
        elif value == '=':
            try:
                result = eval(self.current_value.get())
                self.current_value.set(str(result))
            except:
                self.current_value.set("Error")
        else:
            current = self.current_value.get()
            if current == "0" or current == "Error":
                self.current_value.set(value)
            else:
                self.current_value.set(current + value)


root = tk.Tk()
root.title("Калькулятор")
calculator = Calculator(root)
root.mainloop()