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
        return random.choice(['br', 'bn', 'bp'])
    def pawn():
        global moved
        pawnchosen = random.choice(['bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7', 'bp8'])
        start_pos = black_positions[pawnchosen]
        new_pos = start_pos - random.choice([-8, -16, -9, -7])
    def knight():
        global moved
        knightchosen = random.choice(['bn1', 'bn2'])
        start_pos = black_positions[knightchosen]
        start_rank = (start_pos - 1) // 8
        start_file = (start_pos - 1) % 8
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                        (1, -2), (1, 2), (2, -1), (2, 1)]
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
        else:
            print(f'Computer tried to move {knightchosen}, but no valid moves were available.')


    def rook():
        global moved
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
        else:
            print(f'Computer tried to move {rookchosen} {direction} {distancechosen} spaces, but path was blocked or out of bounds.')
    choice = computerchoose()
    if choice == 'br':
        rook()
    elif choice == 'bn':
        knight()
    elif choice == 'bp':
        pawn()
print('Trying computer move...')
moved = False
while not moved:
    computermove()
print(black_positions)