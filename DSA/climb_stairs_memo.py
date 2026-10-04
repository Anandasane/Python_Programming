def climb_stairs_paths(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        memo[n] = [[1]]
        print(f"n=1: {memo[n]}")
        return memo[n]
    if n == 2:
        memo[n] = [[1, 1], [2]]
        print(f"n=2: {memo[n]}")
        return memo[n]

    paths1 = climb_stairs_paths(n-1, memo)
    paths2 = climb_stairs_paths(n-2, memo)

    all_paths = [[1] + p for p in paths1] + [[2] + p for p in paths2]
    memo[n] = all_paths
    print(f"n={n}: [[1]+p for p in {paths1}] + [[2]+p for p in {paths2}]")
    print(f"     = {[ [1]+p for p in paths1 ]} + {[[2]+p for p in paths2]}")
    print(f"     = {all_paths}")
    return all_paths

climb_stairs_paths(4)   

