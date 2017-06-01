a = "python"
b = "Hello World!"
print(a[1], b[3], b[2:7], sep = ',')
print(b.find('W'))
print(a.rfind('o'))
print(b[0:-3])
print(b[-4])
print(a[:], b[3:], b[:4], sep = ',')
# 字符串连接
print("haha" * 4 + " Lily")
# 文件操作
infile = open("data.txt", 'r') 
listName1 = [eval(line) for line in infile]
# listName = [line.rstrip() for line in infile]
infile.close()
print(listName1)
# print(listName)
t = ('a', 'b', 'c')
print(t)
# 交换数据
x, y = 5, 7
x, y = y, x
print(x, y)