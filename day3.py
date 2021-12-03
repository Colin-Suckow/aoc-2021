with open("input.txt") as f:

    og_input = f.readlines()

    search_space = og_input.copy()
    current_bit = 0

    while len(search_space) > 1:
        bits = [0, 0, 0, 0, 0, 0, 0,0,0,0,0,0]

        total_lines = 0

        for l in search_space:
            total_lines += 1
            for i in range(12):
                if l[i] == '1':
                    bits[i] += 1
        
        co2 = ""
        ox = ""

        co2 = co2.join(list(map(lambda bc : "1" if bc - (total_lines - bc) >= 0 else "0", bits)))

        new_space = []

        for l in search_space:
            if l[current_bit] == co2[current_bit]:
                new_space.append(l)
        search_space = new_space
        current_bit += 1
    
    co2 = search_space[0].strip()

    search_space = og_input.copy()
    current_bit = 0

    while len(search_space) > 1:
        bits = [0, 0, 0, 0, 0, 0, 0,0,0,0,0,0]

        total_lines = 0

        for l in search_space:
            total_lines += 1
            for i in range(12):
                if l[i] == '1':
                    bits[i] += 1
        
        ox = ""

        ox = ox.join(list(map(lambda bc : "1" if bc - (total_lines - bc) < 0 else "0" , bits)))

        new_space = []

        for l in search_space:
            if l[current_bit] == ox[current_bit]:
                new_space.append(l)
        search_space = new_space
        current_bit += 1

    ox = search_space[0].strip()

    print(int(co2,2) * int(ox,2))
