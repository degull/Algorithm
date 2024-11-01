numbers = [int(input().strip()) for _ in range(9)]

# 최댓값 찾고
max_value = max(numbers)

# 그게 몇번재 수인지
max_index = numbers.index(max_value)+1

print(max_value)
print(max_index)