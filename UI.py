import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
window = tk.Tk()
window.title("Multifamily Workflow Tool")

# Create a label
label = tk.Label(window, text="Enter your name:")
label.pack()

# Create an entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button
button = tk.Button(window, text="Click me", command=on_button_click)
button.pack()

# Start the main loop
window.mainloop()