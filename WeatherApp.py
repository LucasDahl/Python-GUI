# import libraries
import tkinter as tk

# Set the height and width
canvasHeight = 700
canvasWidth = 800

# Setup the root
root = tk.Tk()

# Setup the canvas
canvas = tk.Canvas(root, height = canvasHeight, width = canvasWidth)
canvas.pack()

# Setup the frame and place it.
frame = tk.Frame(root, bg = "blue")
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

# Add a button to the root and pack it
button = tk.Button(root, text = "Test Button", bg = "gray", fg = "red")
button.pack()

# Run the mianloop
root.mainloop()