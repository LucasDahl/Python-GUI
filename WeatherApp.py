# import libraries
import tkinter as tk

# Setup the root
root = tk.Tk()

# Add a button to the root and pack it
button = tk.Button(root, text = "Test Button", bg = "gray", fg = "red")
button.pack()

# Run the mianloop
root.mainloop()