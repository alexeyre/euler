import math
from typing import List
# try Eratosthenes


def sieve(n: int) -> List[int]:
    A = { i: True for i in range(2, n) }
    i = 2
    sqrt_n = math.sqrt(n)
    while i < sqrt_n:
        if A[i] is True:
            j = i**2
            while j < n:
                A[j] = False
                #print(f"A[{j}] = False")
                j += i
        i += 1
    return list(filter(lambda x: x[1], A.items()))

