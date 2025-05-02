import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe variables
#   * Quality and service on subjective ranges [0, 10]
#   * Tip has a range of [0, 25] in units of percentage points
x_qual = np.arange(0.0, 1.1, 0.01)


# Generate fuzzy membership functions
qual_el = fuzz.trapmf(x_qual, [0.0, 0.0, 0.05, 0.15])
qual_vl = fuzz.trapmf(x_qual, [0.05, 0.15, 0.2, 0.3])
qual_l = fuzz.trapmf(x_qual, [0.2, 0.3, 0.35, 0.45])
qual_m = fuzz.trapmf(x_qual, [0.35, 0.45, 0.5, 0.6])
qual_h = fuzz.trapmf(x_qual, [0.5, 0.6, 0.65, 0.75])
qual_vh = fuzz.trapmf(x_qual, [0.65, 0.75, 0.8, 0.9])
qual_eh = fuzz.trapmf(x_qual, [0.8, 0.9, 1.0, 1.0])


# Visualize these universes and membership functions

plt.plot(x_qual, qual_el, 'b', linewidth=1.5, label='EL')
plt.plot(x_qual, qual_vl, 'g', linewidth=1.5, label='VL')
plt.plot(x_qual, qual_l, 'r', linewidth=1.5, label='L')
plt.plot(x_qual, qual_m, 'y', linewidth=1.5, label='M')
plt.plot(x_qual, qual_h, 'c', linewidth=1.5, label='H')
plt.plot(x_qual, qual_vh, 'm', linewidth=1.5, label='VH')
plt.plot(x_qual, qual_eh, 'k', linewidth=1.5, label='EH')
#ax0.set_title('Food quality')
plt.xlabel('Theta')
plt.ylabel('Membership degree')
plt.legend(loc='upper right')
plt.savefig('bye.pdf')
plt.show()
#save the plot as a pdf file
