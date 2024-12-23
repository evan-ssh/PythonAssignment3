import random
def main():
 while True:
    die_one = RollDiceOne()
    die_two = RollDiceTwo()
    total = Total(die_one, die_two)
    print(f"Die 1:", die_one)
    print(f"Die 2:", die_two)
    print(f"Total:", total)
    if die_one == 1 and die_two == 1:
     print("Snake Eyes")
    elif die_one == 6 and die_two == 6:
     print("Boxcars")
    go_again = input("Roll Again? (y/n)")
    if go_again != "y":
     return False
def RollDiceOne():
 die_one = random.randint(0,6)
 return die_one
def RollDiceTwo():
 die_two = random.randint(0,6)
 return die_two
def Total(die_one,die_two):
 total = die_one + die_two
 return total
main()