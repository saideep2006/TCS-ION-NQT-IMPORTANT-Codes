n = int(input())
c = 0
d = 0
t = n
while t != 0:
    d %= 10
    c += 1
    t //= 10
print(f"Count is:{c}")
