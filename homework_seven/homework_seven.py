
# 1
def get_nearest_number(numbers, target = 0):
    sorted_numbers = sorted(numbers, key=lambda num: abs(num - target))
    print(target, tuple(sorted_numbers))

get_nearest_number([20.18,5,4, 103], 27)

# 2
# map
numbers_list = [1,2,3,4,5,6,7,8,9,10]
mapped_num = list(map(lambda num: num ** 2 / 2, numbers_list))
print(mapped_num)

# filter
words = ["ketchup", "tomato", "lemon", "bbq", "cucumber", "lime", 'coconut']
filtered_words = list(filter(lambda word: 'c' in word, words))
print(filtered_words)

# 3
def get_value_by_index (iterable=[1,2,3,4,5]):
    while True:
        try:
            index = input("Введите index элемента который хотите получить либо введите 'exit' для выхода: ")

            if index.lower() == "exit":
                print("Вы вышли из программы написав exit")
                break

            index = int(index)
            print(f"Элемент который находится под индексом - {index} это: {iterable[index]}")

        except ValueError:
            print(f"Введите число либо введите слово 'exit' верно")
        except IndexError:
            print(f"Введите индекс от 0 до {len(iterable) - 1}")

get_value_by_index()

