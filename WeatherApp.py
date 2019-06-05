# import libraries
import tkinter as tk
import requests

# Properties ===========================================================

# Set the height and width
canvasHeight = 500
canvasWidth = 600

# End Properties =======================================================

# Methods===============================================================

# This will format the JSON data
def formatResponse(weather):

    #Try to get the desired JSON data
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]

        finalString = "City: %s \nConditions: %s \nTemperature (°F): %s" % (name, desc, temp)

    #Let the user know there was an error getting the data
    except:
        finalString = "There was a problem the requested info"
    
    # Return the string
    return finalString

# used in getting the city weather data
def getWeather(city):
    #API Key
    weatherKey = ""
    # API URL
    url = "http://api.openweathermap.org/data/2.5/weather"
    # Get a reference for the parameters
    params = {"APPID": weatherKey, "q": city, "units": "imperial"}
    # Bundle up the url and param
    response = requests.get(url, params = params)
    # Collect the json data
    weather = response.json()

    # Set the labels text to the city the user searched for
    label["text"] = formatResponse(weather)

    # Print the json thats returned
    #print(response.json())


def testFunction(entryBar):
    print("You typed:", entryBar)

# End Methods===========================================================

# Setup the root and set the title for the window
root = tk.Tk()
root.title("WeatherApp")

# Setup the canvas
canvas = tk.Canvas(root, height = canvasHeight, width = canvasWidth)
canvas.pack()

# Setup the background image to display
backgroundImage = tk.PhotoImage(file = "landscape.png")
backgroundLabel = tk.Label(root, image = backgroundImage)
backgroundLabel.place(relwidth = 1, relheight = 1)

# Setup the frame and place it.
frame = tk.Frame(root, bg = "blue", bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

# UI Elements =========================================================

# Add an entry bar
entryBar = tk.Entry(frame, font = 40)
entryBar.place(relwidth = 0.65, relheight = 1)

# Add a button to the root and pack it, use a Lambd method so it will be called everytime the button is pressed.
button = tk.Button(frame, text = "Get Weather", font = 40, command = lambda: getWeather(entryBar.get()))
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