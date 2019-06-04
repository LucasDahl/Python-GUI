# import libraries
import tkinter as tk

# Properties ===========================================================

# Set the height and width
canvasHeight = 700
canvasWidth = 800

# End Properties =======================================================

# Setup the root
root = tk.Tk()

# Setup the canvas
canvas = tk.Canvas(root, height = canvasHeight, width = canvasWidth)
canvas.pack()

# Setup the frame and place it.
frame = tk.Frame(root, bg = "blue")
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

# UI Elements =========================================================

# Add an entry bar
entryBar = tk.Entry(frame, font = 40)
entryBar.place(relwidth = 0.65, relheight = 1)

# Add a button to the root and pack it
button = tk.Button(frame, text = "Test Button", font = 40)
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

# Add a label and pack it in
#label = tk.Label(frame, text = "Hello World!", bg = "yellow")
#label.place(relx = 0.3, rely = 0, relwidth = 0.45, relheight = 0.25)

# End UI Elements ======================================================

# Run the mianloop
root.mainloop()