n = int(input())
a = list(map(int, input().split()))
t = int(input())
lo = 0
r = n - 1
while lo < r:
    if a[lo] + a[r] == t:
        print([lo, r])
        break
    elif a[lo] + a[r] < t:
        lo += 1
    else:
        r -= 1
