n = int(input())
t = n
s = 0
while t != 0:
    d = t % 10
    s += d
    t //= 10
print(f"The sum of digits in {n} is {s}")
