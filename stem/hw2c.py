#consulted with ChatGPT, Jay Newfield, and Brian Nguyen to work through questions and bugs

#import region
from copy import deepcopy #from copy imports deepcopy for use
from NumericalMethods import GaussSeidel #imports GaussSeidel for use
#endregion
def solve_linear_system(Aaug, initial_guess, iterations=15):

    """
    Uses the Gauss-Seidel method to approximate the solution of a linear system.

    Parameters:
    Aaug: Augmented matrix [A | b] representing the system.
    initial_guess: Starting values for the solution vector.
    iterations: Number of iterations to execute (default: 15).

    Returns:
    list of floats: The computed solution vector after the given iterations.
    """

    return GaussSeidel(deepcopy(Aaug), deepcopy(initial_guess), iterations)

def main():
    pass

if __name__=="__main":
    main()