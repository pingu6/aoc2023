with open("day02/input.txt") as record:  # noqa: PTH123
    power_sum = 0
    for line in record.read().splitlines():
        game_id, game = line.split(':')
        cubes: dict[str, list[int]] = {}
        for row in game.split('; '):
            for cube in row.split(', '):
                count, color = cube.split()
                cubes.setdefault(color, []).append(int(count))
        power = 1
        for cube in cubes.values():
            power *= max(cube)
        power_sum += power
    print(power_sum)
