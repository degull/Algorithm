# 현재시각
A, B = map(int, input().split())
# 요리하는 데 필요한 시간
C = int(input())

# 분 계산
B+=C
A+=B // 60
B%=60

A%=24

print(A,B)
