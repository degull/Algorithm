def min_coins(n):
    # 5원 동전을 최대한 많이 사용
    # stop = -1
    # step = -1
    for five_count in range(n//5, -1, -1):
        remainder = n - (5 * five_count)
        
    # 남은 금액이 2원으로 나누어 떨어진다면
        if remainder % 2 == 0:
            two_count = remainder // 2
            return five_count + two_count
 
    return -1

n = int(input())
print(min_coins(n))