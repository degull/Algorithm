T = int(input())

results = []

for i in range(1, T+1):
    A, B = map(int, input().split())
    results.append(f"Case #{i}: {A + B}")
    
print("\n".join(results))