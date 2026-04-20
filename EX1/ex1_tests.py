# Simple tests for Python functions

# 1. Factorial Function

def factorial(n):
    if n < 0:
        return "Error: negative input"
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# 2. Palindrome Checker

def is_palindrome(text):
    lower_text = text.lower()
    reversed_text = lower_text[::-1]
    return lower_text == reversed_text

# 3. Prime Number Checker

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. Sorting Function

def simple_sort(numbers):
    sorted_numbers = numbers[:]  # copy list to avoid changing original
    sorted_numbers.sort()
    return sorted_numbers

# 5. Fibonacci Sequence

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

# Print test results
print("Factorial tests")
print("factorial(5) ->", factorial(5))
print("factorial(0) ->", factorial(0))
print("factorial(-3) ->", factorial(-3))
print()

print("Palindrome tests")
print("is_palindrome('Level') ->", is_palindrome('Level'))
print("is_palindrome('Noon') ->", is_palindrome('Noon'))
print("is_palindrome('12321') ->", is_palindrome('12321'))
print("is_palindrome('!@#@!') ->", is_palindrome('!@#@!'))
print("is_palindrome('Hello') ->", is_palindrome('Hello'))
print()

print("Prime tests")
print("is_prime(7) ->", is_prime(7))
print("is_prime(8) ->", is_prime(8))
print("is_prime(0) ->", is_prime(0))
print("is_prime(1) ->", is_prime(1))
print("is_prime(-5) ->", is_prime(-5))
print()

print("Sorting tests")
print("simple_sort([3, 1, 4, 2]) ->", simple_sort([3, 1, 4, 2]))
print("simple_sort([]) ->", simple_sort([]))
print("simple_sort([2, 5, 2, 1]) ->", simple_sort([2, 5, 2, 1]))
print()

print("Fibonacci tests")
print("fibonacci(5) ->", fibonacci(5))
print("fibonacci(1) ->", fibonacci(1))
print("fibonacci(0) ->", fibonacci(0))
print("fibonacci(-2) ->", fibonacci(-2))
