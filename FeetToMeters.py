def main():
 
   print("Feet and Meteres Converter")
   conversionmenu()
 
    
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
   feet = float(input("Enter feet"))
   meters = feet * 0.3048
   print(f"{meters:.2f} meters")


def ConvertMeters():
   meters = float(input("Enter meters"))
   feet = meters / 0.3048
   print(f"{feet:.2f} feet")

main()