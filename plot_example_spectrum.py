# make a nice plot of SMR spectrum

import numpy as np
import matplotlib.pyplot as plt

smrdata = np.genfromtxt('../misc_data/bd60583.txt')


smr_wave = smrdata[:, 0]
smr_flux = smrdata[:, 1]

fig=plt.figure(figsize=(11,4.5))

plt.plot(smr_wave, smr_flux,linewidth=2, color='RoyalBlue', label='BD+60 583')

plt.xticks(np.arange(6450, 6810.5, 50))
plt.yticks(np.arange(.5, 1.05, 0.1))


plt.xlim((6470.7, 6830.1))
plt.ylim((0.50, 1.03))
plt.tick_params(labelsize=14)

plt.ylabel('Normalized Flux', fontsize=14)
plt.xlabel(r'Wavelength ($\mathrm{\AA}$)', fontsize=14)

# plot various elements
elmwidth = 1.75

# work on the legend
plt.legend(loc=3, prop={'size': 12}, frameon=False)

plt.savefig('solar_example_spec', format='pdf',bbox_inches='tight')

plt.show()