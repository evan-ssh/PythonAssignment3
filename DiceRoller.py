import random
def main():
 die_one = 6
 #die_one = random.randint(0,6)
 print(f"Die 1:", die_one)
 die_two = 6
 #die_two = random.randint(0,6)
 print(f"Die 2:", die_two)
 total = die_one + die_two
 print(f"Total:", total)
 if die_one and die_two == 1:
  print("Snake Eyes")
 elif die_one and die_two == 6:
  print("Boxcars")
  

main()