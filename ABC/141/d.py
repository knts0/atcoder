import heapq

n, m = map(int, input().split())

q = []
heapq.heapify(q)

a = list(map(int, input().split()))

for i in range(n):
    heapq.heappush(q, - a[i])

for i in range(m):
    v = - heapq.heappop(q)
    heapq.heappush(q, - (v // 2))

ans = 0
for i in range(n):
    v = - heapq.heappop(q)
    ans += v
print(ans)