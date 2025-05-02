import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe variables
#   * Quality and service on subjective ranges [0, 10]
#   * Tip has a range of [0, 25] in units of percentage points
x_qual = np.arange(0.0, 1.1, 0.1)
x_serv = np.arange(0.0, 1.1, 0.1)
x_tip  = np.arange(0.0, 1.1, 0.1)

# Generate fuzzy membership functions
qual_lo = fuzz.trapmf(x_qual, [0, 0, 0.2, 0.25])
qual_md = fuzz.trapmf(x_qual, [0.2, 0.25, 0.75, 0.8])
qual_hi = fuzz.trapmf(x_qual, [0.75, 0.8, 1, 1])
serv_lo = fuzz.trapmf(x_serv, [0, 0, 0.2, 0.25])
serv_md = fuzz.trapmf(x_serv, [0.2, 0.25, 0.45, 0.55])
serv_hi = fuzz.trapmf(x_serv, [0.45, 0.55, 1, 1])
tip_lo = fuzz.trapmf(x_tip, [0, 0, 0.2, 0.25])
tip_md = fuzz.trapmf(x_tip, [0.2, 0.25, 0.75, 0.85])
tip_hi = fuzz.trapmf(x_tip, [0.75, 0.85, 1, 1])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(16, 4))

ax0.plot(x_qual, qual_lo, 'b', linewidth=1.5, label='Low')
ax0.plot(x_qual, qual_md, 'g', linewidth=1.5, label='Medium')
ax0.plot(x_qual, qual_hi, 'r', linewidth=1.5, label='High')
#ax0.set_title('Food quality')
ax0.set_xlabel('EF')
ax0.set_ylabel('Membership degree')
ax0.legend(loc='upper right')

ax1.plot(x_serv, serv_lo, 'b', linewidth=1.5, label='Low')
ax1.plot(x_serv, serv_md, 'g', linewidth=1.5, label='Medium')
ax1.plot(x_serv, serv_hi, 'r', linewidth=1.5, label='High')
#ax1.set_title('Service quality')
ax1.set_xlabel('UF')
ax1.set_ylabel('Membership degree')
ax1.legend(loc = 'upper right')

ax2.plot(x_tip, tip_lo, 'b', linewidth=1.5, label='Low')
ax2.plot(x_tip, tip_md, 'g', linewidth=1.5, label='Medium')
ax2.plot(x_tip, tip_hi, 'r', linewidth=1.5, label='High')
#ax2.set_title('Tip amount')
ax2.set_xlabel('ESR')
ax2.set_ylabel('Membership degree')
ax2.legend(loc = 'upper right')
plt.show()
fig.savefig('hello.pdf')