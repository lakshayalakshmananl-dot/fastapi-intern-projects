def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def celsius_to_kelvin(c):
    return c + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = input("Enter your choice (1-4): ")

temperature = float(input("Enter temperature: "))


if choice == "1":
    print("Converted Temperature:", celsius_to_fahrenheit(temperature))

elif choice == "2":
    print("Converted Temperature:", fahrenheit_to_celsius(temperature))

elif choice == "3":
    print("Converted Temperature:", celsius_to_kelvin(temperature))

elif choice == "4":
    print("Converted Temperature:", kelvin_to_celsius(temperature))

else:
    print("Invalid choice")