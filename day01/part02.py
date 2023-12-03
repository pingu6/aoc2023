NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
with open("day01/input.txt") as fb:  # noqa: PTH123
    calibration = 0
    document = fb.read()
    for word, number in NUMBERS.items():
        document = document.replace(word, f"{word}{number}{word}")
    for line in document.splitlines():
        numbers = [character for character in line if character.isdigit()]
        if numbers:
            calibration += int(f"{numbers[0]}{numbers[-1]}")
    print(calibration)
