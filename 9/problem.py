# stupid bruteforce approach, something smarter exists
from itertools import permutations
from functools import reduce
import operator

def is_result(x):
    (a, b, c) = x
    return a**2 + b**2 == c**2


candidates = permutations(range(1,501), 3)
candidates = filter(lambda x: x[0] < x[1] < x[2], candidates)
candidates = filter(lambda x: sum(x) == 1000, candidates)
candidates = filter(lambda x: x[0]**2 + x[1]**2 == x[2]**2, candidates)
final_cand = next(candidates)
print(reduce(operator.mul, final_cand, 1))
