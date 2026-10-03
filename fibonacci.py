n = int(input())
a = 0
b = 1
if n <= 0:
    print(a, end=" ")
if n == 1:
    print(a)
    print(b, end=" ")
else:
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c, end=" ")
