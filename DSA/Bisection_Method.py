def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    if number > 1:
        low = 1
        high = number
    else:
        low = 0
        high = 1

    for _ in range(max_iterations):
        mid = (low + high) / 2
        if mid * mid > number:
            high = mid
        else:
            low = mid
        if (high - low) <= tolerance:
            root = (low + high) / 2
            print(f"The square root of {number} is approximately {root}")
            return root

    print(f"Failed to converge within {max_iterations} iterations")
    return None   

