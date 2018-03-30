import matplotlib.pyplot as plt
from math import *
import numpy as np

ratio_n_2_to_n_1 = 2.0
beta = 2.0

d_angle = 1.0


T_amp = []
R_amp = []
Incident_angle = []
incident_angle = 0
R = []
T = []
total = []


while incident_angle < 90:
	I_angle = np.deg2rad(incident_angle)
	alpha_beta = sqrt(beta**2-sin(I_angle)**2)/cos(I_angle)
	E_T_over_E_I = (2/(1+alpha_beta))
	E_R_over_E_I = abs((1-alpha_beta)/(1+alpha_beta))
	T_amp.append(E_T_over_E_I)
	R_amp.append(E_R_over_E_I)
	Incident_angle.append(incident_angle)

	R.append((E_R_over_E_I)**2)
	T.append(alpha_beta*(E_T_over_E_I)**2)
	total.append((alpha_beta*(E_T_over_E_I)**2) + (E_R_over_E_I)**2) 
	incident_angle += d_angle

plt.plot(Incident_angle, T_amp, label = r'$\frac{E_{T}}{E_{I}}$')
plt.plot(Incident_angle, R_amp, label = r'$\frac{E_{R}}{E_{I}}$')
plt.ylabel('Amplitude of Electric Field')
plt.xlabel(r'$\theta_{I}$')
plt.suptitle(r'Ratio of Reflected and Transmitted Amplitudes corresponding to $\theta_{I}$')
plt.title('No Brewster angle', fontsize = 10)
plt.legend()
plt.show()


plt.plot(Incident_angle, T, label = 'T')
plt.plot(Incident_angle, R, label = 'R')
plt.plot(Incident_angle, total, '--',  label = 'R+T')
plt.ylabel('Intensity ratios of Electric Field')
plt.xlabel(r'$\theta_{I}$')
plt.title(r'Ratio of Reflected and Transmitted Coefficients corresponding to $\theta_{I}$')
plt.legend()
plt.show()

