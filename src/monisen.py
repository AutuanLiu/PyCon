import math

def prime(num):
    # if or not 素数
    if num < 2:
    	return False
    elif num == 2:
    	return True
    bound = int(math.sqrt(num))
    for fac in range(2, bound + 1):
    	if num % fac == 0:
    		return False
    		break
    else:
    	return True

list1 = []
for num in range(2, int(5e3)):
	if prime(num):
		list1.append(num)
	else:
		continue

def monisen(no):
    count = 0
    for num in list1:
    	if prime(2 ** num - 1):
    		result = 2 ** num - 1
    		count += 1
    		if count == no:
    			break
    	else:
    		continue
    return  result

print(monisen(int(input("Enter the nth:"))))