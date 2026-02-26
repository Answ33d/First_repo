item=input("Product name:")
quantity=int(input("quantity: "))
price=float(input("Price"))
discount=float(input("Discount in %"))

print(f"You bought {quantity} {item.upper()} for {price*quantity} USD . Your discount is {discount}% . To pay {(price-(price/100*discount))*quantity}")