import tkinter as tk
from tkinter import messagebox

def display_matrix(matrix):
    matrix_str = ""
    for i in range(3):
        matrix_str += "[ "
        for j in range(4):
            if j == 3:
                matrix_str += "| "
            matrix_str += "{:>6.2f} ".format(matrix[i][j])  # Adjusted format for larger matrix
        matrix_str += "]\n"
    return matrix_str

def gje(matrix):
    m21 = matrix[1][0] / matrix[0][0]
    m31 = matrix[2][0] / matrix[0][0]

    # Rule E2-(m21)E1 = E2
    for j in range(4):
        matrix[1][j] -= m21 * matrix[0][j]

    # Rule E3-(m31)E1 = E3
    for j in range(4):
        matrix[2][j] -= m31 * matrix[0][j]

    m32 = matrix[2][1] / matrix[1][1]

    # Rule E3-(m32)E2 = E3
    for j in range(4):
        matrix[2][j] -= m32 * matrix[1][j]

    x3 = matrix[2][3] / matrix[2][2]
    x2 = (matrix[1][3] - (matrix[1][2] * x3)) / matrix[1][1]
    x1 = (matrix[0][3] - ((matrix[0][1] * x2) + (matrix[0][2] * x3))) / matrix[0][0]

    return x1, x2, x3

def calculate():
    matrix = []
    try:
        for i in range(3):
            row = []
            for j in range(4):
                entry = float(entries[i][j].get())
                row.append(entry)
            matrix.append(row)

        result_label.config(text="Original Matrix:\n" + display_matrix(matrix), fg="#FFFFFF", bg="#00224D")

        x1, x2, x3 = gje(matrix)
        result_label.config(text=result_label.cget("text") + "\nAfter Gauss Elimination:\n" + display_matrix(matrix), fg="#FFFFFF", bg="#00224D")
        result_label.config(text=result_label.cget("text") + f"\n\nSolution:\nX1 = {x1:.2f}\nX2 = {x2:.2f}\nX3 = {x3:.2f}", fg="#FFFFFF", bg="#00224D")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all fields.")
# gui
def create_entry_widgets():
    entry_frame = tk.Frame(root, bg="#00224D")
    entry_frame.pack(pady=10)

    for i in range(3):
        for j in range(4):
            entry = tk.Entry(entry_frame, width=8, font=('Arial', 12))
            entry.grid(row=i, column=j, padx=5, pady=5)
            entries[i].append(entry)

root = tk.Tk()
root.title("Gauss Elimination Calculator")
root.geometry("1500x900")
root.configure(bg="#00224D")  # Set background color of the window

entries = [[] for _ in range(3)]

# Title label
title_label = tk.Label(root, text="Gauss Elimination Calculator", font=("Helvetica", 20, "bold"), fg="#00224D", bg="#FF3EA5")
title_label.pack(pady=(50, 10))  # Sticky "ew" to fill horizontally

# Input matrix label
input_label = tk.Label(root, text="Enter Matrix", font=('Arial', 14, 'bold'), fg="#FFFFFF", bg="#00224D")
input_label.pack()

create_entry_widgets()

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=('Arial', 12), bg="#FF3EA5", fg="#00224D")
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 12), bg="#00224D", justify="left", anchor="w", padx=10)
result_label.pack(pady=10)

root.mainloop()
