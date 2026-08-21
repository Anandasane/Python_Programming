def number_pattern(n):
    # Check if n is an integer (excluding booleans which are a subclass of int)
    if not isinstance(n, int) or isinstance(n, bool):
        return 'Argument must be an integer value.'
    
    # Check if n is less than 1
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    
    # Build the string of numbers
    result = []
    for i in range(1, n + 1):
        result.append(str(i))
    
    # Join the list into a single string separated by spaces
    return " ".join(result)   

print(number_pattern(12))