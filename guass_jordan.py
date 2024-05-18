import tkinter as tk
from tkinter import messagebox

#def print_matrix(matrix, message="Matrix"):
    #print(message)
    #for row in matrix:
        #print(row)

def gauss_jordan(matrix, result_label):
    n = len(matrix)

    # Forward Elimination
    for i in range(n):
        # Partial pivoting
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Make the diagonal elements 1
        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        # Make the other elements in the column 0
        #R2-m21R1=R2
          #R3-m31R1=R3
        for j in range(n):
            if j != i:
                factor = matrix[j][i]
                for k in range(i, n + 1):
                    matrix[j][k] -= factor * matrix[i][k]

        # Print intermediate matrices
        result_label.config(text=result_label.cget("text") + f"\nIntermediate Matrix {i + 1}:\n" + display_matrix(matrix))

    # Print the final solution
    result_label.config(text=result_label.cget("text") + f"\nFinal Solution:\n" + display_matrix(matrix))

    # Calculate and print x1, x2, x3
    x_values = [matrix[row][-1] for row in range(n)]
    result_label.config(text=result_label.cget("text") + f"\nx1 = {x_values[0]}, x2 = {x_values[1]}, x3 = {x_values[2]}")

def display_matrix(matrix):
    matrix_str = ""
    for i in range(len(matrix)):
        matrix_str += "[ "
        for j in range(len(matrix[0])):
            matrix_str += "{:>6.2f} ".format(matrix[i][j])
        matrix_str += "]\n"
    return matrix_str

def calculate():
    matrix = []
    try:
        for i in range(3):
            row = []
            for j in range(4):
                entry = float(entries[i][j].get())
                row.append(entry)
            matrix.append(row)

        result_label.config(text="Original Matrix:\n" + display_matrix(matrix))

        gauss_jordan(matrix, result_label)

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
root.title("Gauss jordan Calculator")
root.geometry("1500x900")
root.configure(bg="#00224D")  # Set background color of the window

entries = [[] for _ in range(3)]

# Title label
title_label = tk.Label(root, text="Gauss Jordan Calculator", font=("Helvetica", 20, "bold"), fg="#00224D", bg="#FF3EA5")
title_label.pack(pady=(50, 10))  # Sticky "ew" to fill horizontally

# Input matrix label
input_label = tk.Label(root, text="Enter Matrix", font=('Arial', 14, 'bold'), fg="#FFFFFF", bg="#00224D")
input_label.pack()

create_entry_widgets()

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=('Arial', 12), bg="#FF3EA5", fg="#00224D")
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 12), bg="#00224D", fg="#FFFFFF", justify="left", anchor="center")
result_label.pack(pady=10, fill="both", expand=True)

root.mainloop()
