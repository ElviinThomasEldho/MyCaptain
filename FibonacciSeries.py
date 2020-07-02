print("Fibonacci Series :-")
n = int(input("Enter number of elements to be displayed : "))

a=0
b=1

if (n==1):
    print(a)
else if (n==2):
    print(a)   
    print(b)    
else:
    print(a)   
    print(b)   
    n-=2
    while(n!=0):
        s=a+b
        a=b
        b=s
        print(b)
        n-=1
    

