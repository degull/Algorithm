#숫자개수
N = int(input().strip())

numbers = input().strip()

total_sum = sum(int(num) for num in numbers)

print(total_sum)