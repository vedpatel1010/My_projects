item = str(input("what whould you like to buy today? \nHere is the list: Ammonia , HCL , Nitric Acid:"))
if item == "Ammonia":
    print("The price of ammonia is 40 rupess per litre")
    quantity1 = float(input("How many litres you need? "))
    total1 = quantity1 * 40
    print(f"Your total is {total1}")
elif item == "HCL":
    print("The price of HCL is 60 rupess per litre")
    quantity2 = float(input("How many litres you need? "))
    total2 = quantity2 * 60
    print(f"Your total is {total2}")
elif item == "Nitric Acid":
    print("The price of Nitric Acid is 70 rupess per litre")
    quantity3 = float(input("How many litres you need? "))
    total3 = quantity3 * 70
    print(f"Your total is {total3}")
