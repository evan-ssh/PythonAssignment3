def main():
 while True:
    print("Even or Odd checker")
    user_number = int(input("Enter an integer: "))
    if user_number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")
    go_again = input("Continue? (y/n)")
    if go_again != 'y':
       return False
main()



