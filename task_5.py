def decide_grade(grades):
    """
    Разбивает заданный массив оценок на два массива, содержащих четные и нечетные числа,
    и определяет, может ли Вася рассчитывать на 4 балла.
    
    Args:
    grades (list): Список оценок, полученных Васей.
    
    Returns:
    tuple: Два массива, содержащие нечетные и четные числа, а также строку, указывающую,
    может ли Вася рассчитывать на оценку 4.
    """
    threes = []
    fours = []
    for grade in grades:
        if grade % 2 == 0:
            fours.append(grade)
        else:
            threes.append(grade)
    if len(fours) >= len(threes):
        return threes, fours, "YES"
    else:
        return threes, fours, "NO"

def main():
    """
    Считывает оценки из файла INPUT.TXT, вызывает функцию decode_grade для определения
    оценки Васи и записывает результат в файл OUTPUT.TXT.
    """
    with open("INPUT.TXT", "r") as file:
        file.readline()
        grades = [int(x) for x in file.readline().split()]
    threes, fours, answer = decide_grade(grades)
    with open("OUTPUT.TXT", "w") as file:
        file.write(" ".join(str(x) for x in threes))
        file.write("\n")
        file.write(" ".join(str(x) for x in fours))
        file.write("\n")
        file.write(answer)

# Запуск main-функции
if __name__ == "__main__":
    main()
