with open("input.txt") as f:
    directions = f.readlines()
    x = 0
    y = 0
    aim = 0
    for direction in directions:
        direction = direction.strip()
        parts = direction.split(" ")
        d = parts[0]
        dist = int(parts[1])
        if d == 'forward':
            x += dist
            y += dist * aim
        if d == 'down':
            aim += dist
        if d == 'up':
            aim -= dist
    print(x * y)