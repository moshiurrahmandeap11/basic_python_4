# Fibonacci Sequence

def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Example usage
print(fibonacci(10))  # Should return first 10 Fibonacci numbers