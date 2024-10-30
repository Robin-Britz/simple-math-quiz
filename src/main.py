import random
import tkinter as tk
from tkinter import ttk

PINK = "#ffd1dc"

quiz = []

def math_quiz(multiplication_table):
    for num in range(1, 13):
        quiz.append(f"{num} x {multiplication_table} = ")

random.shuffle(quiz)

for question in quiz:
    print(question)

window = tk.Tk()
window.title("Math Quiz")
window.geometry("500x700")
window.config(pady=25, padx=25, bg=PINK)


lb_dropdown = ttk.Label(window, text="Time Table: ", font=("Robot", 10))
lb_dropdown.grid(column=0, row=1)

dropdown = tk.StringVar()

dd_dropdown = ttk.Combobox(window, width= 3, textvariable=dropdown)
dd_dropdown.config(values=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
dd_dropdown.grid(column=1, row=1)
dd_dropdown.current(0)

window.mainloop()
