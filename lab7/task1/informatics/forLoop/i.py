import math

n = int(input())
count = 0

limit = int(math.sqrt(n))

for i in range(1, limit + 1):
    if n % i == 0:
        if i * i == n:
            count += 1
        else:
            count += 2

print(count)