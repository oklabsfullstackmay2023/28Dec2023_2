#1. Function Defination is one time process
def myFunction(x,y,z):
    return x + y + z
    
#2. Function Calling/Invoking is many time process
result=myFunction(y=5.2,z=4.5,x=9.2)
print(result)