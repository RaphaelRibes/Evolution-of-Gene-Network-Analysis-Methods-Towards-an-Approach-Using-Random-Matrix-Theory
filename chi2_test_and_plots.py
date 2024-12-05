import numpy as np
from scipy.interpolate import UnivariateSpline
from scipy.stats import chi2
import matplotlib.pyplot as plt


# Example usage
if __name__ == '__main__':
    # Generate sample eigenvalues for testing
    N = 10000
    lambdas = np.random.normal(loc=0, scale=1, size=N)
    lambdas.sort()

    N_lambda = np.arange(1, N + 1)  # Integrated density N(λ_i) = i

    # Create the spline with smoothing
    spline = UnivariateSpline(lambdas, N_lambda, s=N, k=3)

    # Compute N_av(λ_i)
    e_i = spline(lambdas)

    # Compute the NNDS
    s = np.diff(e_i)

    # Khi² test, compute the expected spacings
    x = np.linspace(0.5, 5, 50)
    # Compute the histogram of spacings
    p_s, bin_edges = np.histogram(s, bins=50, density=True)
    s = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    poisson = np.exp(-s)

    # Compute the chi-squared statistic
    chi2_stat = np.sum((p_s - poisson) ** 2 / poisson)
    print(f"{chi2_stat:.2f} < {chi2.ppf(0.99, 1):.2f} so H0 is accepted")

    # Create the plot
    plt.figure(figsize=(10, 5))

    x = np.linspace(0, 5, counts.size)
    wingner_dyson = ((np.pi * bin_centers) / 2) * np.exp(-(np.pi * bin_centers ** 2) / 4)
    poisson = np.exp(-bin_centers)

    plt.plot(x, wingner_dyson, label=r"$P(s) = \frac{\pi s}{2} e^{-\frac{\pi s^2}{4}}$")
    plt.plot(x, poisson, label=r"$P(s) = e^{-s}$")
    plt.hist(s, bins=50, density=True, alpha=0.7, label='Histogram of $s$')
    plt.xlabel(r"$s$", fontsize=12)
    plt.ylabel(r"$P(s)$", fontsize=12)
    plt.xlim(0, 5)
    plt.ylim(0)
    plt.legend(fontsize=12)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Wigner’s surmise and Poisson fitting P(s) noisy.png", dpi=300)
    plt.show()


"""Explanation:

    Sorting Eigenvalues: The eigenvalues lambdas are sorted to ensure proper mapping to their indices.
    Integrated Density: The integrated density N_lambda is simply the index of each eigenvalue.
    Cubic Spline Fit: A cubic spline is fitted to the integrated density using UnivariateSpline from scipy.interpolate. The smoothing factor s controls the trade-off between smoothness and closeness to the data.
    Unfolded Eigenvalues: The unfolded eigenvalues e_i are obtained by evaluating the fitted spline at each original eigenvalue.
    Plotting: If plot=True, the script plots the original and fitted integrated densities and the histogram of the unfolded level spacings.
    Example Usage: An example demonstrates how to use the function with random data.

Notes:

    Smoothing Factor: Adjust the smoothing_factor as needed for your specific data to get an appropriate fit.
    Eigenvalue Data: Replace the random eigenvalues in the example with your actual data.
    Dependencies: Ensure you have numpy, matplotlib, and scipy installed in your Python environment.

Feel free to integrate this script into your workflow and adjust parameters as necessary for your specific application."""