def hotel():
    print("REGENCY HOTEL")
    food=input("Enter your order:")
    qnt=int(input("Enter quantity:"))
    if food=="dosa":
        rate=30.00
    elif food=="idly":
        rate=25.00
    elif food=="pongal":
        rate=40.00
    elif food=="poori":
        rate=35.00
    elif food=="coffee":
        rate=20.00
    Total_bill =qnt*rate
    print("Food:",food)
    print("Quantity:",qnt)
    print(f"Total Bill: {Total_bill:.2f}")
      
