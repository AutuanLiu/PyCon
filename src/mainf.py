## 函数的标准定义，一般情况下要这样使用
def main():
	## extract the first name from a full name
	fullName = input("Enter a full name:")
	print("first name:", firstName(fullName))

def firstName(fullName):
	firstSpace = fullName.index(" ")
	givenName = fullName[:firstSpace]
	return givenName

main()

## 列表解析
def g(x):
    return (int(x) ** 2)
list1 = [2, 4, 5, 6]
list2 = [g(x) for x in list1]
print(list2)

import pylab
pylab.plot(range(10), 'o')