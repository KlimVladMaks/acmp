def is_valid_move(move):
    """
    Определяет правильность хода коня на основе введенных пользователем данных.

    Args:
    move (str): Строка, представляющая ход конем в формате "XY-UV",
    где X, Y, U и V - координаты.

    Returns:
    str: Строка, указывающая на правильность перемещения: "YES", если перемещение
    правильное, "NO", если перемещение неправильное, но координаты действительны,
    и "ERROR", если координаты неверны или формат ввода неверен.
    """
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    rows = ['1', '2', '3', '4', '5', '6', '7', '8']
    if len(move) != 5:
        return "ERROR"
    start_col, start_row, dash, end_col, end_row = move
    if (start_col in columns and end_col in columns and
            start_row in rows and end_row in rows
            and dash == "-"):
        start_col_index = columns.index(start_col)
        start_row_index = rows.index(start_row)
        end_col_index = columns.index(end_col)
        end_row_index = rows.index(end_row)
        col_diff = abs(start_col_index - end_col_index)
        row_diff = abs(start_row_index - end_row_index)
        if (col_diff == 1 and row_diff == 2) or (col_diff == 2 and row_diff == 1):
            return "YES"
        else:
            return "NO"
    else:
        return "ERROR"

def main():
    """
    Считывает входные данные из файла "INPUT.TXT", вызывает функцию is_valid_move для
    определения правильности перемещения и записывает результат в файл "OUTPUT.TXT".
    """
    with open("INPUT.TXT", "r") as file:
        move = file.readline().strip()
    result = is_valid_move(move)
    with open("OUTPUT.TXT", "w") as file:
        file.write(result)

# Запускаем main-функцию
if __name__ == "__main__":
    main()
