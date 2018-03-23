"""two-panel plot - the plateau temperature region and the distribution of Li for these stars
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

directory = '/home/donald/Desktop/PYTHON/misc_data/'

input_data = '/home/donald/Desktop/PYTHON/misc_data/confirmed_SMR_Li_plateau_only_noll.csv'
data = np.genfromtxt(input_data, delimiter=',', skip_header=1)

# set the bin width to be approximately the uncertainty in A(Li)
nbins = 5

f, ((ax1, ax2)) = plt.subplots(1, 2, figsize=(10, 5))
f.subplots_adjust(wspace=0.3)

print(np.mean(data[:, 2]))
print(np.std(data[:, 2]))


ax1.scatter(data[:, 3], data[:, 2], color='FireBrick', s=120, zorder=4)
ax1.plot([5500, 6500], [2.55, 2.55], linestyle='--', linewidth=4.0, color='DarkSlateGray', zorder=1)
ax1.plot([5500, 6500], [2.55, 2.55], linestyle='-', color='LightBlue', linewidth=82, zorder=0)
ax1.errorbar(6160, 2.15, xerr=57, yerr=0.15, ecolor='k', capsize=3, zorder=3)

n, bins, patches = ax2.hist(data[:, 2], bins=nbins, color='DarkSlateGray', edgecolor='White', linewidth=3.5)

ax1.set_xlim([5920, 6230])
ax1.set_ylim([1.95, 3.05])
ax1.set_ylabel('A(Li) (dex)', fontsize=12)
ax1.set_xlabel('Temperature (K)', fontsize=12)

ax2.set_ylabel('# Stars', fontsize=12)
ax2.set_xlabel('A(Li)', fontsize=12)

plt.savefig(directory+'plateau_doubleplot', format='pdf')

plt.show()

