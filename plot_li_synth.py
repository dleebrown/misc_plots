"""plot a variety of synth li lines over each other to illustrate the effect of changing A(Li)
"""

import numpy as np
import matplotlib.pyplot as plt

dir = '/home/donald/Desktop/PYTHON/misc_data/'
subdir = 'li_synth/'

li33 = np.genfromtxt(dir+subdir+'li33')
li28 = np.genfromtxt(dir+subdir+'li28')
li23 = np.genfromtxt(dir+subdir+'li23')
li18 = np.genfromtxt(dir+subdir+'li18')
li13 = np.genfromtxt(dir+subdir+'li13')


plt.figure(figsize=(7, 3))

plt.plot(li13[:, 0], li13[:, 1], linewidth=3.1, label='A(Li)=1.3', color='DarkMagenta')
plt.plot(li18[:, 0], li18[:, 1], linewidth=3.1, label='A(Li)=1.8', color='GoldenRod')
plt.plot(li13[:, 0], li23[:, 1], linewidth=3.1, label='A(Li)=2.3', color='DarkSlateGray')
plt.plot(li28[:, 0], li28[:, 1], linewidth=3.1, label='A(Li)=2.8', color='FireBrick')
plt.plot(li33[:, 0], li33[:, 1], linewidth=3.3, label='A(Li)=3.3', color='RoyalBlue')

plt.xlim([6703.5, 6712.5])
plt.ylim([0.638, 1.012])
plt.ylabel('Relative Flux', fontsize=12)
plt.xlabel('Wavelength (Angstroms)', fontsize=12)
plt.legend(loc=4, frameon=False, fontsize=12)

plt.savefig(dir+'li_synth_plot', bbox_inches='tight', format='pdf')


plt.show()


