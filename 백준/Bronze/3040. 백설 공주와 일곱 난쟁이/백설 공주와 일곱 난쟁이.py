dwarfs = [int(input()) for _ in range(9)]
total = sum(dwarfs)

for i in range(9):
    for j in range(i + 1, 9):
        if total - dwarfs[i] - dwarfs[j] == 100:
            for k in range(9):
                if k not in [i,j]:
                    print(dwarfs[k])