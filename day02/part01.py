POSSIBLE = {'red': 12, 'green': 13, 'blue': 14}


def is_possible(cube: str) -> bool:
    count, color = cube.split()
    if int(count) > POSSIBLE[color]:
        return True
    return False


with open("day02/input.txt") as record:  # noqa: PTH123
    possible_sum = 0
    for line in record.read().splitlines():
        game_id, game = line.split(':')
        if not any(is_possible(cube) for cube in game.replace(';', ',').split(', ')):
            possible_sum += int(game_id.split()[-1])
    print(possible_sum)
