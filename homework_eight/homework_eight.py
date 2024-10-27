
def findGuessNumber(minNum = 1, maxNum = 100):
    with open('results.txt', 'w', encoding="utf-8") as file:
        file.write("Результат\n")

    try:
        secret_number = int(input("Загадайте число: "))
        attempts_list = []
        attempts_number = 0
        while True:
            average_number = int((minNum + maxNum) // 2)

            if average_number == secret_number:
                yes_or_no = input(f"Ваше число {average_number}? ").lower()

                if yes_or_no == "да":
                    with open('results.txt', 'a', encoding='utf-8') as file:
                        file.write(f'Количество попыток: {attempts_number}\n')
                        file.write(f'Список попыток: {attempts_list}\n')
                        file.write(f'Загаданное число: {secret_number}')
                    print("Число угадано!")
                    break
                elif yes_or_no not in ["да", "нет"]:
                    print("Введите только да или нет")
                else:
                    print("Вы врёте")

            else:
                print(f"Ваше число {average_number}?")
                moreOrLess = input("+ или -: ").lower()

                if moreOrLess not in ["+", "-"]:
                    print("Введите только + или -")
                    continue

                if moreOrLess == "+":
                    minNum = average_number + 1
                elif moreOrLess == "-":
                    maxNum = average_number - 1

                attempts_list.append(average_number)
                attempts_number += 1

        print(f"Загаданное число: {secret_number}")
        print(f"Кол-во попыток: {attempts_number}")
        print(f"Список попыток: {attempts_list}")

    except ValueError:
        print("Введите только число ")



findGuessNumber()