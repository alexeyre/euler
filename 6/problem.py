# this is a maths problem

# sum of n squared numbers is n/6 (n+1)(2n + 1)
# sum of n numbers is n/2 (n+1), so this squared is n^2 / 4 (n+1)^2

# difference is thus n/6 (n+1)(2n + 1) - n^2 / 4 * (n+1)^2

def compute_difference(n):
    return n * (n+1) * (2*n + 1) / 6 - n**2 * (n+1)**2 / 4

print(compute_difference(100))
