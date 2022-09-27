#calculating price of each item
sum=0
print("PRESS Q TO QUIT")
while(True):
    itemprice=input("Enter the price of the item:\n")
    if (itemprice!='q'):
        sum= sum + int(itemprice)

    else:
        print(f"your total bill is:{sum}\nTHANKS VISIT AGAIN")
        break   




