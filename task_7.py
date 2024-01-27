def main():
    """
    Считывает входные данные из INPUT.TXT, находит кучу с максимальным количеством монет
    и записывает результат в OUTPUT.TXT
    """
    with open('INPUT.TXT', 'r') as input_file:
        data = input_file.read().strip().split()
    piles = list(map(int, data))
    with open('OUTPUT.TXT', 'w') as output_file:
        output_file.write(str(max(piles)))

# Запускаем main-функцию
if __name__ == '__main__':
    main()
