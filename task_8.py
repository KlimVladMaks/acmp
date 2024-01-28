def check_product(a, b, c):
    """
    Проверяет, равно ли произведение A и B числу C.
    
    Args:
    a (int): Первое число.
    b (int): Второе число.
    c (int): Третье число.
    
    Returns:
    str: 'YES', если произведение A и B равно C, 'NO' в противном случае.
    """
    if a * b == c:
        return 'YES'
    else:
        return 'NO'

def main():
    """
    Считывает входные данные из файла, проверяет произведение A и B на корректность
    и записывает результат в выходной файл.
    """
    with open('INPUT.TXT', 'r') as file:
        data = file.read().split()
        a, b, c = int(data[0]), int(data[1]), int(data[2])
    result = check_product(a, b, c)
    with open('OUTPUT.TXT', 'w') as file:
        file.write(result)

# Запускаем main-функцию
if __name__ == '__main__':
    main()
