def robot_returns_to_origin(moves):
    x = 0
    y = 0

    for move in moves:
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
        elif move == "R":
            x += 1
        elif move == "L":
            x -= 1

    return x == 0 and y == 0


# Test 
test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))
