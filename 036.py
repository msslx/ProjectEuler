"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

from __future__ import division
import math

from Euler import palindromic_number, reverse_number


def e036a():
    # in base2 a palindromic number must be odd
    counter = 0
    for i in range(1, 1000000, 2):
        if palindromic_number(i) and palindromic_number(i, 2):
            counter += i
    return counter


# Instead of checking every number in both bases for being palindromic
# Generate all palindromic numbers in one base and check in the second
# All palindromic numbers with length 3, 4 are generated by xy
# xy -> xyx, xyyx
# this can be continued. Since the limit is 1000000 we need to go up to
# xyz -> xyzyx, xyzzyx
# obviously there are more palindromes in base2, thus we generate
# base10 palindromes
def e036b():
    counter = 0
    for i in range(1, 1000):
        length = math.ceil(math.log10(i))
        palindromic1 = i*10**length + reverse_number(i)
        if length > 1:
            palindromic2 = i*10**(length-1) + reverse_number(i//10)
        else:
            palindromic2 = i
        if palindromic_number(palindromic1, 2):
            counter += palindromic1
        if palindromic_number(palindromic2, 2):
            counter += palindromic2
    return counter

print(e036b())