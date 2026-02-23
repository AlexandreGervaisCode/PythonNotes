import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    label = tk.Label(new_window, text="This is a new window!")
    label.pack()

# Create the main window
root = tk.Tk()
root.title("random inputs")

# Create a button to open a new window
button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack()

# Start the GUI event loop
root.mainloop()
