def dfs_n_queens(n):
    if n < 1:
        return []
    
    solutions = []
    board = [-1] * n  # board[row] = column of queen in that row

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col:                    # same column
                return False
            if abs(c - col) == abs(r - row): # same diagonal
                return False
        return True

    def dfs(row):
        if row == n:                        # all rows filled → valid solution
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col            # place queen
                dfs(row + 1)                # recurse to next row
                board[row] = -1             # backtrack

    dfs(0)
    return solutions   


print(dfs_n_queens(5),'\n')
print(len(dfs_n_queens(5)),'\n')