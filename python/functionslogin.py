def login(user="unknown",passwd =000):
	print(user,passwd)

try :
	a =str(input("username"))
	b =int(input("passwd"))
	login(a,b)
except ValueError as e :
	print("invalid",e)
