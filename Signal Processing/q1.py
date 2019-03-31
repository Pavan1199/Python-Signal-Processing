import matplotlib.pyplot as plt
import numpy as np
from pavanvadde import comb_step_ramp

'original function'

t = np.arange(-10, 10,0.01)
x=[]
comb_step_ramp(t,x)
print(x)

plt.step(t,x)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('time') 
plt.ylabel('function value') 
plt.title('original function')
plt.show()
