## function define
def trip(num):
	## can't modify the value 
	num *= 3
	return num
num = 8
print(trip(num))
print(num)

## 元音字母
def occur(word):
	word = word.upper()
	vowels = ('A', 'E', 'I', 'O', 'U')
	include = []
	for vow in vowels:
		if (vow in word) and (vow not in include):
			include.append(vow)
	return include

word = input("Enter a word:")
listOfVowels = occur(word)
print("The following vowels occur in the word:")
string = " ".join(listOfVowels) # 转化为字符串
print(string)