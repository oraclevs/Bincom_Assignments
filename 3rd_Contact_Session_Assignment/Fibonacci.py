# Implement a Fibonacci series generator.


#  A Fibonacci sequence
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


n = 30  
print(fibonacci(n))