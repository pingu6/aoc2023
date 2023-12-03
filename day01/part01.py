with open('day01/input.txt') as document:  # noqa: PTH123
    calibration = 0
    for line in document.readlines():
        numbers = [character for character in line if character.isdigit()]
        if numbers:
            calibration += int(f'{numbers[0]}{numbers[-1]}')
    print(calibration)
