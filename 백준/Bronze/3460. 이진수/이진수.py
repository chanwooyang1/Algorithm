def binary(num):
    answer = []
    while num > 0:
        answer.append(num % 2)
        num = num // 2
    return answer 

T = int(input())
for _ in range(T):
    n = int(input())
    bi = binary(n)
    all_a_index = [i for i in range(len(bi)) if bi[i] == 1]
    print(" ".join(map(str, all_a_index)))


