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
    """
    Main function to solve and print the solutions of the linear equations
    using the Gauss-Seidel method.
    """

    # First system of equations:
    Aaug1 = [[3, 1, -1, 2],[1, 4, 1, 12],[2, 2, 1, 10]]
    x1 = [0, 0, 0]  # Starting with a zero vector

    sol1 = solve_linear_system(Aaug1, x1)
    print("Solution for the first system is:")
    for i, val in enumerate(sol1, start=1):
        print(f"x{i} = {val:.4f}")
    print()

    # Second system of equations:
    Aaug2 = [[1, -10, 2, 4, 2],[3, 1, 4, 12, 12],[9, 2, 3, 4, 21],[-1, 2, 7, 3, 37]]
    x2 = [0, 0, 0, 0]  # Starting with a zero vector

    sol2 = solve_linear_system(Aaug2, x2)
    print("Solution for the second system is:")
    for i, val in enumerate(sol2, start=1):
        print(f"x{i} = {val:.4f}")

if __name__ == "__main__":
    main()