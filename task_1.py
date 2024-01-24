def main():
    with open("INPUT.TXT", "r") as file:
        numbers = file.readline().strip().split()
    result = int(numbers[0]) + int(numbers[1])
    with open("OUTPUT.TXT", "w") as file:
        file.write(str(result))

if __name__ == "__main__":
    main()
