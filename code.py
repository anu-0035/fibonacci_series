# fibonacci_series
#it is a series of sum of previous two consecutive no.
#program to print fibonacci series

#defining a function
def fib(n):
    a = 0
    b = 1
#using conditional statements
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
#using looping statements
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
n=int(input("enter till where you want the series"))
fib(n)
    
