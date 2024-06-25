def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

def celsius_to_kelvin(celsius):
    return celsius + 273

def kelvin_to_celsius(kelvin):
    return kelvin - 273

def fahrenheit_to_kelvin(fahrenheit):
    return ((5/9) * (fahrenheit - 32)) + 273

def kelvin_to_fahrenheit(kelvin):
    return ((9/5) * (kelvin - 273)) + 32

def main():
    while True:
        print("Temperature Converter")
        print("1: Celsius to fahrenheit")
        print("2: Fahrenheit to celsius")
        print("3: Celsius to Kelvin")
        print("4: Kelvin to celsius")
        print("5: fahrenheit to kelvin")
        print("6: Kelvin to fahrenheit")
        print("q: to quit")

        choice = input("Choice an option").strip().lower()

        if choice == "1":
            temp = float(input("Enter your temperature in celsius"))
            try:
                celsius = temp
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"your temperature is {fahrenheit} fahrenheit")
            except ValueError:
                print("Enter a valid number")

        elif choice == "2":
            temp = float(input("Enter your temperature in fahrenheit"))
            try:
                fahrenheit = temp
                celsius = fahrenheit_to_celsius(celsius)
                print(f"Your temperature is {celsius} celsius")
            except ValueError:
                print("Enter a valid number")
            
        elif choice == "3":
            temp = float(input("Enter your temperature in celsius"))
            try:
                celsius = temp
                kelvin = celsius_to_kelvin(celsius)
                print(f"your temperature is {kelvin} kelvin")
            except ValueError:
                print("Enter a valid number")

        elif choice == "4":
            temp = float(input("Enter your temperature in kelvin"))
            try:
                kelvin = temp
                celsius = kelvin_to_celsius(kelvin)
                print(f"your temperature is {celsius} celsius")
            except ValueError:
                print("Enter a valid number")

        if choice == "5":
            temp = float(input("Enter your temperature in fahrenheit"))
            try:
                fahrenheit = temp
                kelvin = fahrenheit_to_kelvin(fahrenheit)
                print(f"your temperature is {kelvin} kelvin")
            except ValueError:
                print("Enter a valid number")

        if choice == "6":
            temp = float(input("Enter your temperature in kelvin"))
            try:
                kelvin = temp
                fahrenheit = kelvin_to_fahrenheit(kelvin)
                print(f"your temperature is {fahrenheit} fahrenheit")
            except ValueError:
                print("Enter a valid number")

        elif choice == "q":
            break


        else:
            print("Enter a valid number")

        print()



if __name__ == "__main__":
    main()
