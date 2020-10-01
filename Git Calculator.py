import re

print("My beautiful Calculator")
print("Type Quit to Finish")

previous = 0
run = True

def performMath():
    global run
    global pre
    equation =""
    if pre==0:
        equation=input("Enter The Equation")
    else:
        equation=input(str(pre))    
    if equation == 'quit':
        print("Goodbye")
        run = False

    else:
        equation = re.sub('[a-zA-Z,.:()" "]'," ",equation)
        if pre ==0:
            pre = eval(equation)
        else:
            pre = eval(str(pre) + equation)    
       

while run:
    #it will run again and again
    performMath()
