def solveMeFirst(a,b):
	# Hint: Type return a+b below
    sum = int(a) + int(b)

    return sum


num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
res = solveMeFirst(num1,num2)
print('The sum of the two number is {}'.format(res))