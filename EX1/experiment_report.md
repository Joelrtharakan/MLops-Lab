# Crafting Effective Test Cases for Python Functions

## 1. Title
Crafting Effective Test Cases for Python Functions

## 2. Objective
Learn how to write simple Python functions and test them with clear cases.

## 3. Job Role
Software Engineer and QA Tester

## 4. Skills Required
- Basic Python programming
- Simple logic for functions
- Understanding of test cases and edge cases
- Ability to read and write tables

## 5. Prerequisites
- Python installed
- Basic understanding of numbers, strings, lists
- Ability to run Python scripts and see printed output

## 6. Description
A test case is a simple check to see if a function works correctly. Test cases help find mistakes early. Good test cases include normal inputs and special cases like empty values or invalid data.

## 7. Implementation

### Problem 1: Factorial Function

**Explain the problem:**
The factorial of a number is the product of all whole numbers from 1 to that number. For example, 4! is 1 * 2 * 3 * 4 = 24. For zero, the factorial is 1. Negative numbers are not allowed.

**Python function:**
```python
# Factorial function using simple loop

def factorial(n):
    if n < 0:
        return "Error: negative input"
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
```

**Test cases:**

| Test Case | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| Positive number | 5 | 120 | 120 | Pass |
| Zero | 0 | 1 | 1 | Pass |
| Negative number | -3 | Error: negative input | Error: negative input | Pass |

**Sample outputs:**
```text
factorial(5) -> 120
factorial(0) -> 1
factorial(-3) -> Error: negative input
```

---

### Problem 2: Palindrome Checker

**Explain the problem:**
A palindrome is a word or phrase that reads the same forwards and backwards. This checker should ignore uppercase and lowercase letters, and it should keep letters, numbers, and symbols.

**Python function:**
```python
# Check if a string is a palindrome

def is_palindrome(text):
    lower_text = text.lower()
    reversed_text = lower_text[::-1]
    return lower_text == reversed_text
```

**Test cases:**

| Test Case | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| Odd length palindrome | "Level" | True | True | Pass |
| Even length palindrome | "Noon" | True | True | Pass |
| Palindrome with numbers | "12321" | True | True | Pass |
| Palindrome with symbols | "!@#@!" | True | True | Pass |
| Not a palindrome | "Hello" | False | False | Pass |

**Sample outputs:**
```text
is_palindrome("Level") -> True
is_palindrome("Noon") -> True
is_palindrome("12321") -> True
is_palindrome("!@#@!") -> True
is_palindrome("Hello") -> False
```

---

### Problem 3: Prime Number Checker

**Explain the problem:**
A prime number is a whole number greater than 1 that has no divisors other than 1 and itself. Numbers like 2, 3, 5 are prime. Zero, one, and negative numbers are not prime.

**Python function:**
```python
# Check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

**Test cases:**

| Test Case | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| Prime number | 7 | True | True | Pass |
| Non-prime number | 8 | False | False | Pass |
| Zero | 0 | False | False | Pass |
| One | 1 | False | False | Pass |
| Negative number | -5 | False | False | Pass |

**Sample outputs:**
```text
is_prime(7) -> True
is_prime(8) -> False
is_prime(0) -> False
is_prime(1) -> False
is_prime(-5) -> False
```

---

### Problem 4: Sorting Function

**Explain the problem:**
Sorting means putting numbers in order from smallest to largest. The function should handle an empty list and repeated numbers.

**Python function:**
```python
# Sort a list in ascending order

def simple_sort(numbers):
    # Use Python built-in sort for simplicity
    sorted_numbers = numbers[:]  # copy list to avoid changing original
    sorted_numbers.sort()
    return sorted_numbers
```

**Test cases:**

| Test Case | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| Normal list | [3, 1, 4, 2] | [1, 2, 3, 4] | [1, 2, 3, 4] | Pass |
| Empty list | [] | [] | [] | Pass |
| Repeated elements | [2, 5, 2, 1] | [1, 2, 2, 5] | [1, 2, 2, 5] | Pass |

**Sample outputs:**
```text
simple_sort([3, 1, 4, 2]) -> [1, 2, 3, 4]
simple_sort([]) -> []
simple_sort([2, 5, 2, 1]) -> [1, 2, 2, 5]
```

---

### Problem 5: Fibonacci Sequence

**Explain the problem:**
The Fibonacci sequence starts with 0 and 1, and each next number is the sum of the two before it. The function should create a list of Fibonacci numbers up to n terms. If n is zero or negative, the function should return an empty list.

**Python function:**
```python
# Generate Fibonacci sequence up to n terms

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
```

**Test cases:**

| Test Case | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| Normal input | 5 | [0, 1, 1, 2, 3] | [0, 1, 1, 2, 3] | Pass |
| n = 1 | 1 | [0] | [0] | Pass |
| n = 0 | 0 | [] | [] | Pass |
| Negative input | -2 | [] | [] | Pass |

**Sample outputs:**
```text
fibonacci(5) -> [0, 1, 1, 2, 3]
fibonacci(1) -> [0]
fibonacci(0) -> []
fibonacci(-2) -> []
```

## 8. Result
This experiment shows how simple functions and clear test cases help find correct behavior. Each problem includes normal checks and edge cases to make sure the code works well.

## 9. Learning Outcome
- Learned how to write easy Python functions with clear comments.
- Learned how to build test cases that include normal and edge situations.
- Learned why testing is important to catch problems early.
