num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    

if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    addition = round(num1 + num2, 2)
    subtraction = round(num1 - num2, 2)
    multiplication = round(num1 * num2, 2)
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

    print(f"{'Operation' :<20}{'Result' :>10}")
    print("-" * 30)
    print(f"{'Addition' :<20}{addition :>10}")
    print(f"{'Subtraction' :<20}{subtraction :>10}")
    print(f"{'Multiplication' :<20}{multiplication :>10}")
    print(f"{'Division' :<20}{division :>10}")
    print(f"{'Floor Division' :<20}{floor_division :>10}")
    print(f"{'Modulus' :<20}{modulus :>10}")