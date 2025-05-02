import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.ticker import AutoMinorLocator
import pandas as pd

fig, ax = plt.subplots(layout='constrained')
data = pd.read_excel(r'C:\Users\admin\OneDrive\Github\WRSN-team\experiment\results_JPD05\scenario5.4.4\scenario5_result.xlsx')

x = np.array(list(map(float, data['U'])))
xx = np.array(list(map(float, data['Emc'])))
inma = np.array(list(map(float, data['INMA'])))
hflga = np.array(list(map(float, data['HFLGA'])))
gr = np.array(list(map(float, data['RL-Graph'])))
no_charging = np.array(list(map(float, data['No charging'])))

xx = xx/1000
inma = inma / 2
hflga = hflga / 2
gr = gr / 2
no_charging = no_charging / 2

ax.plot(x, inma, marker='8', label='INMA', color='green')
ax.plot(x, hflga, marker='^', label='HFLGA', color='blue')
ax.plot(x, gr, marker='v', label='FMCS', color='red')
ax.plot(x, no_charging, marker='D', label='No charging', color='gray')
ax.set_ylabel("Node failure ratio (%)")
ax.set_xlabel("Charging rate (J/s)")

#plt.subplots_adjust(left=0.18)
plt.xlim(2, 13)
plt.ylim(9, 47)


#plt.xticks(x, np.array([1,2,3,4,5]))
plt.xticks(x, x)
#plt.xticks(xx, xx)
plt.grid('x', color='0.85', linestyle="--")
plt.grid('y', color='0.85', linestyle="--")
plt.legend(loc='upper left')

def f1(x):
    return x*21.6

def f2(x):
    return x/21.6

secax = ax.secondary_xaxis('top', functions=(f1, f2))
secax.set_xlabel("Capacity of MC (kJ)")
secax.set_xticks(xx,xx)
plt.show()