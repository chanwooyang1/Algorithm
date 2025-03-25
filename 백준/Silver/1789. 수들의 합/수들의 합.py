
N = int(input())
max = 0
num = 1
count = 0
while(True):
    if max + num > N:
        print(count)
        break
    else:
        max = max + num
        num = num + 1
        count = count + 1
    