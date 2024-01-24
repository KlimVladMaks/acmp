def calculate_sum(n):
    """
    Вычисляет сумму целых чисел от 1 до n включительно.

    Args:
    n (int): Верхний предел диапазона для вычисления суммы.

    Returns:
    int: Сумма целых чисел от 1 до n включительно.
    """
    if n < 1:
        return (n * (n - 1)) // -2 + 1
    else:
        return (n * (n + 1)) // 2

def main():
    """
    Считывает целое число из файла INPUT.TXT и записывает сумму чисел 
    от 1 до этого целого числа (включительно) в файл OUTPUT.TXT.
    """
    with open("INPUT.TXT", "r") as file:
        n = int(file.readline())
    result = calculate_sum(n)
    with open("OUTPUT.TXT", "w") as file:
        file.write(str(result))

# Запуск main-функции
if __name__ == "__main__":
    main()
