a, b = int(input()), int(input())
for i in range(1, b+1):
    if i % a == 0:
        max_num = i
print(max_num)