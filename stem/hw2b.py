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
       fn2:   with x0=1, x1= 2, maxiter = 3 and xtol = 1e-8

       I observe that for functions 2 and 3, the answer should be pi/2 or about 1.57
    :return: nothing, just print results
    """
    r1 = Secant(fn1, 1, 2, 5,1e-4)
    r2 = Secant(fn2, 1,2,15, 1e-8)
    r3 = Secant(fn2,1,2,3,1e-8)
    print("root of fn1 = {root:0.4f}, after {iter :0d} iterations".format(root=r1[0], iter=r1[1]))
    #etc.
    pass
#endregion

if __name__=="__main__":
    main()