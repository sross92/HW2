#consulted with ChatGPT and Jay Newfield to work through questions and bugs
#region imports
from NumericalMethods import Secant
from math import sqrt, pi, exp, cos
#endregion

#region function definitions
def fn1(x):
    """ Function 1: x - 3cos(x) """
    return x - 3 * cos(x)

def fn2(x):
    """ Function 2: cos(2x) * x^3 """
    return cos(2 * x) * x ** 3

def main():
    """
       fn1:  x-3cos(x)=0; with x0=1, x1= 2, maxiter = 5 and xtol = 1e-4
       fn2:  cos(2x)*x**3; with x0=1, x1= 2, maxiter = 15 and xtol = 1e-8
       fn2:  cos(2x) * x^3; with x0=1, x1= 2, maxiter = 3 and xtol = 1e-8


    :return: nothing, just print results
    """
    r1 = Secant(fn1,1, 2, 5,1e-4) #calls Secant with the argument values listed being used
    r2 = Secant(fn2, 1,2,15, 1e-8) #calls Secant with the argument values listed being used
    r3 = Secant(fn2,1,2,3,1e-8) #calls Secant with the argument values listed being used
    print("Root of fn1 = {:.4f}".format(r1))
    print("Root of fn2 (maxiter=15) = {:.4f}".format(r2))
    print("Root of fn2 (maxiter=3) = {:.4f}".format(r3))

#endregion

if __name__=="__main__":
    main()