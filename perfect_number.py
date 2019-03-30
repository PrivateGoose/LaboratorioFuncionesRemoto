def perfect_number(n):
    a=0
    for i in range(1,n):
        if(n%i==0):
            a+=i
    if (a==n):
        print("The number you have typed is a perfect number.")
    else:
        print("The number you have typed is not a perfect number.")
    if ((a==(n-3) or a==(n+3))):
            print("The number you have typed isn´t an almost perfect number")
    else:
        print("The number you have typed is an almost perfect number")

n=int(input("Number to evaluate: "))
perfect_number(n)