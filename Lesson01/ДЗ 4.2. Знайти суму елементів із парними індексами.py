lst = [67, 89, 666, 23, 0,0,85,123, 0, 456, 23,89,0,34]
total = 0
for index, value in enumerate(lst):
    if index % 2 == 0:
        total = total + value
if lst:
    product = total * lst[-1]
else:
    product = 0
print(product)






