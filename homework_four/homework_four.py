#Начало
data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

#1 пункт
letters = []
numbers = []

#2 пункт
for data in data_tuple:
    if isinstance(data, (str, bool)):
        letters.append(data)
    else:
        numbers.append(data)

#3 пункт
deleted_num = numbers.remove(6.13)
index_bool = letters.index(True)
letters.append(letters.pop(index_bool))
numbers.insert(1, 2)

#4 пункт
numbers.sort()
letters.reverse()
letters = [letter.upper() if letter == 'g' else letter.lower() if letter == 'C' else letter for letter in letters]

#5 пункт
sqrt_num = [num * num for num in numbers]

#6 пункт
tuple_letters = tuple(letters)
tuple_num = tuple(sqrt_num)

print(tuple_letters)
print(tuple_num)
