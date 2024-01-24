def main():
    """
    Считывает два числа из файла INPUT.TXT, вычисляет их сумму и записывает результат в файл OUTPUT.TXT.
    """
    with open("INPUT.TXT", "r") as file:
        numbers = file.readline().strip().split()
    result = int(numbers[0]) + int(numbers[1])
    with open("OUTPUT.TXT", "w") as file:
        file.write(str(result))

# Запуск main-функции
if __name__ == "__main__":
    main()
