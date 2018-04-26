"""make a Mv vs teff Hr diagram with different ages"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

directory = '/home/donald/Desktop/PYTHON/misc_data/'
iso_subdir = 'age_diff_iso/'

# read in the isochrones - some or none of these will be used

age250 = np.genfromtxt(directory+iso_subdir+'age0.25.dat', skip_header=8)
age250[:, 5] = 10**age250[:, 5]

age500 = np.genfromtxt(directory+iso_subdir+'age0.5.dat', skip_header=8)
age500[:, 5] = 10**age500[:, 5]

age1 = np.genfromtxt(directory+iso_subdir+'age1.dat', skip_header=8)
age1[:, 5] = 10**age1[:, 5]

age25 = np.genfromtxt(directory+iso_subdir+'age2.5.dat', skip_header=8)
age25[:, 5] = 10**age25[:, 5]

age50 = np.genfromtxt(directory+iso_subdir+'age5.dat', skip_header=8)
age50[:, 5] = 10**age50[:, 5]

age10 = np.genfromtxt(directory+iso_subdir+'age10.dat', skip_header=8)
age10[:, 5] = 10**age10[:, 5]

plt.figure(figsize=(5, 6))

plt.plot(age250[:-350, 5], age250[:-350, 25], c='RoyalBlue', label='250 Myr', zorder=0, linewidth=5)

plt.plot(age500[:-300, 5], age500[:-300, 25], c='DarkOrchid', label='500 Myr', zorder=0, linewidth=5)

plt.plot(age1[:-300, 5], age1[:-300, 25], c='DarkSlateGray', label='1 Gyr', zorder=0, linewidth=5)

plt.plot(age25[:-260, 5], age25[:-260, 25], c='Green', label='2.5 Gyr', zorder=0, linewidth=5)

plt.plot(age50[:-200, 5], age50[:-200, 25], c='Orange', label='5.0 Gyr', zorder=0, linewidth=5)

plt.plot(age10[:-200, 5], age10[:-200, 25], c='FireBrick', label='10 Gyr', zorder=0, linewidth=5)

plt.scatter(5770, 5.0, marker='*', s=500, c='White', linewidth=3, edgecolor='k')

# limits for plot with isochrones added
plt.xlim([4500, 12500])
plt.ylim([-2.75, 7.25])

plt.xlabel('Temperature (K)', fontsize=12)
plt.ylabel(r'$M_V$', fontsize=12)

plt.legend(loc=3, fontsize=12)

# invert the axes
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

plt.savefig(directory+'example_hr', format='pdf', bbox_inches='tight')
plt.show()