def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = [" ".join(str(r) for r in rods)]

    def move(disk, src, dst, aux):
        if disk == 1:
            rods[dst].append(rods[src].pop())
            states.append(" ".join(str(r) for r in rods))
        else:
            move(disk - 1, src, aux, dst)
            rods[dst].append(rods[src].pop())
            states.append(" ".join(str(r) for r in rods))
            move(disk - 1, aux, dst, src)

    move(n, 0, 2, 1)
    return "\n".join(states)   
    

print(hanoi_solver(3))
print('====================================================================================================================================')

def Hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    steps = [" ".join(str(r) for r in rods)]

    def move(disk, src, dst, aux):
        if disk == 1:
            rods[dst].append(rods[src].pop())
            steps.append(" ".join(str(r) for r in rods))
        else:
            move(disk - 1, src, aux, dst)
            rods[dst].append(rods[src].pop())
            steps.append(" ".join(str(r) for r in rods))
            move(disk - 1, aux, dst, src)

    move(n, 0, 2, 1)
    result = "\n".join(steps)
    print(f"Total moves required: {len(steps) - 1}")  # ← print step count
    print(result)
    return result   

print(Hanoi_solver(3))