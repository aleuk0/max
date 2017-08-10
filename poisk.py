def guess_number():
	a, b, n = 1000000, 1, 0
	# n - количество итераций
	while True:
		x = input("Number < " + str(round((a+b)/2, 2)) + "?")
		# округления позволяют скорее найти нужное число + выглядит лучше
		if x == 'yes':
			a = (a+b)/2
			n += 1
			if round(a)==round(b):
				print("Your number is ", round(a))
				input()
				break
		elif x == 'no':
			b = (a+b)/2
			n += 1
			if round(a)==round(b):
				print("Your number is ", round(a))
				input()
				break
		else:
			input("You are wrong")
			break

input("I can guess your number from 1 to 1000000. Let's play!")
guess_number()


'''
Далее приведен базовый алгоритм, на вход функция
	принимает число, которое необходимо найти:
def s(x):
	a, b, n = 1000000, 1, 0
	# n - количество итераций
	while True:
		if x < (a+b)/2:
			a = (a+b)/2
			n += 1
			print(a)
		elif x > (a+b)/2:
			b = (a+b)/2
			n += 1
		else: break
'''
