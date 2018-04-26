# make a nice plot of SMR spectrum and label some lines and compare with solar spectrum (same temps)

import numpy as np
import matplotlib.pyplot as plt

smrdata = np.genfromtxt('../misc_data/bd60583.txt')
solardata = np.genfromtxt('../misc_data/objs_ap5.txt')


smr_wave = smrdata[1234:1341, 0]
smr_flux = smrdata[1234:1341, 1]

solar_wave = solardata[1234:1341, 0]
solar_flux = solardata[1234:1341, 1]
solar_wave = solar_wave + 0.42
solar_flux = solar_flux - 0.009

fig=plt.figure(figsize=(9,4.5))

plt.plot(solar_wave, solar_flux, linewidth=3.0, color='RoyalBlue', label='Sun, T=5770')
plt.plot(smr_wave, smr_flux,linewidth=3.0, color='FireBrick', label='BD+60 583, T=5817')

plt.xticks(np.arange(6704, 6727.5, 3))
plt.yticks(np.arange(.70, 1.05, 0.05))


plt.xlim((6702.7, 6723.1))
plt.ylim((0.67, 1.03))
plt.tick_params(labelsize=14)

plt.ylabel('Normalized Flux', fontsize=14)
plt.xlabel(r'Wavelength ($\mathrm{\AA}$)', fontsize=14)

# plot various elements
elmwidth = 1.75

plt.text(6703.1, 0.85, 'Fe I', fontsize=12)
plt.vlines(6703.6, 0.87, 0.90, linewidth=elmwidth)

plt.text(6704.6, 0.82, 'Fe I', fontsize=12)
plt.vlines(6705.1, 0.84, 0.87, linewidth=elmwidth)

plt.text(6707.1, 0.90, 'Fe I', fontsize=12)
plt.vlines(6707.6, 0.92, 0.95, linewidth=elmwidth)

plt.text(6709.8, 0.88, 'Fe I', fontsize=12)
plt.vlines(6710.3, 0.90, 0.93, linewidth=elmwidth)

plt.text(6712.6, 0.85, 'Fe I', fontsize=12)
plt.vlines(6713.1, 0.87, 0.90, linewidth=elmwidth)

plt.text(6713.3, 0.87, 'Fe I', fontsize=12)
plt.vlines(6713.8, 0.89, 0.92, linewidth=elmwidth)

plt.text(6714.9, 0.85, 'Fe I', fontsize=12)
plt.vlines(6715.4, 0.87, 0.90, linewidth=elmwidth)

plt.text(6715.8, 0.88, 'Fe I', fontsize=12)
plt.vlines(6716.3, 0.90, 0.93, linewidth=elmwidth)

plt.text(6717.1, 0.68, 'Ca I', fontsize=12)
plt.vlines(6717.6, 0.70, 0.73, linewidth=elmwidth)

plt.text(6719.3, 0.87, 'Si I', fontsize=12)
plt.vlines(6719.7, 0.89, 0.92, linewidth=elmwidth)

plt.text(6721.4, 0.82, 'Si I', fontsize=12)
plt.vlines(6721.8, 0.84, 0.87, linewidth=elmwidth)

# work on the legend
plt.legend(loc=3, prop={'size': 12}, frameon=False)

plt.savefig('solar_smr_compare', format='pdf',bbox_inches='tight')

plt.show()