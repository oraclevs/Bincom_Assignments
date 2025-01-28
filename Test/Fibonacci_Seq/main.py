def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

# Usage
num_terms = 10  # Specify the number of terms 
print(fibonacci(num_terms))
