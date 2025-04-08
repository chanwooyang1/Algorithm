dwarfs = [int(input()) for _ in range(9)]

target = 100

dwarfs.sort()
total = sum(dwarfs)
a, b = 0, 0
diff = total - target

for i in range(9):
    for j in range(i+1, 9):
        if dwarfs[i] + dwarfs[j] == diff:
            a = dwarfs[i]
            b = dwarfs[j]
dwarfs.remove(a)
dwarfs.remove(b)
for dwarf in dwarfs:
    print(dwarf)