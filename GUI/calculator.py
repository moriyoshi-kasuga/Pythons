import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def remove_char():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.title("電卓")
root.geometry("300x220")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)


def set_button(text: str, command, row: int, column: int):
    button = tk.Button(root, text=text, command=command, width=5, font=("Arial", 14))
    button.grid(row=row, column=column)


set_button("1", lambda: add_to_calculation(1), 3, 1)
set_button("2", lambda: add_to_calculation(2), 3, 2)
set_button("3", lambda: add_to_calculation(3), 3, 3)
set_button("4", lambda: add_to_calculation(4), 4, 1)
set_button("5", lambda: add_to_calculation(5), 4, 2)
set_button("6", lambda: add_to_calculation(6), 4, 3)
set_button("7", lambda: add_to_calculation(7), 5, 1)
set_button("8", lambda: add_to_calculation(8), 5, 2)
set_button("9", lambda: add_to_calculation(9), 5, 3)
set_button("0", lambda: add_to_calculation(0), 6, 1)

set_button("+", lambda: add_to_calculation("+"), 6, 4)
set_button("-", lambda: add_to_calculation("-"), 5, 4)
set_button("*", lambda: add_to_calculation("*"), 4, 4)
set_button("/", lambda: add_to_calculation("/"), 3, 4)
set_button("(", lambda: add_to_calculation("("), 2, 1)
set_button(")", lambda: add_to_calculation(")"), 2, 2)
set_button("%", lambda: add_to_calculation("%"), 2, 3)
set_button(".", lambda: add_to_calculation("."), 6, 2)

set_button("=", evaluate_calculation, 6, 3)
set_button("CE", remove_char, 2, 4)

root.mainloop()
