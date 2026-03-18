import math

n = int(input())
k = int(input())

print(k - (math.floor(k/n) * n))