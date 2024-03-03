import matplotlib.pyplot as plt
import math
import numpy as np
import figStuff as fs


phi = 4.85
F = 2.8 #V*nm-1
e = 1.602176634e-1 
e0= 8.85e-3

z = np.linspace(0.01,1,100)
z = np.array(z)

m = []
M = []
for i in range(0,len(z)):
    m.append(phi - F*z[i])
    M.append(phi - F*z[i] - e/(16*math.pi*e0*z[i]))


fig,ax=plt.subplots(figsize = fs.setSize(80))  # width 80 mm
fs.setTexFonts(plt,10)  # size of font 10pt
ax.tick_params(direction='in') # ticks inside plot   see https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.html
               

#plt.plot(z,m,color='red',marker='+',linestyle='None', label='m')
plt.plot(z,m,color='red', linewidth=2,label=r'm')
plt.plot(z,M,color='blue',linewidth=1,label=r'M')

#plt.xlim([0,1])     # set x axis range
#plt.ylim([-40,10])  # set y axis range
plt.xlabel(r'$z$ [nm]')
plt.ylabel(r'$m$')
plt.legend(frameon=False,loc='lower right')
fig.savefig('figure.pdf',format='pdf', bbox_inches='tight',pad_inches=0.05)
plt.show;
