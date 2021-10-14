import random

class Account:
    # Construct an Account object
    def __init__(self, id, balance=0, annualInterestRate=3.4):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()

def main():
        # Creating accounts
        accounts = []
        for i in range(1000, 9999):
            account = Account(i, 0)
            accounts.append(account)

        # ATM Processes
        while True:
            try:
                # Reading id from user
                id = int(input("\nEnter account pin: "))
            except ValueError:
                print("Please enter an Integer Value.")
                continue

            # Loop still id is valid
            while id < 1000 or id > 9999:
                id = int(input("\nInvalid Id.. Re-enter: "))

            # Iterating over account session
            while True:

                # Printing menu
                print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
                try:
                # Reading selection
                    selection = int(input("\nEnter your selection: "))
                except ValueError:
                    print("Please enter an Integer Value.")
                    continue

                # Getting account object
                for acc in accounts:
                    # Comparing account id
                    if acc.getId() == id:
                        accountObj = acc
                        break

                # View Balance
                if selection == 1:
                    # Printing balance
                    print(accountObj.getBalance())

                # Withdraw
                elif selection == 2:
                    # Reading amount
                    amt = float(input("\nEnter amount to withdraw: "))
                    ver_withdraw = input("Is this the correct amount, yes or no ? " + str(amt) + " ")

                    if ver_withdraw == "yes":
                        print("Verify withdraw")
                    else:
                        break

                    if amt < accountObj.getBalance():
                        # Calling withdraw method
                        accountObj.withdraw(amt)
                        # Printing updated balance
                        print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
                    else:
                        print("\nYou're balance is less than withdrawl amount: " + str(
                        accountObj.getBalance()) + " n")
                        print("\nPlease make a deposit.")

                # Deposit
                elif selection == 3:
                        # Reading amount
                        amt = float(input("\nEnter amount to deposit: "))
                        ver_deposit = input("Is this the correct amount, yes, or no ? " + str(amt) + " ")

                        if ver_deposit == "yes":
                            # Calling deposit method
                            accountObj.deposit(amt)
                            # Printing updated balance
                            print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
                        else:
                            break

                elif selection == 4:
                    print("\nTransaction is now complete.")
                    print("________________________________________")
                    print("Transaction number: ", random.randint(10000, 1000000))
                    print("________________________________________")
                    print("Current Interest Rate: ", accountObj.annualInterestRate)
                    print("________________________________________")
                    print("Monthly Interest Rate: ", accountObj.annualInterestRate / 12)
                    print("________________________________________")
                    print("Thanks for choosing us as your bank.")
                    exit()

                # Any other choice
                else:
                    print("\nThat's an invalid choice.")

    #Main function
main()