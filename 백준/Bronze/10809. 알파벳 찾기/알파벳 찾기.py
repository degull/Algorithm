S = input().strip()

positions = [S.find(chr(i)) for i in range(ord('a'), ord('z')+1)]

print(" ".join(map(str, positions)))