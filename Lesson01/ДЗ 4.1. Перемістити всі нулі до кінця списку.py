lst = [67, 89, 666, 23, 0,0,85,123, 0, 456, 23,89,0,34]
zeros = lst.count(0)
while zeros > 0:
    lst.remove(0)
    lst.append(0)
    zeros = zeros -1
print(lst)

