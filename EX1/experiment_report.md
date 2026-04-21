# Crafting Effective Test Cases for Python Functions

## 1. Title
Crafting Effective Test Cases for Python Functions

## 2. Objective
Learn how to write simple Python functions and test them with clear examples.

## 3. Job Role
Software Engineer and QA Tester

## 4. Skills Required
- Basic Python programming
- Simple logic for functions
- Understanding of test cases and edge cases
- Ability to read tables and compare results

## 5. Prerequisites
- Python installed on your computer
- Know how to open a terminal or command prompt
- Know how to run a Python script

## 6. Description
A test case is a small check that tells if a function works correctly. Good test cases use normal values and special values such as zero or wrong input. This helps find mistakes before the code is used.

## 7. Implementation

### Problem 1: Factorial Function

**Explain the problem:**
The factorial of a number is the product of all whole numbers from 1 up to that number. For example, 4! is 1 * 2 * 3 * 4 = 24. The factorial of 0 is 1. Negative numbers are not allowed.

**Python function:**
```python
# Factorial function using simple loop

def factorial(n):
    if n < 0:
        return "Error"
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
```

**Why it works:**
- If n is negative, return the string `Error`.
- Start with 1 and multiply by every number up to n.
- Return the final result.

**Test cases:**

| Test Case | Input | Expected Output | Status |
|---|---|---|---|
| Positive number | 5 | 120 | Pass |
| Zero | 0 | 1 | Pass |
| Negative number | -3 | Error | Error | Pass |

**Sample outputs:**
```text
factorial(5) -> 120
factorial(0) -> 1
factorial(-3) -> Error
```

---

### Problem 2: Palindrome Checker

**Explain the problem:**
A palindrome is a word or phrase that reads the same forwards and backwards. This checker ignores letter case and checks the text exactly.

**Python function:**
```python
# Check if a string is a palindrome

def is_palindrome(text):
    lower_text = text.lower()
    reversed_text = lower_text[::-1]
    return lower_text == reversed_text
```

**Why it works:**
- Convert the text to lowercase.
- Reverse the text.
- Compare the reversed text to the original lowercase text.

**Test cases:**

| Test Case | Input | Expected Output | Status |
|---|---|---|---|
| Odd length palindrome | "Level" | True | Pass |
| Even length palindrome | "Noon" | True | Pass |
| Palindrome with numbers | "12321" | True | Pass |
| Palindrome with symbols | "!@#@!" | True | Pass |
| Not a palindrome | "Hello" | False | Pass |

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
A prime number is a whole number greater than 1 that is only divisible by 1 and itself. Numbers like 2, 3, and 5 are prime. Zero, one, and negative numbers are not prime.

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

**Why it works:**
- If n is 1 or less, return False.
- Check divisors from 2 up to the square root of n.
- If any divisor divides n, it is not prime.

**Test cases:**

| Test Case | Input | Expected Output | Status |
|---|---|---|---|
| Prime number | 7 | True | Pass |
| Non-prime number | 8 | False | Pass |
| Zero | 0 | False | Pass |
| One | 1 | False | Pass |
| Negative number | -5 | False | Pass |

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
Sorting means putting numbers in order from smallest to largest. The function should work for empty lists and lists with duplicate numbers.

**Python function:**
```python
# Sort a list in ascending order

def simple_sort(lst):
    return sorted(lst)
```

**Why it works:**
- Python's built-in `sorted()` function returns a new sorted list.
- The original list is not changed.
- Return the sorted result.

**Test cases:**

| Test Case | Input | Expected Output | Status |
|---|---|---|---|
| Normal list | [3, 1, 4, 2] | [1, 2, 3, 4] | Pass |
| Empty list | [] | [] | Pass |
| Repeated elements | [2, 5, 2, 1] | [1, 2, 2, 5] | Pass |

**Sample outputs:**
```text
simple_sort([3, 1, 4, 2]) -> [1, 2, 3, 4]
simple_sort([]) -> []
simple_sort([2, 5, 2, 1]) -> [1, 2, 2, 5]
```

---

### Problem 5: Fibonacci Sequence

**Explain the problem:**
The Fibonacci sequence starts with 0 and 1. Each next number is the sum of the two numbers before it. If n is zero or negative, return an empty list.

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

**Why it works:**
- Handle cases where n is 0 or negative.
- Start the list with [0, 1].
- Add new numbers until the list has n items.

**Test cases:**

| Test Case | Input | Expected Output | Status |
|---|---|---|---|
| Normal input | 5 | [0, 1, 1, 2, 3] | Pass |
| n = 1 | 1 | [0] | Pass |
| n = 0 | 0 | [] | Pass |
| Negative input | -2 | [] | Pass |

**Sample outputs:**
```text
fibonacci(5) -> [0, 1, 1, 2, 3]
fibonacci(1) -> [0]
fibonacci(0) -> []
fibonacci(-2) -> []
```

## 8. Commands
Run this file in a terminal:
```bash
python ex1_tests.py
```

The file prints the result of each test directly.

## 9. Result
This experiment shows how simple functions and clear test cases help find correct behavior. Each problem uses normal checks and edge cases to make sure the code works well.

## 10. Learning Outcome
- Learn how to write easy Python functions with comments.
- Learn how to build test cases that include normal and edge situations.
- Learn why testing is important to catch problems early.

## 11. Exam Tips
- Always check the input and output for each function.
- Use test cases for normal values and special values.
- Describe why the function returns an error for bad input.
