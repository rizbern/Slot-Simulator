import random

class Selector:
    def __init__(self):
        print("Initializing Slot machine...")
    
    def play(self, winCheck: int, res: list):
        # returns winCheck ->0, 1 and result-> numbers
        self.num1 = random.randint(1,5)
        self.num2 = random.randint(1,5)
        self.num3 = random.randint(1,5)

        print(f"Number 1: {self.num1}\tNumber 2: {self.num2}\tNumber 3: {self.num3}") 
        if self.num1 == self.num2 == self.num3:
            print("Congratulations, you won...")
            self.winCheck = 1
            self.res = [self.num1, self.num2, self.num3]
        else:
            self.res = [self.num1, self.num2, self.num3]

        return winCheck, self.res





result: Selector = Selector()
winCheck, resultNumbers = result.play(0,[])
