from ast import main


def factorial(number):
  if number==0 or number==1:
    return 1
  else:
    return number*factorial(number-1)

def trailing(number):
    count=0
    i=5
    while(number//i!=0):
        count=count+int(number/i)
        i=i*5
    return count
if __name__=="__main__":
 num=int(input("enter the number:\n"))
 fac=factorial(num)
 zero=trailing(num)
 print(f"factorial={fac}\ntrailingzero={zero}\n")

  

    