import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp import comb_step_ramp

'original function'

t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp(t,x)
print(x)
plt.subplot(2,2,1)
plt.step(t,x)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('original function')

'TIME INVERSION x(-t)'

y=[]
comb_step_ramp(-t,y)
plt.subplot(2,2,2)
plt.step(t,y)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('time inversion function')
plt.show()

'AMPLITUDE INVERSION -x(t)'

z=[]
comb_step_ramp(t,z)
plt.subplot(2,2,3)
z[:] = [x*-1 for x in z]
plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('amplitude inversion function')
plt.show()

'TIME SCALING BY 2t'

u=[]
comb_step_ramp(2*t,u)
plt.subplot(2,2,4)
plt.step(t,u)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('time scalling by 2 function')
plt.show()


