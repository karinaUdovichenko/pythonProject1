x = int(input())
k = 0
s = ''
while x != 1:
	k = 0
	if (x% 2 ==0):
		x = x / 2
		s += '2'
		k +=1
	elif ( x % 3) == 0:
		x = x / 3
		s += '3'
		k += 1
	elif x % 5 == 0:
		x = x/5
		s += '5'
		k += 1
	elif x % 29 == 0:
		x = x /29
		s += '29'
		k += 1
	elif x % 869 == 0:
		x = x/869
		s += '869'
		k += 1
	if k == 0:
		print(0)
		break
if x == 1:
	print(s)
