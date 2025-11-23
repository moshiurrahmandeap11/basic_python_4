# Multiplication Table

def multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(f"{n} x {i} = {n * i}")
    return table

# Example usage
print(multiplication_table(5))  # Should return multiplication table of 5