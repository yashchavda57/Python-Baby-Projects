import re



def performMath():
    global run
    global previous
    equation =""
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
       

    
if __main__(self):
    print("Our Magical Calculator")
    print("Type Quit to Exit")
    previous = 0
    run = True
    while run:
        performMath()
