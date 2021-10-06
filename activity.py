print ("Temperture Converter")

tem=(input("Enter the Temperature:"))
sing=input("Input 'F' for Fahrenheit or 'C' for Celsius:")

if sing == "F":
    tem = ((tem-32.00)*5.00/9.00)
    print ("Temperature in Celsius: ",tem, "C")
    
elif sing == "C":
    tem = ((tem*9.00/5.00)+32.00)
    print ("Temperature in Fahrenheit: ", tem, "F")
