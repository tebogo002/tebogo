account_balance = float(1000.00)  # Initial account balance

def check_balance():
    print(f"Welcome, Your current account balance is: R{account_balance:.2f}")   

request_amount = float(input("Enter the amount you want to withdraw: R"))

if (request_amount <= account_balance) and (request_amount != 0) and (request_amount > 0):
    account_balance = account_balance - request_amount
    print(f"Withdrawal successful. Your new account balance is: R{round(account_balance, 2)}") 
elif request_amount <= 0:       
    print("Invalid amount. Please enter a valid amount.")
else:
    print("Withdrawal amount exceeds account balance. Transaction denied.") 
    print(f"Your current account balance is: R{account_balance:.2f}")  