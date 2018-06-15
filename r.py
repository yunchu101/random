import random
start = input('決定隨機數字開始值')
end = input('決定隨機數字結束值')
start =  int(start)
end = int(end)
r = random.randint(start,end)
count = 0      
while True:
	count = count + 1
	num = input('what is the number?')
	num = int(num)
	if num > r:
		print('比這個小喔，再試一次！')
	elif num < r:
		print('比這個大唷，再試一次')
	elif num == r:
		print ('你答對了')
		print ('猜了',count, '次，得到正確答案')
		break
	print ('猜了',count, '次')

