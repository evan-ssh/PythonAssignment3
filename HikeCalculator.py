def main():
    print("Hike calculator")
    miles_walked = float(input("How many miles did you walk?: "))
    convert_miles(miles_walked)


def convert_miles(miles_walked):
 feet = miles_walked * 5280
 print(f"You walked {feet} feet.")

if __name__ == "__main__":
   main()