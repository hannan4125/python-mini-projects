def convert_temperature(choice,temp):
    
    if choice == "C":
        to_f = (temp * 9/5) + 32      # Celsius → Fahrenheit
        to_k = temp + 273.15          # Celsius → Kelvin
        return f"{temp}°C is {to_f:.2f}°F and {to_k:.2f}K"

    elif choice == "F":
        to_c = (temp - 32) * 5/9      # Fahrenheit → Celsius
        to_k = (temp - 32) * 5/9 + 273.15  # Fahrenheit → Kelvin
        return f"{temp}°F is {to_c:.2f}°C and {to_k:.2f}K"

    elif choice == "K":
        to_c = temp - 273.15          # Kelvin → Celsius
        to_f = (temp - 273.15) * 9/5 + 32  # Kelvin → Fahrenheit
        return f"{temp}K is {to_c:.2f}°C and {to_f:.2f}°F"

while True:
    
    choice = input("Convert from (C/F/K) or type 'exit' to quit: ").upper()
    
    if choice == "EXIT":
        print("Goodbye!")
        break
    
    if choice not in ['C','F','K']:
        print("❌ Invalid choice! Please enter C, F or K.")
        continue
    
    try:
        temp = float(input("Enter temperature: "))
    except ValueError:
        print("❌ Invalid number! Please enter a valid numeric value.")
        continue    

    print(convert_temperature(choice,temp))
