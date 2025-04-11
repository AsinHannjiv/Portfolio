#Write a code to convert Fahrenheit to Celsius; vice versa

#Make a welcome message including my name
print("Welcome to Marques' Temperature Converter")

#Ask for the temperature
fTemp = float(input("What is the temperature?"))

#Find out if it is Fahrenheit or Celsius
sUnit = input("Is the temperature you entered Fahrenheit (F) or Celsius (C)?")

#Convert Temp; If certain conditions are not met, issue error message and end program there
if (sUnit == "F" or sUnit == "f") and fTemp > 212:
    print("Temp can not be > 212")
elif sUnit == "F" or sUnit == "f":
    fCelsius = (5.0/9) * (fTemp - 32)
    print("The Celsius equivalent is:", format(fCelsius, ",.1f"))
elif (sUnit == "C" or sUnit == "c") and fTemp > 100:
    print("Temp can not be > 100")
elif sUnit == "C" or sUnit == "c":
    fFahrenheit = ((9.0/5.0) * fTemp + 32)
    print("The Fahrenheit equivalent is:", format(fFahrenheit, ',.1f'))
else:
    print("You have to enter a F or C")