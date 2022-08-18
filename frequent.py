def most_frequent(charValue):
    myDict={}
    for i in charValue:
        if i in myDict:
            myDict[i]+=1
        else:
            myDict[i]=1 

    des= sorted(myDict,key=myDict.get,reverse=True)
    for r in des:
        print(r+"="+str(myDict[r])+" ",end="")
    
most_frequent("Mississippi")