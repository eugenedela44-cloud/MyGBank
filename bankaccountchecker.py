class Account_checker : 
    def __init__(self, full_name, dob,ID_number):
        self.full_name = full_name
        self.dob = dob
        self.id= ID_number
        self.balance = 0
        
        
        
        
    def deposit(self, amount):
        if amount<= 0:
            print("You have entered an invalid amount")
                
        else:
            self.balance += amount
            
            print(f"You have successfully deposited {amount}")
             
                
        
             
             
                 
    def withdraw(self, amount):
        if amount <=0:
            print("Invalid Amount")
                
        elif amount > self.balance:
            print("Insufficient amount")
                
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn {amount}")
            print(f"Your new balance is {self.balance}")      
     
    
    
    
    def check_balance(self):
        print(f"Your new balance is {self.balance}")


# my_acc.deposit(25000)
# my_acc.withdraw(250)
# my_acc.check_balance()
    def displayinfo(self):
        print("------ACCOUNT INFORMATION------")
        print()
        print(f"User Name: {self.full_name}")
        print(f"Date of Birth: {self.dob}")
        print(f"ID Card Number: {self.id}")
        print(f"Current Balance: {self.balance}")
              
# my_acc = Account_checker("Agbemade Eugene Dela","200007","21/08/2007","GHA1234567-8")        
# my_acc.deposit(20000000)
# my_acc.displayinfo()
print("------Welcome to MyGBank-------  ")
print()
name = input("Please enter your full name: ")
dob = input("Enter your date of birth(DD/MM/YYYY): ")
idnum =input("Enter your ID card number: ")
print()
print()


my_acc = Account_checker(name, dob, idnum)
print()
my_acc.displayinfo()
print()
print()
print("Account successfully created🎗🧨")
 
                    
                                          




                    
        
        
        
        
            
