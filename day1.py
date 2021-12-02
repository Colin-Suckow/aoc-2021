with open(" .txt") as f:
    ints = list(map(int, f.readlines()))
    count = 0
    for i in range(0, len(ints) - 3):
        if ints[i] + ints[i + 1] + ints[i + 2] < ints[i + 1] + ints[i + 2] + ints[i + 3]:
            count += 1
    print(count)
