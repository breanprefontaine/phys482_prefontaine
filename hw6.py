import matplotlib.pyplot as plt
from math import *


w = [1, 5, 10, 20]

time = []
time5 = []
time10 =[]
time20= []
TrueCurrent = []
TrueCurrent5 = []
TrueCurrent10 = []
TrueCurrent20 = []


i = 0
t = 0.0
dt = 0.01
tf = 10.0
v_0 = 1.0
R = 1.0
L = 1.0
C = 1.0

'''

for i in w:
	
	while t < tf:
		true_current = ((v_0 * cos(i * t)) * sqrt((1.0/R)**2 + ((1.0/(i*L))-i*C)**2))
		
		if i == 1:
			TrueCurrent.append(true_current)
			time.append(t)
		if i == 5:
			TrueCurrent5.append(true_current)
			time5.append(t)
		if i == 10:
			TrueCurrent10.append(true_current)
			time10.append(t)
		if i == 20:
			TrueCurrent20.append(true_current)
			time20.append(t)
		t = t+ dt
	t = 0.0

'''

#make new plot becuase I misread the problem
w = 0.10
w_final = 20.0
dw = 0.01
t = 1.0
frequency = []

while w < w_final:
	true_current = ((v_0 * cos(w * t)) * sqrt((1.0/R)**2 + ((1.0/(w*L))-w*C)**2))
	TrueCurrent.append(true_current)
	frequency.append(w)
	w = w + dw


plt.plot(frequency, TrueCurrent)
#plt.plot(time5, TrueCurrent5, label='w = 5')
#plt.plot(time10, TrueCurrent10, label='w = 10')
#plt.plot(time20, TrueCurrent20, label='w = 20')
plt.ylabel('True current (A)')
#plt.xlabel('Time (s)')
plt.xlabel('Angular Frequency')
plt.title('True current in parallel RLC circuit')
plt.legend()
plt.show()



