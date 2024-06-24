x=["sathya","kani"]
y=["2000","1999"]
def checkbalance():
    return a
def deposit():
    print("enter your amount to deposit:")
    e=int(input())
    print("your amount is deposit successfully")
    print("your total amount is ",a+e)
def widhraw():
    print("enter your amount to widhraw:")
    f=int(input())
    print("your amount is widhraw successfully")
    print("your total amount is ",a-f)
def options():
    print("please choose your process to continue:")
    print("\n1.check balance\n2.deposit\n3.widhraw")
    o=int(input("select:"))
    if(o==1):
        print(checkbalance())
    elif(o==2):
        deposit()
    elif(o==3):
        widhraw()
    else:
        print("invalid option")
n=input("name:")
c=input("code:")
if(n==x[0] and c==y[0]):
    a=10000
    print("welcome",n)
    options()
elif(n==x[1] and c==y[1]):
    a=20000
    print("welcome",n)
    options()
else:
    print("invalid name and code")






