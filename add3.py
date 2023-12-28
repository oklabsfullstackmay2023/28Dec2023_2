#1. Function Defination is one time process
def addFourNumber(*fa): # *fa are arbitary formalargument
    return fa[0] + fa[1] + fa[2] + fa[3]

#2. Function calling/invoking is many time process
result=addFourNumber(1.9,5.6,4.6,7.2) #sending float value(decimal) as actualargument
print(result)