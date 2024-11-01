grade_to_point = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

# 총 학점
total_credits = 0.0

# 총 평점
total_points = 0.0

for _ in range(20):
    # 과목명 data
    data = input().split()
    subject = data[0]
    # 학점 credit
    credit = float(data[1])
    # 등급
    grade = data[2]
    
    if grade == "P":
        continue
        
    # 학점 * 누적 성적
    total_points += credit * grade_to_point[grade]
    total_credits+=credit

if total_credits > 0:
    gpa = total_points/total_credits
else:
    gpa:0.0
        
print(f"{gpa:.6f}")