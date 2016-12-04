INPUT = 'L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R4, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1'.split(', ')


def calculate_destination_coordinates(directions):
    coords = {'x': 0, 'y': 0}
    facing = 'N'
    for i in directions:
        turn = i[0]
        blocks = int(i[1:])
        facing = facing_from_turn(facing, turn)
        coords = move_with_facing(coords, facing, blocks)
    return coords


def facing_from_turn(facing, turn):
    if facing == 'N':
        if turn == 'L':
            return 'W'
        if turn == 'R':
            return 'E'
    if facing == 'E':
        if turn == 'L':
            return 'N'
        if turn == 'R':
            return 'S'
    if facing == 'S':
        if turn == 'L':
            return 'E'
        if turn == 'R':
            return 'W'
    if facing == 'W':
        if turn == 'L':
            return 'S'
        if turn == 'R':
            return 'N'


def move_with_facing(coords, facing, blocks):
    if facing == 'N':
        coords['y'] += blocks
    if facing == 'E':
        coords['x'] += blocks
    if facing == 'S':
        coords['y'] -= blocks
    if facing == 'W':
        coords['x'] -= blocks
    return coords

if __name__ == '__main__':
    destination_coordinates = calculate_destination_coordinates(INPUT)
    print(destination_coordinates)
    raise NotImplementedError()
