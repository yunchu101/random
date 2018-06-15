import random

r = random.randint(1,100)      
while True:
	num = input('what is the number?')
	num = int(num)
	if num > r:
		print('比這個小喔，再試一次！')
	elif num < r:
		print('比這個大唷，再試一次')
	elif num == r:
		print ('你答對了')
		break


