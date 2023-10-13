def bonAppetit(bill, k, b):
    # Calculate the total that Anna should pay
    bill_ana_should_pay = (sum(bill) - bill[k]) // 2
    
    # Check whether Brian overcharged Anna
    if b == bill_ana_should_pay:
        print("Bon Appetit")
    else:
        print(b - bill_ana_should_pay)