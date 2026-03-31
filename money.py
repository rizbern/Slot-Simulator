class MoneyHandle:
    def deposit(self, amount, rem_balance, casino_balance, brokeCheck):
        print("How much money would you like to deposit?? (Go big or go home)")
        amount = int(input())
        if amount > rem_balance:
            print("You aint that rich bro, add a little less money")
            self.brokeCheck = 1
        else:
            casino_balance += amount   # add to casino
            rem_balance -= amount      # subtract from pocket

        return rem_balance, casino_balance, brokeCheck
    

    def withdraw(self, amount, rem_balance, casino_balance, brokeCheck):
        print("LOL!! QUIT ALREADY??? How much money brokie?")
        amount = int(input())
        if amount > casino_balance:
            print("Bro, you dont have that much money lol")
            self.brokeCheck = 1
        else:
            casino_balance -= amount   # subtract from casino
            rem_balance += amount      # add to pocket

        return rem_balance, casino_balance, brokeCheck