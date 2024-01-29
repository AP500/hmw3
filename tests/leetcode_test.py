import unittest
import pytest
import hmw3.leetcode as leetcode


def test_is_palindrome():
    assert leetcode.is_palindrome("racecar") == True
    assert leetcode.is_palindrome("") == True
    assert leetcode.is_palindrome("a") == True
    assert leetcode.is_palindrome("ab") == False
    assert leetcode.is_palindrome("A n na") == False
    assert leetcode.is_palindrome("RaceCar") == True


def test_fibonacci():
    assert leetcode.fibonacci(2) == 1
    assert leetcode.fibonacci(3) == 2
    assert leetcode.fibonacci(4) == 3
    assert leetcode.fibonacci(5) == 5
    assert leetcode.fibonacci(6) == 8
    assert leetcode.fibonacci(30) == 832040
    with pytest.raises(ValueError):
        leetcode.fibonacci(-1)
    with pytest.raises(RecursionError):
        leetcode.fibonacci(1000)
