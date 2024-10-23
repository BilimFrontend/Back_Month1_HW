# 1
# 1.1
from sys import dllhandle


def password_check (password):
    symbols = '@#$%^&*()!_+=/.,<>'
    defect_symbol = set()
    for password_letter in password:
        if password_letter in symbols:
            defect_symbol.add(password_letter)

    if len(password) >= 6 and not defect_symbol:
        print(f"Ваш пароль: {password}")
    elif defect_symbol:
        print(f"Пароль не должен содержать: {defect_symbol}")
    else:
        print(f"Ваш пароль не надежный: {password}")


password_check('123456')

# 2
# 2.1
def get_nearest_number(numbers, target=0):
    # 2.2
    nearest_num = numbers[0]
    for number in numbers:
        if abs(number - target) <= abs(nearest_num - target):
            nearest_num = number
    print(f"Ближайшее число к {target} это {nearest_num}")

get_nearest_number([1, 2, 3], 5)
