# import libraries
import tkinter as tk

# Properties ===========================================================

# Set the height and width
canvasHeight = 500
canvasWidth = 600

# End Properties =======================================================

# Setup the root
root = tk.Tk()
backgroundImage = tk.PhotoImage(file = "landscape.png")
backgroundLabel = tk.Label(root, image = backgroundImage)
backgroundLabel.place(relwidth = 1, relheight = 1)

# Setup the canvas
canvas = tk.Canvas(root, height = canvasHeight, width = canvasWidth)
canvas.pack()

# Setup the frame and place it.
frame = tk.Frame(root, bg = "blue", bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

# UI Elements =========================================================

# Add an entry bar
entryBar = tk.Entry(frame, font = 40)
entryBar.place(relwidth = 0.65, relheight = 1)

# Add a button to the root and pack it
button = tk.Button(frame, text = "Test Button", font = 40)
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

# Setup the lower Frame
lowerFrame = tk.Frame(root, bg = "blue", bd = 10)
lowerFrame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

# Add a label and pack it in
label = tk.Label(lowerFrame)
label.place(relwidth = 1, relheight = 1)

# End UI Elements ======================================================

# Run the mianloop
root.mainloop()