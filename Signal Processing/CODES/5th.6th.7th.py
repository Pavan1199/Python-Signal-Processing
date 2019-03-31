import matplotlib.pyplot as plt
import numpy as np
from comb_step_ramp import comb_step_ramp
t = np.arange(-10, 10,0.01)

'TIME SCALING BY t/2'

x=[]
comb_step_ramp(t/2,x)
plt.subplot(2,2,1)
plt.step(t,x)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('time scaling by 1/2 function')
plt.show()

'AMPLITUDE SCALING BY 4'

y=[]
comb_step_ramp(t,y)
y[:] = [x*4 for x in y]
plt.subplot(2,2,2)
plt.step(t,y)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('amplitude scaling by 4 function')
plt.show()

'AMPLITUDE SCALING BY -4'

z=[]
comb_step_ramp(t,z)
z[:] = [x*-4 for x in z]
plt.subplot(2,2,3)
plt.step(t,z)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('amplitude scaling by -4 function')
plt.show()




