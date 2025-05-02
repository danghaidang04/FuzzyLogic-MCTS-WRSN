import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

E_min_crisp = 3.8542
L_r_crisp = 1
E_min = ctrl.Antecedent(np.linspace(0, 10, num = 1001), 'E_min')
L_r = ctrl.Antecedent(np.arange(0, 1000), 'L_r')
Theta = ctrl.Consequent(np.linspace(0, 1, num = 1001), 'Theta')
L_r['L'] = fuzz.trapmf(L_r.universe, [0, 0, 2, 6])
L_r['M'] = fuzz.trimf(L_r.universe, [2, 6, 10])
L_r['H'] = fuzz.trapmf(L_r.universe, [6, 10, 1000, 1000])

E_min['L'] = fuzz.trapmf(E_min.universe, [0, 0, 2.5, 5])
E_min['M'] = fuzz.trimf(E_min.universe, [2.5, 5.0, 7.5])
E_min['H'] = fuzz.trapmf(E_min.universe, [5, 7.5, 10, 10])

Theta['VL'] = fuzz.trimf(Theta.universe, [0, 0, 1/3])
Theta['L'] = fuzz.trimf(Theta.universe, [0, 1/3, 2/3])
Theta['M'] = fuzz.trimf(Theta.universe, [1/3, 2/3, 1])
Theta['H'] = fuzz.trimf(Theta.universe, [2/3, 1, 1])

R1 = ctrl.Rule(L_r['L'] & E_min['L'], Theta['H'])
R2 = ctrl.Rule(L_r['L'] & E_min['M'], Theta['M'])
R3 = ctrl.Rule(L_r['L'] & E_min['H'], Theta['L'])
R4 = ctrl.Rule(L_r['M'] & E_min['L'], Theta['M'])
R5 = ctrl.Rule(L_r['M'] & E_min['M'], Theta['L'])
R6 = ctrl.Rule(L_r['M'] & E_min['H'], Theta['VL'])
R7 = ctrl.Rule(L_r['H'] & E_min['L'], Theta['L'])
R8 = ctrl.Rule(L_r['H'] & E_min['M'], Theta['VL'])
R9 = ctrl.Rule(L_r['H'] & E_min['H'], Theta['VL'])

FLCDS_ctrl = ctrl.ControlSystem([R1, R2, R3,
                                 R4, R5, R6,
                                 R7, R8, R9])
FLCDS = ctrl.ControlSystemSimulation(FLCDS_ctrl)
FLCDS.input['L_r'] = L_r_crisp
FLCDS.input['E_min'] = E_min_crisp
FLCDS.compute()
alpha = FLCDS.output['Theta']


#E_min.view()
