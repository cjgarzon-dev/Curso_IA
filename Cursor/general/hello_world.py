import tkinter as tk
from tkinter import ttk

def greet():
    name = entry.get()
    result_label.config(text=f"Hello {name}!")

# Create main window
window = tk.Tk()
window.title("My First Interface")
window.geometry("400x200")

# Create and configure style
style = ttk.Style()
style.configure('TButton', font=('Arial', 12))
style.configure('TLabel', font=('Arial', 12))

# Create widgets
label = ttk.Label(window, text="Enter your name:")
entry = ttk.Entry(window, width=30)
button = ttk.Button(window, text="Greet", command=greet)
result_label = ttk.Label(window, text="")

# Place widgets in window
label.pack(pady=10)
entry.pack(pady=5)
button.pack(pady=10)
result_label.pack(pady=10)

# Start main loop
window.mainloop()

