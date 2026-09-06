import string

x = input("Enter any sequence of alphabet using small and capital letters, for instance, a-H: ")
parts = x.split("-")
first = parts[0]
second = parts[1]
#знаходимо позицію(індекси) у string.ascii_letters
i1 = string.ascii_letters.index(first)
i2 = string.ascii_letters.index(second)
result = string.ascii_letters[i1:i2 + 1]
print(result)

