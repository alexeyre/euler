tmp = 0
x = 1
y = 2
summation = 0
while x < 4 * 10**6:
    if y % 2 == 0:
        summation += y
    tmp = y
    y += x
    x = tmp
print(summation)
