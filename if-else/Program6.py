# Accept the marked price from the user and calculate
# the Net amount as (Marked Price – Discount) to pay
# according to following criteria:

# Marked Price Discount
# >10000 20%
# >7000 and <=10000 15%
# <=7000 10%

marked_price = float(input("Enter the market price : "))

discount = 0

if marked_price > 10000:
    discount = 0.20
elif marked_price > 7000 and marked_price <= 10000:
    discount = 0.15
else:
    discount = 0.10
    
discount_amount = marked_price * discount

net_amount = marked_price - discount_amount

print("The net amount to pay is : ", net_amount)