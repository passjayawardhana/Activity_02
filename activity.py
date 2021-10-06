print ("Temperture Converter")

temp=(input("Enter the Temperature:"))
sing=input("Input 'F' for Fahrenheit or 'C' for Celsius:")

if sing == "F":
    temp = ((temp-32.00)*5.00/9.00)
    print ("Temperature in Celsius: ",temp, "C")
    
elif sing == "C":
    temp = ((temp*9.00/5.00)+32.00)
    print ("Temperature in Fahrenheit: ", temp, "F")
