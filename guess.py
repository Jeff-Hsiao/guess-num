import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	guess = input('請猜數字: ')
	guess = int(guess)
	if guess == r:
		print('猜對了!!!')
		print('這是你猜的第', count, '次')
		break
	elif guess > r:
		print('比答案大')
	elif guess < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
