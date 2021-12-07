import statistics

def part1():
    with open('input.txt') as input_string:
        in_pos = list(map(int, input_string.readlines()[0].strip().split(',')))
        closest = statistics.median(in_pos)
        result = sum(list(map(lambda x : abs(x - closest), in_pos)))
        print(int(result))

def part2():
    with open('input.txt') as input_string:
        in_pos = list(map(int, input_string.readlines()[0].strip().split(',')))
        closest = int(statistics.mean(in_pos))
        fuel_cache = {}

        def fuel(n):
            result = 0
            if n in fuel_cache:
                return fuel_cache[n]
            elif n == 0:
                result = 0
            else:
                result = n + fuel(n - 1)
            fuel_cache[n] = result
            return result

        result = sum(list(map(lambda x : fuel(abs(x - closest)), in_pos)))
        print(int(result))

#part1()
part2()
