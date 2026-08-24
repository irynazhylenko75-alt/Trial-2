
# Зрізи (slice) списку
# https://wezom.academy/ua/chto-takoe-spiski-v-python-i-kak-s-nimi-rabotat/

# 0    1   2   3  4  5
# [15, 12, 10, 8, 5, 6]
# -6 -5  -4  -3 -2  -1

# numbers[:-1] від початку до останнього
# numbers[-1:]  тільки останній

# Код (варіант 1)
my_random_list = [15, 12, 10, 8, 5, 6]

#[останній]   + [усі іші]
my_random_list = my_random_list[-1:] + my_random_list[:-1]

print(my_random_list)

# Код (варіант 2)
my_random_list = [15, 12, 10, 8, 5, 6]

# Pop — видаляє елемент у заданому індексі та виводить віддалений елемент. При цьому, якщо ви не вкажете індекс, то метод видалить останній елемент.

last = my_random_list.pop()

my_random_list.insert(0, last)

print(my_random_list)