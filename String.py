def myFirstProgram():
    name="Myname"
    name=name.upper()
    name=name.replace("MY", "Your")
    
    print("Hello World")
    print(name)
    print(name.find("NAME"))
    print(type(name))
    tupleExample=('disco',1,3,("ABcd",1))
    print(type(tupleExample))
    print(len(tupleExample))
    print(tupleExample[3])
    
myFirstProgram()