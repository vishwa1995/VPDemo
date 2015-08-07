a=raw_input("enter the temperature:")
a=int(a)
while True:
	if a>31 and a<35:
		print("sunny day")
		break
	elif a>35 and a<40:
		print("warm day")
		break
	elif a>40 and a<50:
		print("high temperature")
		break
	else:
		print("invalid")
