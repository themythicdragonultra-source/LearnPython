x, d, n = map(int, input().split())
arr = []
for i in range(n - 1, -1, -1):
     arr.append(x + i * d)
print(*arr)