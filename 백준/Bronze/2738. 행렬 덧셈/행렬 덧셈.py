# N과 M 입력받기
N, M = map(int, input().split())

# 첫 번째 행렬 A 입력받기
matrix_A = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_A.append(row)

# 두 번째 행렬 B 입력받기
matrix_B = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix_B.append(row)

# 두 행렬 A와 B의 합을 계산
result_matrix = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(matrix_A[i][j] + matrix_B[i][j])
    result_matrix.append(row)

# 결과 행렬 출력
for row in result_matrix:
    print(" ".join(map(str, row)))
