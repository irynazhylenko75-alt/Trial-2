total_seconds = int(input("Enter a number that is equal to or greater than zero, less than 8640000:"))
day = total_seconds // 86400
remainder_1 = total_seconds % 86400
hour = remainder_1// 3600
remainder_2 = remainder_1 % 3600
minute = remainder_2 // 60
seconds = remainder_2 % 60
#zfill() in programming (specifically Python) is a string method that pads a string on the left with zeros until it reaches a specified total length.
hour = str(hour).zfill(2)
minute = str(minute).zfill(2)
seconds = str(seconds).zfill(2)
#1, 21, 31, 41... (закінчується на 1, крім 11) → "день"
#2,3,4, 22,23,24... (закінчується на 2,3,4, крім 12,13,14) → "дні"
#Всі інші (0, 5-20, 25-30...) → "днів"
last_digit = day % 10
last_two_digits = day % 100 # для винятків 11, 12, 13, 14 (8640000 // 86400 = 100 = > максимальна кількість дннів 99)
if 11 <= last_two_digits <= 14:
    day_word = "днів"
elif last_digit == 1:
    day_word = "день"
elif last_digit in [2,3,4]:
    day_word = "дні"
else:
    day_word = "днів"
print(f"{day} {day_word}, {hour}:{minute}:{seconds}")



