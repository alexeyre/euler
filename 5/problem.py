import math
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def is_evenly_divisible(n: int) -> bool:
    return all(n % i == 0 for i in range(1, 21))

n = 1
for i in range(1, 21):
    n *= i // math.gcd(i, n)
print(n)
