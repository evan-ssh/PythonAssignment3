def main():
   print("Feet and Meteres Converter")
    
def conversionmenu():
   print("Conversions Menu:")
   print("a. Feet to Meters")
   print("b. Meters to feet")
   select_conversion = input("Select a conversion (a/b):").lower()
   if select_conversion == "a":
      Convertfeet()
   elif select_conversion == "b":
        ConvertMeters()
    
   


def Convertfeet():
 meters = float("Enter meters")
 feet = meters / 0.3048
 print(feet)

def ConvertMeters():
    feet = float("Enter feet")
    meters = feet * 0.3048
    print(meters)