# plot two spectra on top of each other - synthetic solar and real solar

import numpy as np
import matplotlib.pyplot as plt

synthdata = np.genfromtxt('../misc_data/send_to_me/solar.615.150.sn')
realdata = np.genfromtxt('../misc_data/send_to_me/solar20')


synth_wave = synthdata[:, 0]
synth_flux = synthdata[:, 1]

real_wave = realdata[:, 0]
real_flux = realdata[:, 1]
real_wave = real_wave
real_flux = real_flux-0.002

fig=plt.figure(figsize=(9,4.5))

plt.plot(real_wave, real_flux, linewidth=3.0, color='RoyalBlue', label='Hydra Solar Spectrum')
plt.plot(synth_wave, synth_flux,linewidth=3.0, color='FireBrick', label='Model Solar Spectrum')

plt.xticks(np.arange(6625, 6827.5, 3))
plt.yticks(np.arange(.70, 1.05, 0.05))


plt.xlim((6702, 6725))
plt.ylim((0.75, 1.03))
plt.tick_params(labelsize=14)

plt.ylabel('Normalized Flux', fontsize=14)
plt.xlabel(r'Wavelength ($\mathrm{\AA}$)', fontsize=14)

# work on the legend
plt.legend(loc=3, prop={'size': 12}, frameon=False)

plt.savefig('../solar_synth_real_comp', format='pdf',bbox_inches='tight')

plt.show()