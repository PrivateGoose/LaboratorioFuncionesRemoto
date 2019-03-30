def is_prime():
 
    number=int(input("Type a number to check if it is prime or not: "))

    counter = 0
    for i in range(1,number+1):
        if (number% i)==0:
            counter = counter + 1
    if counter==2:
        print ("The number you typed: {} is a prime number".format(number))
    else:
        print ("The number you typed: {} is not a prime number.".format(number))

is_prime()