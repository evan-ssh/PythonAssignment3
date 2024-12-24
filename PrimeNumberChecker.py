def main():
 while True:
    number = int(input("Enter Number: "))
    IsPrimeNumber(number)
    PrintFactors(number)
    go_again = input("Try another number?: ").lower()
    if go_again != "y":
        return False


def IsPrimeNumber(number):
    for numbers in range(2, number):
        if number % numbers == 0:
            print(f"{number} is NOT a prime number")
            break 
        else:
            print(f"{number} is a prime number")
            break

def PrintFactors(number):
    print("Factors")
    for numbers in range(1, number + 1):
        if number % numbers == 0:
            print(numbers)
           
main() 