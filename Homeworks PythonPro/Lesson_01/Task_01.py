color = input("Enter a color: ")
color = color.lower().strip()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait and Get ready")
elif color == "green":
   print("Go, if it is safe")
else:
    print("Unknown signal")

print ("-----------------------------")

color = input("Enter a color: ")
color = color.lower().strip()

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait and get ready")
    case "green":
        print("Go, if it is safe")
    case _:
        print("Unknown signal")
