n = int(input())
s = 0
t = n
while t != 0:
    d = t % 10
    s = s * 10 + d
    t //= 10
print(s)
