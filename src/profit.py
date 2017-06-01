# evaluate the profit
costs = eval(input("Enter the total costs: "))
revenue = eval(input("Enter total revenue: "))
if costs == revenue:
	result = "Break even."
else:
	if costs < revenue:
		profit = revenue - costs
		result = "profit is ${0:,.2f}.".format(profit)
	else:
		loss = costs - revenue
		result = "Loss is ${0:,.2f}.".format(loss)
print(result)

# max value of list
num1 = eval(input("first number: "))
num2 = eval(input("second number: "))
if num1 > num2:
	print("the max value is:", num1)
elif num2 > num1:
	print("the max value is:", num2)
else:
	print("the two numbers are equal.")
