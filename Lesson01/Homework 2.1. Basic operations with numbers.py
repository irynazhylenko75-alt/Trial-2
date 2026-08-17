# Квадрат числа
number = int(input("Enter your favourite number: "))
square = number ** 2
print ("Square is", square)


# Середнє трьох чисел
number1 = int(input("Enter your first unlucky number: "))
number2 = int(input("Enter your second unlucky number: "))
number3 = int(input("Enter your third unlucky number: "))

average = round((number1 + number2 + number3) / 3, 3)
print ("Your unlucky average is", average)


# Перетворення хвилин у години
duration = int(input("Enter the duration of your favourite movie in minutes: "))
hours = duration //60
minutes = duration % 60
if hours > 1:
    print ("The duration of your favourite movie is", hours,"hours", minutes, "minutes")
if hours == 1:
    print("The duration of your favourite movie is", hours, "hour", minutes, "minutes")
if hours == 0:
    print ("The duration of your favourite movie is", minutes, "minutes")


# "Розрахунок знижки”
price = int(input("Enter the price of the car that you would like to purchase in dollars: "))
discount = int(input("Enter the discount for the car that you would like to purchase in %: "))
final_price = round (price*(1 - discount / 100))
print ("The final price for the car that you would like to purchase is", final_price, "$")

# “Остання цифра числа”
whole_number = int(input("Enter any whole number that comes to your mind: "))
last_digit = whole_number % 10
print ("The last digit of whole_number is", last_digit)


# “Периметр прямокутника”
length = int(input("Enter the length of the rectangle in cm: "))
width = int(input("Enter the width of the rectangle in cm: "))
perimeter = (length + width) * 2
print ("The perimeter of the rectangle is ", perimeter, "cm")


#  Виведення числа в стовпчик
number = int(input("Please enter a four-digit number"))
first_digit = number // 1000
second_digit = (number // 100) % 10
third_digit = (number // 10) % 10
fourth_digit = number % 10
print ("The first digit of number is ", first_digit)
print("The second digit of number is ", second_digit)
print("The third digit of number is ", third_digit)
print("The fourth digit of number is ", fourth_digit)

