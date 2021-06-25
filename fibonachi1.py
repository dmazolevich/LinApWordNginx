while True:
    n = int(input('Write the income number of "Fibonachi": '))
    if n < 2:
        print('The "Fibonachi" number is : ' + str(n))
    else :
        i = 2
        fib = [0, 1, 1]
        while i <= n :
            fib[2] = fib[0] + fib[1]
            fib[0] = fib[1]
            fib[1] = fib[2]
            i += 1
        print('The "Fibonachi" number is : ' + str(fib[2]))
