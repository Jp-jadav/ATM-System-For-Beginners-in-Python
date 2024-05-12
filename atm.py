class Atm:
	def __init__(self,account_no,name,number,age,bal=0):
		self.account_no = account_no
		self.balance= bal
		self.name = name
		self.number = number
		self.age = age

# Account Holder Method
	def account_details(self):
		print("Account number: ",self.account_no)
		print("Holder Name	 : ",self.name)
		print("Holder age    : ",self.age)
		print("Holder Mo_No  : ",self.number)

# Check Balance Method
	def checkBalance(self):
		print("Total balance :--",self.balance)

# Add amount Method
	def credit(self,amount):
		self.balance = self.balance + amount
		print("Rs.", amount, "was debited.")
		
# remove amount method
	def debit(self,amount):
		if self.balance < amount :
			print("Your avalable balance is low")
		else:
			self.balance = self.balance - amount
		print("Rs.", amount, "was credited.")
			

account_no = 12345
while True:	
	user_no = int(input("enter your acount no:---"))
	if account_no == user_no:
		u_name = input("Enter name:--")
		u_no = int(input("Enter no:--"))
		u_age = int(input("age is:--"))
		add_bal = int(input("add bal:--"))

		while True:

			obj = Atm(account_no,u_name,u_no,u_age,add_bal)
			uc = int(input('''
		0. Account Details.			
		1. Check Bank Balance.
		2. Add Amount. 
		3. widrow Amount.
		4. Log out
				'''))

			if uc == 1:
				obj.checkBalance()
			elif uc == 2:
				ad = int(input("add amount:--"))
				obj.credit(ad)
			elif uc == 3:
				wid = int(input("widraw amount:--"))
				obj.debit(wid)
			elif uc == 0:
				obj.account_details()
			else:
				print("account logout...\nPlease again")
				break
	else:
		print("Not Avalable account")
	