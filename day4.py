input_file = "input.txt"
#input_file = "test.txt"

input_data = []
picks = []

boards = []

with open(input_file) as f:
    input_data = f.readlines()
    picks = list(map(int, input_data[0].strip().split(',')))

input_data = list(map(lambda s : s.strip(), input_data[2:]))

current_board = []

for l in input_data:
    if l != "":
        row = []
        for num in l.split(' '):
            if num == '':
                continue
            row.append(int(num))
        current_board.append(row)
    else:
        boards.append(current_board)
        current_board = []

boards.append(current_board)

board_size = len(boards[0])

def board_complete(board):
    complete = False
    for row in board:
        if all(map(lambda num : num == -1, row)):
            complete = True
    
    for i in range(board_size):
        if all(map(lambda j : board[j][i] == -1, range(board_size))):
            complete = True
    return complete

solved_board = None
last_pick = None

for pick in picks:
    for board in boards:
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == pick:
                    board[i][j] = -1

    last_solved_board = None

    for board in boards:
        if board_complete(board):
            last_solved_board = board

            if last_solved_board is not None:
                boards.remove(last_solved_board)
                solved_board = last_solved_board
                last_pick = pick
   

    # for board in boards:
    #     if board_complete(board):
    #         solved_board = board
    #         last_pick = pick
    #         break
    # if solved_board is not None:
    #     break

final_sum = 0


for row in solved_board:
    for num in row:
        if num != -1:
            final_sum += num

print(last_pick)
print(final_sum)

print(final_sum * last_pick)