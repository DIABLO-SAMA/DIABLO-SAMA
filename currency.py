#currency converter
with open('currency.txt')as f:
    lines=f.readlines()

curedict={}
for line in lines:
    passed=line.split("\t")
    curedict[passed[0]] = passed[1]

amount=int(input("Enter the amount in rupees:\n"))
print("****ALL THE AVALAIBLE OPTIONS ARE***\n")
[print(item) for item in curedict.keys()]
currency=input("CHOOSE UR OPTION:\n")
er=amount*float(curedict[currency])
print(f("{amount} rupees = {er}   {currency}"))
