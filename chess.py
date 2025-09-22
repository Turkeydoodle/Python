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
        return random.choice(['br', 'bn'])
    def knight():
        knightchosen = random.choice(['bn1', 'bn2'])
        direction = random.choice(['up', 'down', 'left', 'right'])
        start_pos = black_positions[knightchosen]
        path_clear = True
        new_pos = start_pos
        possiblekinghtmoves = [start_pos + 15, start_pos + 17, start_pos - 15, start_pos - 17, start_pos -6, start_pos -10, start_pos +6, start_pos +10]
        new_pos = random.choice(possiblekinghtmoves)
        if new_pos in black_positions.values():
            path_clear = False 
        if path_clear and new_pos > 0 and new_pos <= 64:
            black_positions[knightchosen] = new_pos
            print(f'Computer moved {knightchosen} to square {new_pos}.')
    def rook():
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
        else:
            print(f'Computer tried to move {rookchosen} {direction} {distancechosen} spaces, but path was blocked or out of bounds.')

    choice = computerchoose()
    if choice == 'br':
        rook()
    elif choice == 'bn':
        knight()
print('Trying computer move...')
computermove()