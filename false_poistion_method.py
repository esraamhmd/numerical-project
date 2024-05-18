import tkinter as tk
from tkinter import ttk
from math import pow

# Function to calculate f(x)
def f(x):
    return eval(entry_f.get().replace("^", "**"))  # Allowing '^' as exponentiation operator

# False Position method
def false_position(xl, xu, xr, xr_old, error, iter, results):
    xr_old = xr
    xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
    error = abs((xr - xr_old) / xr) * 100

    if round_check_var.get():
        if iter == 0:
            results.append((iter, round(xl, round_num), round(f(xl), round_num), round(xu, round_num), round(f(xu), round_num), round(xr, round_num), round(f(xr), round_num), ""))
        else:
            results.append((iter, round(xl, round_num), round(f(xl), round_num), round(xu, round_num), round(f(xu), round_num), round(xr, round_num), round(f(xr), round_num), round(error, round_num)))
    else:
        if iter == 0:
            results.append((iter, xl, f(xl), xu, f(xu), xr, f(xr), ""))
        else:
            results.append((iter, xl, f(xl), xu, f(xu), xr, f(xr), error))

    m = f(xl) * f(xr)
    if m > 0:
        xl = xr
    elif m == 0:
        return xr
    else:
        xu = xr
    iter += 1

    if error > eps:
        false_position(xl, xu, xr, xr_old, error, iter, results)
    else:
        root_result.set(f"Root = {xr:.{round_num}f}" if round_check_var.get() else f"Root = {xr}")  # Set root result text
        final_result_label.config(text=root_result.get())  # Update final result label

        # Clear existing table entries
        for item in result_tree.get_children():
            result_tree.delete(item)

        # Populate the table with all iterations
        for result in results:
            result_tree.insert('', 'end', values=result)

# Function to handle button click event
def calculate_root():
    global eps, round_num
    eps = float(entry_eps.get())
    xl = float(entry_xl.get())
    xu = float(entry_xu.get())
    round_num = int(round_num_entry.get())
    results = []
    false_position(xl, xu, 0, 0, 0, 0, results)
    root.geometry("1500x900")  # Set window size

# Create tkinter window
root = tk.Tk()
root.title("False Position Method Calculator")
root.geometry("800x400")  # Set window size
root.configure(bg="#00224D")  # Set background color of the window

# Add title label with background color matching button color
title_label = tk.Label(root, text="False Position Method", font=("Helvetica", 20, "bold"), fg="#00224D", bg="#FF3EA5")
title_label.pack(fill="x", pady=10)  # Fill the width of the window

# Add spacing
tk.Label(root, bg="#00224D").pack()

# Create labels and entry widgets
input_frame = tk.Frame(root, bg="#00224D")
input_frame.pack()

tk.Label(input_frame, text="Enter f(x):", bg="#00224D", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=0, column=0, sticky="w")
entry_f = tk.Entry(input_frame, font=("Helvetica", 12, "bold"))
entry_f.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Enter xl:", bg="#00224D", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=1, column=0, sticky="w")
entry_xl = tk.Entry(input_frame, font=("Helvetica", 12, "bold"))
entry_xl.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Enter xu:", bg="#00224D", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=2, column=0, sticky="w")
entry_xu = tk.Entry(input_frame, font=("Helvetica", 12, "bold"))
entry_xu.grid(row=2, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Enter epsilon:", bg="#00224D", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=3, column=0, sticky="w")
entry_eps = tk.Entry(input_frame, font=("Helvetica", 12, "bold"))
entry_eps.grid(row=3, column=1, padx=10, pady=5)

round_check_var = tk.BooleanVar()
round_check = tk.Checkbutton(input_frame, text="Round Result", variable=round_check_var, bg="#00224D", fg="#FFFFFF", selectcolor="black", font=("Helvetica", 12, "bold"))
round_check.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

round_num_entry = tk.Entry(input_frame, font=("Helvetica", 12, "bold"))
round_num_entry.grid(row=5, column=1, padx=10, pady=5)
round_num_label = tk.Label(input_frame, text="Enter Number of Decimal Places to Round to:", bg="#00224D", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
round_num_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

# Create a button to calculate the root
calculate_button = tk.Button(root, text="Calculate Root", command=calculate_root, bg="#FF3EA5", fg="#00224D", font=("Helvetica", 14, "bold"))
calculate_button.pack(pady=10)

# Create a label to display the final root result
root_result = tk.StringVar()  # Variable to hold root result text
root_result.set("")  # Initialize to empty string
final_result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#00224D", fg="#FFFFFF")
final_result_label.pack()

# Create a table to display the results
columns = ("Iteration", "xl", "f(xl)", "xu", "f(xu)", "xr", "f(xr)", "Error %")
result_tree = ttk.Treeview(root, columns=columns, show='headings', style="mystyle.Treeview")
for col in columns:
    result_tree.heading(col, text=col)
result_tree.pack(padx=10, pady=5, fill="both", expand=True)

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=result_tree.yview)
scrollbar.pack(side="right", fill="y")
result_tree.configure(yscrollcommand=scrollbar.set)
# Add black grid lines
style = ttk.Style()
style.theme_use("default")
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Helvetica', 12), background="#FFFFFF", foreground="#00224D")
style.map("mystyle.Treeview", background=[('selected', '#FF3EA5')])
style.configure("mystyle.Treeview", rowheight=25)
style.configure("mystyle.Treeview.Heading", background="#FF3EA5", foreground="#00224D")

root.mainloop()
