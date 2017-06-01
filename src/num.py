## 求最值及平均值
list1 = [] # 列表
print("(Enter -1 to terminate.)")
num = eval(input("Enter a number:"))
while num != -1:
	list1.append(num)
	num = eval(input("Enter a number:"))
# display result
n = len(list1)
if n > 0:
	list1.sort()
	print("Min:", list1[0])
	print("max:", list1[-1])
	print("average", sum(list1)/n)
else:
	print("error")

