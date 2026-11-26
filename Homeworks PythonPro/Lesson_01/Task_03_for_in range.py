height = int(input("Enter the height of rectangle: "))
width = int(input("Enter the width of rectangle: "))
#Rectangle
for _ in range(height):
    print("*" * width)
print("-----------------------------------")
#Right triangle
for row in range(width):
    print ("*" * (row +1))
print("-----------------------------------")
#Inverted triangle
for row in range (width):
    print("*" * (width - row))
print("-----------------------------------")
#Hollow rectangle
for row in range(height):
    if row == 0 or row == height -1:
        print("*" * width)
    else:
        print("*" + " " * (width -2) + "*")
