def is_palindrome(s: str):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False


def fibonacci(n: int):
    if n < 0:
        raise ValueError("Negative numbers are not allowed!")
    elif n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
