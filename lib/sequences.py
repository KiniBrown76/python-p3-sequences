def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length < 0:
        print("Length must be a positive integer.")
        return
    
    fibonacci_sequence = []
    
    a, b = 0, 1
    
    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    print(fibonacci_sequence)


print_fibonacci(9)