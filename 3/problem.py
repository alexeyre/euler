# https://en.wikipedia.org/wiki/Trial_division
from typing import List


def trial_division(n: int) -> List[int]:
    a = []
    while n % 2 == 0:
        a += [2]
        n //= 2
    factor = 3
    while factor**2 <= n:
        if n % factor == 0:
            a += [factor]
            n //= factor
        else:
            factor += 2
    if n != 1:
        a += [n]
    return a


factors = trial_division(600851475143)
sorted(factors)
print(factors[-1])
