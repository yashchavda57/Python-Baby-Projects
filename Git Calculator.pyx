import re

print("Our Magical Calculator")
print("Type Quit to Exit")

cdef int previous = 0
def bool run = True

def performMath():
    cdef bool global run
    cdef int global previous
    cdef str equation =""
    if previous==0:
        equation=input("Enter Equation")
    else:
        equation=input(str(previous))    
    if equation == 'quit':
        print("Goodbye , Amigo!!")
        run = False

    else:
        equation = re.sub('[a-zA-Z,.:()" "]'," ",equation)
        if previous ==0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)    
       

while run:
    performMath()