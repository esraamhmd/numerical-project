import tkinter as tk
from tkinter import messagebox
import subprocess
import os

class MethodSelectionPage(tk.Tk):
    def __init__(self):
        #Calls the superclass constructor
        super().__init__()
        self.title("Method Selection")
        
        # Set the size of the window
        self.geometry("1000x600")
        
        # Set background color
        self.configure(bg="#00224D")
        
        label_font = ("Arial", 20)  # Font for labels
        button_font = ("Arial", 16)  # Font for buttons
        
        label = tk.Label(self, text="Select a Method:", font=label_font, bg="#FF3EA5", fg="#00224D")
        label.pack(pady=(10, 20))  # Add space both above and below the label
        
        # Define paths to method files
        method_files = {
            "Bisection Method": "Bisection_method.py",
            "False Position Method": "false_poistion_method.py",
            "Simple Fixed Point": "simple_fixed_point.py",
            "Newton Method": "newton_method.py",
            "Secant Method": "secant_method.py",
            "Gauss Elimination": "guass-elimin.py",
            "LU Decomposition": "LU.py",
            "Cramer's Rule": "cramer.py",
            "Gauss Jordan": "guass_jordan.py"
        }
        
        for method, file_name in method_files.items():
            button = tk.Button(self, text=method, font=button_font, width=25, command=lambda m=file_name: self.open_method_file(m), bg="#FF3EA5", fg="#00224D")
            button.pack(pady=(0, 5))  # Add space only below each button
    
    def open_method_file(self, file_name):
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        try:
            subprocess.Popen(['python', file_path])
        except FileNotFoundError:
            messagebox.showerror("Error", f"Method file '{file_path}' not found.")

if __name__ == "__main__":
    app = MethodSelectionPage()
    app.mainloop()
