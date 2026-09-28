n = int(input())
a = list(map(int, input().split()))
lar = a[0]
sec = a[0]
for i in range(1, n):
    if a[i] > lar:
        sec = lar
        lar = a[i]
    elif a[i] > sec:
        sec = a[i]
print("Second maximum in the array:", sec)