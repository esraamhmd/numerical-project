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


# determinant = a11 * a22 * a33
#             + a12 * a23 * a31
#             + a13 * a21 * a32
#             - a13 * a22 * a31
#             - a12 * a21 * a33
#             - a11 * a23 * a32
def calculate_determinant(matrix):
    return (matrix[0][0] * matrix[1][1] * matrix[2][2] +
            matrix[0][1] * matrix[1][2] * matrix[2][0] +
            matrix[0][2] * matrix[1][0] * matrix[2][1] -
            matrix[0][2] * matrix[1][1] * matrix[2][0] -
            matrix[0][1] * matrix[1][0] * matrix[2][2] -
            matrix[0][0] * matrix[1][2] * matrix[2][1])

def cramer(matrix):
    detA = calculate_determinant([row[:3] for row in matrix])

    if detA == 0:
        return None  # No unique solution

    x1 = calculate_determinant([[matrix[i][3] if j == 0 else matrix[i][j] for j in range(4)] for i in range(3)]) / detA
    x2 = calculate_determinant([[matrix[i][j] if j != 1 else matrix[i][3] for j in range(4)] for i in range(3)]) / detA
    x3 = calculate_determinant([[matrix[i][j] if j != 2 else matrix[i][3] for j in range(4)] for i in range(3)]) / detA

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

        result_text = "Original Matrix:\n" + display_matrix(matrix) + "\n"

        # Display determinants for each augmented matrix
        for i in range(3):
            matrix_copy = [row[:] for row in matrix]  # Create a copy of the original matrix
            for j in range(3):
                matrix_copy[j][i] = matrix[j][3]  # Replace column with solution vector

            determinant = calculate_determinant(matrix_copy)
            result_text += f"\nMatrix A{i+1}:\n" + display_matrix(matrix_copy) + f"Determinant A{i+1}: {determinant:.2f}\n"

        # Calculate and display x1, x2, x3
        solution = cramer(matrix)
        if solution is not None:
            result_text += f"\nSolution:\nX1 = {solution[0]:.2f}\nX2 = {solution[1]:.2f}\nX3 = {solution[2]:.2f}\n"
        else:
            result_text += "\nNo unique solution exists.\n"

        result_label.config(text=result_text, fg="#FFFFFF", bg="#00224D")

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
root.title("Cramer's Rule Calculator")
root.geometry("1500x900")
root.configure(bg="#00224D")  # Set background color of the window

entries = [[] for _ in range(3)]

# Title label
title_label = tk.Label(root, text="Cramer's Rule Calculator", font=("Helvetica", 20, "bold"), fg="#00224D", bg="#FF3EA5")
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
