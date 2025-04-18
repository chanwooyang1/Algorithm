word = input()
result = True

for i in range(len(word)// 2):
	if word[i] != word[-(i + 1)]:
	    result = False
	    break

if result:
    print(1)
else:
    print(0)

