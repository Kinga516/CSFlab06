"""Part C: Factorial and Fibonacci implementations."""

def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)


def iterative_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


class RecursiveFibonacciCounter:
    def __init__(self):
        self.calls = 0

    def fibonacci(self, n):
        self.calls += 1
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


def main():
    print("Task 5: Factorial (Two Methods)")
    number = int(input("Enter number: "))
    print("Iterative factorial =", iterative_factorial(number))
    print("Recursive factorial =", recursive_factorial(number))
    print()

    print("Task 6: Fibonacci Comparison")
    fib_number = int(input("Enter Fibonacci position: "))
    iterative_result = iterative_fibonacci(fib_number)

    counter = RecursiveFibonacciCounter()
    recursive_result = counter.fibonacci(fib_number)

    print("Iterative Fibonacci =", iterative_result)
    print("Recursive Fibonacci =", recursive_result)
    print("Recursive calls =", counter.calls)
    print("Comparison: Iterative Fibonacci is more efficient than recursive Fibonacci because the recursive version makes repeated overlapping calls.")


if __name__ == "__main__":
    main()