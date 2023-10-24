def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_sequence(n):
    i = 0
    while i < n:
        print(fibonacci(i), end=" ")
        i = i + 1
    
    
if __name__ == "__main__":
    fibonacci_sequence(1)
    fibonacci_sequence(2)
    fibonacci_sequence(3)
    fibonacci_sequence(4)
    fibonacci_sequence(5)

 