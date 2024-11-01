A, B = input().split()

# 두 수를 거꾸로 읽음
reversed_A = int(A[::-1])
reversed_B = int(B[::-1])

print(max(reversed_A, reversed_B))