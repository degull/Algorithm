N = int(input().strip())

# 현재성적
scores = list(map(int, input().split()))

# 최고점수 찾기
max_score = max(scores)

# 점수조작
new_scores = [(score/max_score)*100 for score in scores]

# 평균계산
average = sum(new_scores)/N

print(f"{average : .6f}")