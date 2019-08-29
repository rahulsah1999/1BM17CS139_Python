def lin_search(lis):
    a = int(input("Enter the number to search : "))
    for i in lis:
        if a in lis:
            print("The element is present at position : ",lis.index(a)+1)
            break;

        elif i==len(lis)-1 and a not in lis:
            print("The element is not present in the list")

            
N = int(input("Enter the number of elements in the list : "))
lis = []
for x in range(N):
        print("Enter number ", x+1, " : ")
        element = int(input())
        lis.append(element)
lin_search(lis)
