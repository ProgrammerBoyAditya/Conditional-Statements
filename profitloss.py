actual_cost = float(input("Please enter the actual product price"))
sale_cost = float(input("Please enter the sales amount"))
if sale_cost > actual_cost :
    amount = sale_cost - actual_cost
    print("Total profit is = {0}".format(amount))
          
else :
    print("NO PROFIT!!!")