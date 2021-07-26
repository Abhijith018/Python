def listFunction():
   
    listExample=['abcd',1,3,["ABcd",1]]
    l2=["testing"]
    print("Type",type(listExample))
    print("Lenght",len(listExample))
    print(listExample[3])
    print(listExample[3][1])
    print("Concatenation",listExample+l2)
    
    print("Spliting List",listExample[1:3])
    
    appendingList=listExample.append(l2)
    print("Appending",appendingList)
    
    print("Before deletion",listExample)
    del(listExample[0])
    print("After deletion",listExample)
    
    print("Extending",listExample.extend(["l2"]))
    
listFunction()

