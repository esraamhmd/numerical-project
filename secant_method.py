import tkinter as tk
from tkinter import ttk
# Function to calculate f(x)
def f(x):
    return eval(entry_f.get().replace("^", "**"))  # Allowing '^' as exponentiation operator

# Secant method
def secant(x0, x1, eps, iter, results):
    while True:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        error = abs((x2 - x1) / x2) * 100
        
        if round_check_var.get():
            results.append((iter, round(x0, round_num), round(f(x0), round_num), round(x1, round_num), round(f(x1), round_num), round(x2, round_num), round(f(x2), round_num), round(error, round_num)))
        else:
            results.append((iter, x0, f(x0), x1, f(x1), x2, f(x2), error))
        
        if error < eps:
            root_result.set(f"Root = {x2:.{round_num}f}" if round_check_var.get() else f"Root = {x2}")
            final_result_label.config(text=root_result.get())
            
            for item in result_tree.get_children():
                result_tree.delete(item)
                
            for result in results:
                result_tree.insert('', 'end', values=result)
                
            return
            
        x0, x1 = x1, x2
        iter += 1

# Function to handle button click event
def calculate_root():
    global round_num
    x0 = float(entry_x0.get())
    x1 = float(entry_x1.get())
    eps = float(entry_eps.get())
    round_num = int(round_num_entry.get())
    results = []
    secant(x0, x1, eps, 0, results)

# Create tkinter window
root = tk.Tk()
root.title("Secant Method Calculator")
root.geometry("800x400")  # Set window size
root.configure(bg="#00224D")  # Set background color of the window

# Add title label with background color matching button color
title_label = tk.Label(root, text="Secant Method", font=("Helvetica", 20, "bold"), fg="#00224D", bg="#FF3EA5")
title_label.pack(fill="x", pady=10)  # Fill the width of the window

# Add spacing
tk.Label(root, bg="#00224D").pack()

# Create labels and entry widgets
input_frame = tk.Frame(root, bg="#00224D")
input_frame.pack()

tk.Label(input_frame, text="Enter f(x):", bg="#00224D", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=0, column=0, sticky="w")
entry_f = tk.Entry(input_frame, font=("Helvetica", 12, "bold"))
entry_f.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Enter x-1:", bg="#00224D", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=1, column=0, sticky="w")
entry_x0 = tk.Entry(input_frame, font=("Helvetica", 12, "bold"))
entry_x0.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Enter xo:", bg="#00224D", fg="#FFFFFF", font=("Helvetica", 12, "bold")).grid(row=2, column=0, sticky="w")
entry_x1 = tk.Entry(input_frame, font=("Helvetica", 12, "bold"))
entry_x1.grid(row=2, column=1, padx=10, pady=5)

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
columns = ("Iteration", "xi-1", "f(xi-1)", "i", "f(xi)", "Error %")
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
#

root.mainloop()
