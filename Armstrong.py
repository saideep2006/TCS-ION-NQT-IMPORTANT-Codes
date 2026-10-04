n = int(input())
c = 0
s = 0
t = n
while t != 0:
    d = t % 10
    c += 1
    s += d**3
    t //= 10
if s == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
