# make a nice plot of solar spectrum and saves with no background

import numpy as np
import matplotlib.pyplot as plt
solardata = np.genfromtxt('../misc_data/objs_ap5.txt')

solar_wave = solardata[500:1541, 0]
solar_flux = solardata[500:1541, 1]
solar_wave = solar_wave + 0.42
solar_flux = solar_flux - 0.009

fig=plt.figure(figsize=(35,4.5))

plt.plot(solar_wave, solar_flux, linewidth=3.0, color='Black', label='Sun, T=5770')

plt.xticks(np.arange(6600, 6800.5, 3))
plt.yticks(np.arange(.70, 1.05, 0.05))


plt.xlim((6690, 6730))
plt.ylim((0.67, 1.03))
plt.tick_params(labelsize=14)

plt.savefig('justthesun', format='png', transparent=True, bbox_inches='tight')

plt.show()