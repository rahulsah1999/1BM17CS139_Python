lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) 
      
print(lst)

evenlst = []
for i in range(0, len(lst)):
    if lst[i]%2 == 0:
     
     evenlst.append(lst[i])


print("Even number list is:")
print(evenlst)
