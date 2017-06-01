# 乘法表
for m in range(1, 5):
    for n in range(1, 5):
        print(m, 'x', n, '=', m * n, '\t', end = "")
    print()

# 逆序单词
word = input("enter the sentences: ")
reverseword = ""
for ch in word:
	reverseword = ch + reverseword
print("the reverseword is: ", reverseword)