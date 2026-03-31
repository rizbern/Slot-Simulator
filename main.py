# from selector import Selector
from money import MoneyHandle
mh = MoneyHandle()
money_in_pocket = 10000
casino_balance = 0
brokeCheckmain = 0

print(" -------------------------------------------------------------------")
print("| WELCOME TO SLOT MACHINE SIMULATOR, READY TO MAKE SOME REAL MONEY? |")
print(" -------------------------------------------------------------------")

rules = """
1. The house always wins… unless you accidentally unplug it.
2. Coins inserted are non-refundable, emotionally and financially.
3. If you win big, it’s skill. If you lose, it’s “part of the experience.”
4. Button mashing does not increase your luck—but it does improve your cardio.
5. Talking nicely to the machine may improve morale, but not outcomes.
6. Any resemblance between “almost winning” and actual winning is purely psychological.
7. Celebratory dances are encouraged, even if you lose. Especially if you lose.
8. The jackpot exists… we think.
9. Blaming the machine is allowed, blaming the rules is expected.
10. Remember: you’re not losing money, you’re investing in entertainment.
"""

print(f"Rules:\n{rules}")
# alt + click to select multiple lines
while 1:
    ans = int(input("To deposit money click 1\nTo place a bet click 2\nTo withdraw all your money click 3\n"))
    print(f"ans: {ans}")
    if ans == 1:
        money_in_pocket, casino_balance, brokeCheckmain = mh.deposit(0, money_in_pocket, casino_balance, brokeCheckmain) # returns your casino balance
        if brokeCheckmain == 1:
            print("WOW!!! youre bad with maths too, try again lol")
        else:
            print(f"CASINo {casino_balance}         packoettt: {money_in_pocket}")
    elif ans == 3:
        money_in_pocket, casino_balance, brokeCheck = mh.withdraw(0, money_in_pocket, casino_balance, brokeCheckmain)
        if brokeCheckmain == 1:
            print("WOW!!! youre bad with maths too, try again lol")
        else:
            print(f"CASINo {casino_balance}         packoettt: {money_in_pocket}")