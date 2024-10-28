def calculator(num_one:int, operator:str, num_two:int) -> float:
    """Фунцкия Выполняет арифметическую операцию

        num_one (int): Первое число
        num_two (int): Второе число
        operator (str): Оператор для выполнения операции ('+', '-', '*', '/')

        возвращает float: Результат арифметической операции

    Важно:
        Если попытаться разделить на ноль, выведет сообщение об ошибке
        и вернёт ничего вместо результата.
    """
    try:
        if operator == '+':
            return num_one + num_two
        elif operator == "-":
            return num_one - num_two
        elif operator == "*":
            return num_one * num_two
        elif operator == "/":
            return num_one / num_two

    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        print("Неизвестная операция")



def start_code():

    num_and_operation = input("Калькулятор. Введите операцию: ").strip().replace(" ", "")
    for op in "+-*/":
        if op in num_and_operation:
            operator = op
            break

    try:
        num_one, num_two = map(int, num_and_operation.split(operator))
        print(num_and_operation.split(operator))
        # Метод split() ищет в строке символ + и использует его как разделитель
        # В результате он разрезает строку в тех местах, где находит символ +
        # Сам разделитель (+) удаляется,
        # и вы получаете список, содержащий только те части строки,
        # которые были по обе стороны от оператора — '10' и '10'.
    except ValueError:
        print("Введите только числа")

    else:
        result = calculator(num_one, operator, num_two)
        if result is not None:
            print(result)

start_code()
print(calculator.__doc__)