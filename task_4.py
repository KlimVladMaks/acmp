def main():
    """
    Считывает одиночную цифру k из файла INPUT.TXT, вычисляет первую и последнюю цифры 
    результата и записывает результат в файл OUTPUT.TXT.
    """
    with open("INPUT.TXT", "r") as f:
        k = int(f.readline().strip())
    first_digit = k
    last_digit = 9 - k
    result = str(first_digit) + "9" + str(last_digit)
    with open("OUTPUT.TXT", "w") as f:
        f.write(result)

# Запуск main-функции
if __name__ == "__main__":
    main()
