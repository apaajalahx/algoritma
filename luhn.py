#!/bin/python3
# https://en.wikipedia.org/wiki/Luhn_algorithm
def luhn(numbers) -> bool:
    digit = len(numbers)
    s = 0
    p = digit % 2
    for i in range(digit):
        digits = int(numbers[i])
        if (i % 2) == p:
            digits = digits * 2
        if digits > 9:
            digits = digits - 9
        s = s + digits
    print(s % 10)
    return (s % 10) == 0

print(luhn('4408041234567893'))
