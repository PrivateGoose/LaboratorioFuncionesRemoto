def is_prime(number):

        try:
            counter = 0
            for i in range(1,number+1):
                if (number% i)==0:
                    counter = counter + 1
            if counter==2:
                print ("1")
            else:
                print ("0")
        except:
            print("-1")

counter = 0
counterprime = 0

while True:
    a=int(input("Type a number to check if it is a prime number, if you wish to proceed, press any number, if you do not want to proceed, press a number equal or less than 0: "))
    if a<0:
        print("Program finalized")
        print("The number of times you got a prime number is: {}".format(counter))
        print("The quantity of primes number you got is also a prime number: {}".format(counterprime))
        break
    else:
        if a > 0:
            counter= counter + 1
            counterprime=(counter%2!=0)
            number=int(input("Type your number: "))
            print(is_prime(number))
