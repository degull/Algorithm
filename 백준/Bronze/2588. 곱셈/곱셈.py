A = int(input())
B = int(input())

B1 = B % 10        
B10 = (B // 10) % 10  
B100 = B // 100       

result1 = A * B1
result2 = A * B10
result3 = A * B100
final_result = A * B

print(result1)
print(result2)
print(result3)
print(final_result)