
sum=0

while(True):
    item=input()
 
    if(item!='q'):
        sum=sum+int(item)
    else:
        print(f"   PRICE\n{item}    \ntotal is{sum}")
        break