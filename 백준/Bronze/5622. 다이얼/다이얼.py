# 각 숫자에 해당하는 알파벳 그룹과 시간을 매핑
dial_time = {
    'A': 3, 'B': 3, 'C': 3,
    'D': 4, 'E': 4, 'F': 4,
    'G': 5, 'H': 5, 'I': 5,
    'J': 6, 'K': 6, 'L': 6,
    'M': 7, 'N': 7, 'O': 7,
    'P': 8, 'Q': 8, 'R': 8, 'S': 8,
    'T': 9, 'U': 9, 'V': 9,
    'W': 10, 'X': 10, 'Y': 10, 'Z': 10
}

# 단어 입력 받기
word = input().strip()

# 단어의 각 알파벳에 대해 걸리는 시간을 계산하여 합산
total_time = sum(dial_time[char] for char in word)

# 결과 출력
print(total_time)
