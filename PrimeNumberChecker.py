def main():
    number = int(input("Enter Number: "))
    for numbers in range(2, number):
        if number % numbers == 0:
            print("Number is not a prime number")
            break
        else:
            print("Number is a prime number")
main()