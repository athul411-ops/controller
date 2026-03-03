class overheaterror(Exception) :
	pass

try:
	a = int(input("what temp"))
	if a > 50 :
	
		raise overheaterror("overheat")
except overheaterror as e :
	print("rror",e)
except ValueError as e :
	print("Builtin error:",e)
else :
	print(a)
finally :
	print("Done")
