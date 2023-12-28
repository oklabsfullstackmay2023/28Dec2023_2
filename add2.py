#1. Function Defination is one time process
def addThreeNumber(*fa):# *fa is a arbiatary formalargument
    return fa[0] + fa[1] + fa[2]

#2. Function calling/invoking is many time process
result=addThreeNumber(1,2,3) # sending float value(decimal) as actualargument
print(result)