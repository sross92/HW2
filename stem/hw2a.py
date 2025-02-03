#region imports
from math import sqrt, pi, exp
from NumericalMethods import GPDF, Simpson, Probability
#endregion

#region function definitions
def main():
    """
    I want to integrate the Gaussian probability density function between
    a left hand limit = (mean - 5*stDev) to a right hand limit = (c).  Here
    is my step-by-step plan:
    1. Decide mean, stDev, and c and if I want P(x>c) or P(x<c).
    2. Define args tuple and c to be passed to Probability
    3. Pass args, and a callback function (GPDF) to Probability
    4. In probability, pass along GPDF to Simpson along with the appropriate args tuple
    5. Return the required probability from Probability and print to screen.
    :return: Nothing to return, just print results to screen.
    """
    # Compute P(x < 105 | N(100,12.5))
    mu1, sigma1 = 100, 12.5
    c1 = 105
    prob1 = Probability(GPDF, (mu1, sigma1), c1, GT=False) #call probability function

    # Compute P(x > μ+2σ | N(100,3))
    mu2, sigma2 = 100, 3
    c2 = mu2 + 2 * sigma2  # 106
    prob2 = Probability(GPDF, (mu2, sigma2), c2, GT=True) #call probability function

    # Print the results in the required format
    print("P(x<{:.2f}|N({:.0f},{:.1f}))={:.2f}".format(c1, mu1, sigma1, prob1))
    print("P(x>{:.2f}|N({:.0f},{:.0f}))={:.2f}".format(c2, mu2, sigma2, prob2))

#endregion

if __name__ == "__main__":
    main()