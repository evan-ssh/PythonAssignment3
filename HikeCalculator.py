def main():
 while True:
    print("Hike calculator")
    miles_walked = float(input("How many miles did you walk?: "))
    convert_miles(miles_walked)

    go_again = input("Another conversion? (y/n)")
    if go_again != 'y':
      return False
      


def convert_miles(miles_walked):
 feet = miles_walked * 5280
 print(f"You walked {feet} feet.")

if __name__ == "__main__":
   main()