n = int(input())
arr = list(map(int, input().split()))
print("Reversed Array:")
for i in range(n-1, -1, -1):
    print(arr[i], end=" ")