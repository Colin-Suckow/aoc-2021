days = 256

fish_list = [0,0,0,0,0,0,0,0,0]
with open('input.txt') as input_string:
    fish_ages = list(map(int, input_string.readlines()[0].strip().split(',')))
    for fish in fish_ages:
        fish_list[fish] += 1
def run_cycle():
    reset_fish = 0
    born_fish = 0
    for i, fish_count in enumerate(fish_list):
        if i == 0:
            reset_fish = fish_count
            born_fish = fish_count
            fish_list[0] = fish_list[1]
        elif i == 8:
            fish_list[i] = 0
        else:
            fish_list[i] = fish_list[i + 1]
    fish_list[6] += reset_fish
    fish_list[8] += born_fish

for i in range(days):
    run_cycle()

print(sum(fish_list))
