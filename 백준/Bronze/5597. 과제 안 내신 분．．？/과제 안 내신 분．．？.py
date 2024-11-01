all_students = set(range(1, 31))

submitted_students = {int(input().strip()) for _ in range(28)}

missing_students = sorted(all_students-submitted_students)

print(missing_students[0])
print(missing_students[1])