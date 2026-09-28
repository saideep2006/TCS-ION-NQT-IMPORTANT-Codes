n = int(input())
a = list(map(int, input().split()))
c = {}
for i in a:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
print("Count using HashMap:", c[i], "=> ", i)