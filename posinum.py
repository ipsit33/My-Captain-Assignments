list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]

i=0
print("For LIST 1: ")
while i < len(list1):
    if (list1[i] > 0):
        print(str(list1[i])+" ",end="")       

    i+=1

print("\nFor LIST 2: ")
i=0
while(i < len(list2)):
    if(list2[i] < 0):
        list2.pop(i)
    i+=1
print(str(list2))