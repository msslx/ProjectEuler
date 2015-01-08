"""
Often used methods for Project Euler Problems
"""

from __future__ import division
import math

# The often used function operator.mul
# within reduce can be rewritten using
# the lambda function: lambda x, y: x*y


def sum_digits(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


def faculty_list(length):
    f = [1, 1]
    if length == 0:
        return []
    if length == 1:
        return [1]
    if length == 2:
        return f
    for i in range(2, length):
        f.append(f[i-1]*i)
    return f


def fibonacci_limit(limit):
    a, b = 1, 2
    while a < limit:
        yield a
        a, b = b, a+b


def fibonacci_element(x):
    a, b = 1, 2
    for i in range(x):
        yield a
        a, b = b, a+b


def fibonacci_n(x):
    return round((((1 + 5**0.5) / 2)**x - (1 - ((1 + 5**0.5) / 2))**x) / 5**0.5)


def generate_circulars(number):
    length = math.ceil(math.log10(number))
    circulars = []
    for i in range(length-1):
        mod = number % 10
        number //= 10
        number += mod*10**(length-1)
        circulars.append(number)
    return circulars


def palindromic_number(n):
    return reverse_number(n) == n


def prime_sieve(n):
    n += 1
    sieve = [False for i in range(n+1)]
    sqrt = int(math.ceil(math.sqrt(n)))
    sieve[0] = True
    sieve[1] = True
    for i in range(2, sqrt+1, 1):
        if not sieve[i]:
            for j in range(n//i, i-1, -1):
                if not sieve[j]:
                    sieve[i*j] = True
    return sieve


def prime_numbers(limit):
    return [i for i, n in enumerate(prime_sieve(limit)) if n is False]


def reverse_number(n):
    rev = 0
    while n > 0:
        rev = 10*rev + n % 10
        n //= 10
    return rev