ls = [15, 12, 10, 8, 5, 6, 34, 112, 7]

if len(ls) == 0:
    new_ls = [[], []]
else:
    mid = len(ls) // 2

    if len(ls) % 2 == 1:
        mid = mid + 1

    first_half = ls[:mid]
    second_half = ls[mid:]

    new_ls = [first_half, second_half]

print(new_ls)