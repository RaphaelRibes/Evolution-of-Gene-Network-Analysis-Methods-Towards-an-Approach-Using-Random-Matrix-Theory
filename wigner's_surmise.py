import numpy as np
import matplotlib.pyplot as plt

# Define the formula P(s) = (s/2)*exp(-s^2/4)
s = np.linspace(0, 5, 500)
P_s = (s / 2) * np.exp(-s**2 / 4)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(s, P_s, label=r"$P(s) = \frac{s}{2} e^{-\frac{s^2}{4}}$")
# plt.title(r"Plot of $P(s) = \frac{s}{2} e^{-\frac{s^2}{4}}$", fontsize=14)
plt.xlabel(r"$s$", fontsize=12)
plt.ylabel(r"$P(s)$", fontsize=12)
plt.xlim(0, 5)
plt.ylim(0)
# plt.legend(fontsize=12)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.grid(True)
plt.tight_layout()
plt.savefig("Wigner’s surmise.png", dpi=300)
plt.show()

P_s = ((np.pi*s) / 2) * np.exp(-(np.pi*s**2) / 4)
P_e = np.exp(-s)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(s, P_s, label=r"$P(s) = \frac{\pi s}{2} e^{-\frac{\pi s^2}{4}}$")
plt.plot(s, P_e, label=r"$P(s) = e^{-s}$")
# plt.title(r"Plot of $P(s) = \frac{\pi s}{2} e^{-\frac{\pi s^2}{4}}$", fontsize=14)
plt.xlabel(r"$s$", fontsize=12)
plt.ylabel(r"$P(s)$", fontsize=12)
plt.xlim(0, 5)
plt.ylim(0)
plt.legend(fontsize=12)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.grid(True)
plt.tight_layout()
plt.savefig("Wigner’s surmise and Poisson.png", dpi=300)
plt.show()