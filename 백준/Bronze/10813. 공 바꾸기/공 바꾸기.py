# 바구니 개수(N개), 교환 횟수(M번)
N, M = map(int, input().split())

# 각 바구니에 1~N 번호 초기화
buckets = list(range(1, N+1))

# 두 바구니 교환
for _ in range(M):
    i, j = map(int, input().split())
    #i와 j번 바구니의 공 교환
    buckets[i-1], buckets[j-1] = buckets[j - 1], buckets[i - 1]
    
print(" ".join(map(str, buckets)))