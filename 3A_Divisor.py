def divisor(num):
    print("The divisors are : ")
    for i in range(num):
        if (num% (i+1))==0:
            print(i+1)

num=int(input("Enter a number : "))
divisor(num)
