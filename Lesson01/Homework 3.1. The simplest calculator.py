#Оператор	Опис
# x == y	Рівні
# x != y	Не рівні
# x > y	більше
# x < y	менше
# x >= y	більше чи рівні
# x <= y	менше чи рівні

# Я не впевнена, але так розумію, що треба враховувати, що число може бути дробовим.

print("Let's start!")
number_1 = float(input("Enter a number: "))
operation = input("Choose an operation to perform (+, -, *, /): ")
number_2 = float(input("Enter another number: "))
if operation == "+":
    print("The sum is", number_1 + number_2)
elif operation == "-":
    print("The difference is", number_1 - number_2)
elif operation == "*":
    print("The product is", number_1 * number_2)
elif operation == "/":
    if number_2 != 0:
        print("The quotient is", number_1 / number_2)
    else:
        print("Oops, you cannot divide by zero 😰.")

        # не розумію чому останній рядок, а саме print("Oops, you cannot divide by zero 😰.")
        #  у PayCharm сірим кольором




