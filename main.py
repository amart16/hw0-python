# Author: Alex Martin arm6554@psu.edu
temp=float(input("Enter temperature: "))
f=(temp*1.8)+32
c=(temp-32)/1.8

unit=input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  print(f"{temp}° in Fahrenheit is equivalent to {c}° Celsius.")
elif unit == "C" or unit == "c":
  print(f"{temp}° in Celsius is equivalent to {f}° Fahrenheit.")
else:
    print(f"Invalid unit({unit}).")
  
