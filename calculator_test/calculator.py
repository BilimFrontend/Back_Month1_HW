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
    operation = str(num_and_operation[1])

    try:
        num_one = int(num_and_operation[0])
        num_two = int(num_and_operation[2])
    except ValueError:
        print("Введите только числа")
    else:
        result = calculator(num_one, operation, num_two)
        if result is not None:
            print(result)

start_code()
print(calculator.__doc__)