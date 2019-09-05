import random

s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "0123456789"
s3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s4 = "@#$%^&*()?"


l = random.randrange(1,5,1)
u = random.randrange(1,5,1)
n = random.randrange(1,5,1)
s = random.randrange(1,5,1)


p =  "".join(random.sample(s1,l ))
p =  p.join(random.sample(s2,u ))
p =  p.join(random.sample(s3,n ))
p =  p.join(random.sample(s4,s ))


print(p)


print("The number of lowercase : ")
print(l)
print("The number of uppercase : ")
print(u)
print("The number of numbers : ")
print(n)
print("The number of special : ")
print(s)

