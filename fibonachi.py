while True:
    try:
        theinputvalue = int(input('Write the income number of "Fibonachi": '))
    except ValueError:
        print('ERROR:the value is not integer')
        continue
    if theinputvalue <= 0:
        print('ERROR: incorrect input')
    elif theinputvalue < 2:
        print('The "Fibonachi" number is : ' + str(theinputvalue))
    else :
        thevariableforloop: int = 2
        fibonaccisequensarray = [0, 1, 1]
        while thevariableforloop <= theinputvalue:
            fibonaccisequensarray[2] = fibonaccisequensarray[0] + fibonaccisequensarray[1]
            fibonaccisequensarray[0] = fibonaccisequensarray[1]
            fibonaccisequensarray[1] = fibonaccisequensarray[2]
            thevariableforloop += 1
        print('The "Fibonachi" number is : ' + str(fibonaccisequensarray[2]))
