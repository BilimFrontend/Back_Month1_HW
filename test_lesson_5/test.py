while True:
    traffic_light = input("Введите цвет светофора (красный, зеленый, желтый): ").lower()
    if traffic_light == "выход":
        print("Цикл завершен")
        break
    elif traffic_light == "красный":
        print("Стой!")
    elif traffic_light == "зеленый":
        print("Можешь идти")
    elif traffic_light == "желтый":
        print("Жди")
    else:
        print("Нужно ввести один из трех цветов светофора. Если хотите выйти то напишите 'Выход'")