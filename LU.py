import tkinter as tk
from tkinter import messagebox

def display_matrix(matrix):
    matrix_str = ""
    for i in range(len(matrix)):
        matrix_str += "[ "
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                matrix_str += "| "
            matrix_str += "{:>6.2f} ".format(matrix[i][j])
        matrix_str += "]\n"
    return matrix_str

def lu_decomposition(matrix):
    n = len(matrix)
    lower = [[0.0] * n for _ in range(n)]
    upper = [[0.0] * n for _ in range(n)]

    for i in range(n):
        lower[i][i] = 1.0

    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += (lower[i][k] * upper[k][j])
            upper[i][j] = matrix[i][j] - sum

        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += (lower[j][k] * upper[k][i])
            lower[j][i] = (matrix[j][i] - sum) / upper[i][i]

    return lower, upper

def forward_substitution(lower, b):
    n = len(lower)
    y = [0.0] * n
    for i in range(n):#lc=b
        y[i] = b[i] - sum(lower[i][j] * y[j] for j in range(i))
    return y

def backward_substitution(upper, y):
    n = len(upper)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):#ux=c     range(start, stop, step)
        x[i] = (y[i] - sum(upper[i][j] * x[j] for j in range(i + 1, n))) / upper[i][i]
    return x

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

        lower, upper = lu_decomposition(matrix)
        result_label.config(text=result_label.cget("text") + "\nMatrix L:\n" + display_matrix(lower), fg="#FFFFFF", bg="#00224D")
        result_label.config(text=result_label.cget("text") + "\nMatrix U:\n" + display_matrix(upper), fg="#FFFFFF", bg="#00224D")

        b = [row[-1] for row in matrix]#b is the last column of the matrix
        y = forward_substitution(lower, b)
        x = backward_substitution(upper, y)

        result_label.config(text=result_label.cget("text") + "\n\nLc = b, where c =")
        for i, c in enumerate(y):#(index, value)
            result_label.config(text=result_label.cget("text") + f"\nc{i+1} = {c:.2f}")
        result_label.config(text=result_label.cget("text") + "\n\nUx = c, where x =")
        for i, sol in enumerate(x):
            result_label.config(text=result_label.cget("text") + f"\nx{i+1} = {sol:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all fields.")

def create_entry_widgets():
    entry_frame = tk.Frame(root, bg="#00224D")
    entry_frame.pack(pady=10)

    for i in range(3):
        for j in range(4):
            entry = tk.Entry(entry_frame, width=8, font=('Arial', 12))
            entry.grid(row=i, column=j, padx=5, pady=5)
            entries[i].append(entry)

root = tk.Tk()
root.title("LU Decomposition Calculator")
root.geometry("1500x900")
root.configure(bg="#00224D")
#create 3 empty lists
entries = [[] for _ in range(3)]

# Title label
title_label = tk.Label(root, text="LU Decomposition Calculator", font=("Helvetica", 20, "bold"), fg="#00224D", bg="#FF3EA5")
title_label.pack(pady=(50, 10)) 

# Input matrix label
input_label = tk.Label(root, text="Enter Matrix", font=('Arial', 14, 'bold'), fg="#FFFFFF", bg="#00224D")
input_label.pack()

create_entry_widgets()

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=('Arial', 12), bg="#FF3EA5", fg="#00224D")
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 12), bg="#00224D", justify="left", anchor="w", padx=10)
result_label.pack(pady=10)

root.mainloop()
