#consulted with ChatGPT and Jay Newfield to work through questions and bugs
#region imports
import Gauss_Elim as GE  # this is the module from lecture 2 that has useful matrix manipulation functions
from math import sqrt, pi, exp, cos
#endregion

#region function definitions
def Probability(PDF, args, c, GT=True):
    """
    This is the function to calculate the probability that x is >c or <c depending
    on the GT boolean.
    Step 1:  unpack args into mu and stDev
    Step 2:  compute lhl and rhl for Simpson
    Step 3:  package new tuple args1=(mu, stDev, lhl, rhl) to be passed to Simpson
    Step 4:  call Simpson with GNPDF and args1
    Step 5:  return probability
    :param PDF: the probability density function to be integrated
    :param args: a tuple with (mean, standard deviation)
    :param c: value for which we ask the probability question
    :param GT: boolean deciding if we want probability x>c (True) or x<c (False)
    :return: probability value
    """
    mu, sig = args
    lower_limit = mu - 5 * sig
    upper_limit = c
    integral = Simpson(PDF, (mu, sig, lower_limit, upper_limit)) #call the simpson function and arguments
    if GT:
        return 1 - integral
    else:
        return integral

def GPDF(args):
    """
    Here is where I will define the Gaussian probability density function.
    This requires knowing the population mean and standard deviation.
    To compute the GPDF at any value of x, I just need to compute as stated
    in the homework assignment.
    Step 1:  unpack the args tuple into variables called: x, mu, stDev
    Step 2:  compute GPDF value at x
    Step 3:  return value
    :param args: (x, mean, standard deviation)  tuple in that order
    :return: value of GPDF at the desired x
    """
    # Step 1: unpack args
    x, mu, sig = args
    # step 2: compute GPDF at x
    fx = (1 / (sig * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sig) ** 2)
    # step 3: return value
    return fx

def Simpson(fn, args, N=100):
    """
    This executes the Simpson 1/3 rule for numerical integration (see page 832, Table 19.4).
    As I recall:
    1. divide the range from x=lhl to x=rhl into an even number of parts. Perhaps 20?
    2. compute fx at each x value between lhl and rhl
    3. sum the even and odd values of fx as prescribed
    4. return the area beneath the function fx
    :param fn: some function of x to integrate
    :param args: a tuple containing (mean, stDev, lhl, rhl)
    :param N: number of subintervals (should be even to prevent incrementation)
    :return: the area beneath the function between lhl and rhl
    """
    mu, sig, a, b = args  #defines the arguments

    if N % 2 == 1:
        N += 1  # Ensure N is even
    h = (b - a) / N
    s = fn((a, mu, sig)) + fn((b, mu, sig))

    for i in range(1, N, 2):  # Odd indices
        s += 4 * fn((a + i * h, mu, sig))

    for i in range(2, N - 1, 2):  # Even indices
        s += 2 * fn((a + i * h, mu, sig))

    return (h / 3) * s #returns the integral


def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    This funciton implements th Secant method to find the root of an equation.  You should write your equation in a form
    fcn = 0 such that when the correct value of x is selected, the fcn actually equals zero (or very close to it).
    :param fcn: the function for which we want to find the root
    :param x0,x1: x values in neighborhood of root
    :param maxiter: exit if the number of iterations (new x values) equals this number
    :param xtol:  exit if the |xnewest - xprevious| < xtol
    :return: tuple with: (the final estimate of the root (most recent value of x), number of iterations)
    """
    for _ in range(maxiter):
        f0, f1 = fcn(x0), fcn(x1)

        if abs(f1 - f0) < 1e-12:  # Avoid division by zero
            print("Warning: Small denominator in Secant method.")
            return x1

        x_new = x1 - f1 * (x1 - x0) / (f1 - f0)  # Secant formula

        if abs(x_new - x1) < xtol:  # Convergence check
            return x_new

        # Update values for next iteration
        x0, x1 = x1, x_new

    return x1  # Return last computed value if maxiter is reached

def GaussSeidel(Aaug, x, Niter = 15):
    """
    This should implement the Gauss-Seidel method (see page 860, Tabl 20.2) for solving a system of equations.
    :param Aaug: The augmented matrix from Ax=b -> [A|b]
    :param x:  An initial guess for the x vector. if A is nxn, x is nx1
    :param Niter:  Number of iterations to run the GS method
    :return: the solution vector x
    """
    N = len(Aaug)

    for _ in range(Niter):
        for i in range(N):
            # Calculate the sum for the new x_i (excluding A[i, i] * x_i)
            sum_ax = 0
            for j in range(N):
                if j != i:
                    sum_ax += Aaug[i][j] * x[j]

            x[i] = (Aaug[i][N] - sum_ax) / Aaug[i][i]  # Solve for x[i]

    return x

def main():
    '''
    This is a function I created for testing the numerical methods locally.
    :return: None
    '''
    #region testing GPDF
    fx = GPDF((0,0,1))
    print("{:0.5f}".format(fx))  # Does this match the expected value?
    #edregion

    #region testing Simpson
    p=Simpson(GPDF,(0,1,-5,0)) # should return 0.5
    print("p={:0.5f}".format(p))  # Does this match the expected value?
    #endregion

    #region testing Probability
    p1 = Probability(GPDF, (0,1),0,True)
    print("p1={:0.5f}".format(p1))  # Does this match the expected value?
    #endregion


#endregion

#region function calls
if __name__ == '__main__':
    main()
#endregion