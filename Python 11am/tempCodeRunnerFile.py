s = 1
while s <= 25:
    # Determine which row number we are currently on (0 to 4)
    row = (s - 1) // 5
    
    # Even rows (0, 2, 4) print X, Odd rows (1, 3) print O
    if row % 2 == 0:
        print("X", end=" ")
    else:
        print("O", end=" ")
        
    # At the end of every 5 columns, move to the next line
    if s % 5 == 0:
        print()
        
    s += 1