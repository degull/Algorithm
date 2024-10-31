import sys
input = sys.stdin.readline

T = int(input().strip())

results = []

for _ in range(T):
    A, B = map(int, input().strip().split())
    results.append(A + B)
    
print("\n".join(map(str, results)))