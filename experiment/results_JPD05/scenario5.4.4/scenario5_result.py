import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

if __name__ == '__main__':
    data = pd.read_excel(r'C:\Users\admin\OneDrive\Github\WRSN-team\experiment\results_JPD05\scenario5.4.4\scenario5_result.xlsx')

    fig = plt.figure()
    x = np.array(list(map(float, data['U'])))
    xx = np.array(list(map(float, data['Emc'])))
    inma = np.array(list(map(float, data['INMA'])))
    hflga = np.array(list(map(float, data['HFLGA'])))
    gr = np.array(list(map(float, data['RL-Graph'])))
    no_charging = np.array(list(map(float, data['No charging'])))
    
    inma = inma / 2
    hflga = hflga / 2
    gr = gr / 2
    no_charging = no_charging / 2
    


    plt.plot(x, inma, marker='8', label='INMA', color='green')
    plt.plot(x, hflga, marker='^', label='HFLGA', color='blue')
    plt.plot(x, gr, marker='v', label='FMCS', color='red')
    plt.plot(x, no_charging, marker='D', label='No charging', color='gray')

    
    plt.subplots_adjust(left=0.18)
    plt.xlim(2, 13)
    plt.ylim(9, 47)
    plt.xticks(x, x)
    plt.grid('x', color='0.85', linestyle="--")
    plt.grid('y', color='0.85', linestyle="--")
    plt.ylabel("Node failure ratio (%)")
    plt.xlabel("Charging rate (J/s)")
    plt.legend(loc='upper left')
    
   
    plt.show()
    #

