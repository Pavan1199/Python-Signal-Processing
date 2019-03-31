import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp import comb_step_ramp

'EVEN SIGNAL'

t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp(t,x)



y=[]
comb_step_ramp(-t,y)



z=[]
plt.subplot(2,1,1)
[z.append((x[i]+y[i])/2) for i in range(len(x))]
plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('the even signal')
plt.show()
'ODD SIGNAL'
a=[]
plt.subplot(2,1,2)
[a.append((x[i]-y[i])/2) for i in range(len(x))]
plt.step(t,a)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('odd signal')
plt.show()

