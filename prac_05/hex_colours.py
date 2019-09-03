COLOURS = {"AquaMarine": "#7fffd4", "Coral": "#ff7f50", "Black": "#000000", "White": "#ffffff",
           "DarkOrchid": "#9932cc", "DeepPink": "##ff1493", "FireBrick": "#cd2626", "Gold": "#ffd700",
           "LightPink": "#ffb6c1", "LightSeaGreen": "#20b2aa"}

colour = input("Enter Colour: ")
while colour != "":
    if colour in COLOURS:
        print(colour, "is", COLOURS[colour])
else:
    print("Invalid Colour")
colour = input("Enter Colour: ")

# while colour != "":
#    print("Code for \"{}\" is {}".format(colour, COLOURS.get(colour)))
#    colour = input("Enter Colour: ")
