N, M = map(int, input().split())

# 바구니 안 공 들어있지 않음 -> 0으로 초기화
buckets = [0]*N

#M개의 줄에 걸쳐 공을 넣는 방법
for _ in range(M):
    i, j, k = map(int, input().split())
    
    # i번째 바구니부터 j번째 바구니까지 k(공 번호)로 채움
    for idx in range(i-1, j):
        buckets[idx] = k
        
print(" ". join(map(str, buckets)))