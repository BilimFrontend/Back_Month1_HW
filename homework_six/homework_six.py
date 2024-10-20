# 1
# 1.1
def password_check (password):
    if len(password) >= 6:
        print(f'Ваш пароль: {password}')
        return True
    else:
        print("Не надежный пароль")
        return False

password_check('asd')

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
