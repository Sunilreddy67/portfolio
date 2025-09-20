#discount
#amount>10000,15%
#amount>5000,10%
#amount>2000,5%
#amount<2000,0%
amount=1999.00
if amount>10000:
    discount=amount*0.15
elif amount>5000:
    discount=amount*0.1
elif amount>2000:
    discount=amount*0.05
else:
    discount=0
final_price=amount-discount
print(f"Amount={amount:.2f}")
print(f"Discount={discount:.2f}")
print(f"Final_price={final_price:.2f}")
#here amount is rupees(2000) and :.2f it will show with pices(.000)