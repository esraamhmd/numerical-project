import tkinter as tk
import subprocess

class WelcomePage:
    def __init__(self, master):
        #self (a reference to the instance itself) and master, representing the main application window.
        self.master = master
        #allowing access to the main application window throughout the class.
        self.master.title("Welcome")
        self.master.geometry("1000x700")
        self.master.configure(bg="#00224D")
        self.master.resizable(False, False)

        self.canvas = tk.Canvas(self.master, bg="#00224D", width=1000, height=700, highlightthickness=0)# no border
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.welcome_text = self.canvas.create_text(500, 200, text="Welcome To", font=("Helvetica", 30, "bold"), fill="#FF3EA5")
        self.calculator_text = self.canvas.create_text(500, 350, text="Numerical Methods Calculator", font=("Helvetica", 36, "bold"), fill="#FF3EA5")
        self.border_rect = self.canvas.create_rectangle(20, 20, 980, 680, outline="#FFFFFF")

        self.go_to_main_button = tk.Button(self.master, text="Start", font=("Helvetica", 18), bg="#FF3EA5", fg="#00224D", command=self.go_to_main,
                                           borderwidth=3, relief=tk.RAISED, padx=13, pady=5)
        self.go_to_main_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.colors = ["#FF3EA5", "#FF7ED4", "#FFB5DA", "#FFAE3E", "#FFD47E", "#FFDA90", "#D43EFF", "#7E3EFF", "#90DAFF", "#7ED4FF", "#B5DAFF", "#7EFF9E", "#3EFF5D", "#90FFDA", "#7EFFD4"]
        self.current_color = 0

        self.animate()

    def animate(self):
        self.canvas.itemconfig(self.welcome_text, fill=self.colors[self.current_color])
        self.canvas.itemconfig(self.calculator_text, fill=self.colors[(self.current_color + 1) % len(self.colors)])
        
        if self.current_color % 2 == 0:
            delay = 500
        else:
            delay = 300

        self.canvas.itemconfig(self.border_rect, outline=self.colors[(self.current_color + 2) % len(self.colors)])
        
        self.current_color = (self.current_color + 1) % len(self.colors)
        self.master.after(delay, self.animate)
    
    def go_to_main(self):
        # Hide the button
        self.go_to_main_button.place_forget()
        # Start Main.py
        subprocess.Popen(["python", "Main.py"])
        # Close the current window
        self.master.destroy()

def main():
    root = tk.Tk()
    app = WelcomePage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
