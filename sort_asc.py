n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if a[i] < a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t
for i in range(n):
    print(a[i])