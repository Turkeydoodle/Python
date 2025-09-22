import random

squares = list(range(1, 65))
white_positions = {
    'wr1': 1,  'wn1': 2,  'wb1': 3,  'wq': 4,  'wk': 5,  'wb2': 6,  'wn2': 7,  'wr2': 8,
    'wp1': 9,  'wp2': 10, 'wp3': 11, 'wp4': 12, 'wp5': 13, 'wp6': 14, 'wp7': 15, 'wp8': 16
}
black_positions = {
    'br1': 57, 'bn1': 58, 'bb1': 59, 'bq': 60, 'bk': 61, 'bb2': 62, 'bn2': 63, 'br2': 64,
    'bp1': 49, 'bp2': 50, 'bp3': 51, 'bp4': 52, 'bp5': 53, 'bp6': 54, 'bp7': 55, 'bp8': 56
}

def computermove():
    def computerchoose():
        return random.choice(['bp', 'bn', 'br', 'bb'])

    moved = False

    def bishop():
        nonlocal moved
        bishopchosen = random.choice(['bb1', 'bb2'])
        direction = random.choice(['up-left', 'up-right', 'down-left', 'down-right'])
        distancechosen = random.randint(1, 7)
        start_pos = black_positions[bishopchosen]
        path_clear = True
        new_pos = start_pos
        for i in range(1, distancechosen + 1):
            if direction == 'up-left':
                temp_pos = start_pos - 9 * i
            elif direction == 'up-right':
                temp_pos = start_pos - 7 * i
            elif direction == 'down-left':
                temp_pos = start_pos + 7 * i
            elif direction == 'down-right':
                temp_pos = start_pos + 9 * i
            else:
                path_clear = False
                break
            if not (1 <= temp_pos <= 64):
                path_clear = False
                break
            start_rank = (start_pos - 1) // 8
            temp_rank = (temp_pos - 1) // 8
            start_file = (start_pos - 1) % 8
            temp_file = (temp_pos - 1) % 8
            if abs(temp_rank - start_rank) != abs(temp_file - start_file):
                path_clear = False
                break
            if temp_pos in black_positions.values() or temp_pos in white_positions.values():
                path_clear = False
                break
            new_pos = temp_pos
        if path_clear and new_pos != start_pos:
            black_positions[bishopchosen] = new_pos
            print(f'Computer moved {bishopchosen} {direction} {distancechosen} spaces to square {new_pos}.')
            moved = True

    def pawn():
        nonlocal moved
        pawnchosen = random.choice(['bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7', 'bp8'])
        start_pos = black_positions[pawnchosen]
        start_file = (start_pos - 1) % 8
        move_type = random.choice(['forward', 'double', 'capture_left', 'capture_right'])
        if move_type == 'forward':
            new_pos = start_pos - 8
            if new_pos not in black_positions.values() and new_pos not in white_positions.values() and new_pos >= 1:
                black_positions[pawnchosen] = new_pos
                print(f'Computer moved {pawnchosen} forward to square {new_pos}.')
                moved = True
        elif move_type == 'double' and start_pos in range(49, 57):
            new_pos = start_pos - 16
            if new_pos not in black_positions.values() and new_pos not in white_positions.values() and new_pos >= 1:
                black_positions[pawnchosen] = new_pos
                print(f'Computer moved {pawnchosen} two squares forward to square {new_pos}.')
                moved = True
        elif move_type == 'capture_left' and start_file > 0:
            new_pos = start_pos - 7
            if new_pos in white_positions.values() and new_pos >= 1:
                black_positions[pawnchosen] = new_pos
                print(f'Computer moved {pawnchosen} to square {new_pos}, capturing a piece to the left.')
                moved = True
        elif move_type == 'capture_right' and start_file < 7:
            new_pos = start_pos - 9
            if new_pos in white_positions.values() and new_pos >= 1:
                black_positions[pawnchosen] = new_pos
                print(f'Computer moved {pawnchosen} to square {new_pos}, capturing a piece to the right.')
                moved = True

    def knight():
        nonlocal moved
        knightchosen = random.choice(['bn1', 'bn2'])
        start_pos = black_positions[knightchosen]
        start_rank = (start_pos - 1) // 8
        start_file = (start_pos - 1) % 8
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        valid_moves = []
        for dr, df in knight_moves:
            new_rank = start_rank + dr
            new_file = start_file + df
            if 0 <= new_rank < 8 and 0 <= new_file < 8:
                new_pos = new_rank * 8 + new_file + 1
                if new_pos not in black_positions.values():
                    valid_moves.append(new_pos)
        if valid_moves:
            new_pos = random.choice(valid_moves)
            black_positions[knightchosen] = new_pos
            print(f'Computer moved {knightchosen} to square {new_pos}.')
            moved = True

    def rook():
        nonlocal moved
        rookchosen = random.choice(['br1', 'br2'])
        direction = random.choice(['up', 'down', 'left', 'right'])
        distancechosen = random.randint(1, 7)
        start_pos = black_positions[rookchosen]
        path_clear = True
        new_pos = start_pos
        for i in range(1, distancechosen + 1):
            if direction == 'up':
                temp_pos = start_pos - 8 * i
            elif direction == 'down':
                temp_pos = start_pos + 8 * i
            elif direction == 'left':
                temp_pos = start_pos - i
                if (temp_pos - 1) // 8 != (start_pos - 1) // 8:
                    path_clear = False
                    break
            elif direction == 'right':
                temp_pos = start_pos + i
                if (temp_pos - 1) // 8 != (start_pos - 1) // 8:
                    path_clear = False
                    break
            else:
                path_clear = False
                break
            if temp_pos in black_positions.values() or temp_pos in white_positions.values() or not (1 <= temp_pos <= 64):
                path_clear = False
                break
            new_pos = temp_pos
        if path_clear and new_pos != start_pos:
            black_positions[rookchosen] = new_pos
            print(f'Computer moved {rookchosen} {direction} {distancechosen} spaces to square {new_pos}.')
            moved = True

    choice = computerchoose()
    if choice == 'br':
        rook()
    elif choice == 'bn':
        knight()
    elif choice == 'bp':
        pawn()
    elif choice == 'bb':
        bishop()

    return moved

print('Trying computer move...')
for i in range(10):
    while True:
        if computermove():
            break
    print(black_positions)