# 1. Factorial Function
def factorial(n):
    if n < 0:
        return "Error"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Test Cases for Factorial
print("Factorial Tests")
print(factorial(5))   # 120
print(factorial(0))   # 1
print(factorial(-3))  # Error
print()


# 2. Palindrome Function
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]


# Test Cases for Palindrome
print("Palindrome Tests")
print(is_palindrome("Level"))   # True
print(is_palindrome("Noon"))    # True
print(is_palindrome("12321"))   # True
print(is_palindrome("Hello"))   # False
print()


# 3. Prime Number Function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Test Cases for Prime
print("Prime Tests")
print(is_prime(7))    # True
print(is_prime(8))    # False
print(is_prime(0))    # False
print(is_prime(-5))   # False
print()


# 4. Sorting Function
def simple_sort(lst):
    return sorted(lst)


# Test Cases for Sorting
print("Sorting Tests")
print(simple_sort([3, 1, 4, 2]))   # [1, 2, 3, 4]
print(simple_sort([]))             # []
print(simple_sort([2, 5, 2, 1]))   # [1, 2, 2, 5]
print()


# 5. Fibonacci Function
def fibonacci(n):
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


# Test Cases for Fibonacci
print("Fibonacci Tests")
print(fibonacci(5))   # [0, 1, 1, 2, 3]
print(fibonacci(1))   # [0]
print(fibonacci(0))   # []
print(fibonacci(-2))  # []