n = int(input())
a = list(map(int, input().split()))
hs = set()
c = 0
for i in a:
    if i in hs:
        c += 1
    else:
        hs.add(i)
if c > 0:
    print("Yes duplicates there!!!")
else:
    print("No duplicates there!!!")
