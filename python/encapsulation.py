class BankAccount:

	def __init__(self):
		self.name ="athul"
		self._balance  =0
		self.__pin = 1234
	def deposit(self,amount):
		self._balance +=amount
		print(self._balance)
	
	def withdraw(self,amount,pin):
		if self.__pin == pin:
			self._balance -=amount
			print(self._balance)
		else :
			print("auth failed")


test = BankAccount()

test.deposit(3000)
test.withdraw(100,1234)
