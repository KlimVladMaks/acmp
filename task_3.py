def square_number_ending_in_5(num):
    """
    Возводит в квадрат число, оканчивающееся на 5, используя метод Васи.

    Args:
    num (int): Натуральное число, оканчивающееся на цифру 5, не превышающее 4*10^5.

    Returns:
    int: Квадрат введённого числа без начальных нулей.
    """
    if num < 10:
        result = ""
    else:
        num = int(str(num)[:-1])
        result = num * (num + 1)
    return int(str(result) + '25')

def main():
    """
    Считывает натуральное число из INPUT.TXT, возводит его в квадрат, 
    используя метод square_number_ending_in_5, и записывает результат в OUTPUT.TXT.
    """
    with open("INPUT.TXT", "r") as file:
        num = int(file.readline())
    result = square_number_ending_in_5(num)
    with open("OUTPUT.TXT", "w") as file:
        file.write(str(result))

# Запуск main-функции
if __name__ == "__main__":
    main()
