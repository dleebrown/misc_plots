"""creates some thesis plots for the NGC 6819 results:
1. fe/h vs sn
2. fe/h vs temp
3. fe/h vs line
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

directory = '/home/donald/Desktop/PYTHON/misc_data/'
solar_subdir = '6819stuff/'

by_wave = np.genfromtxt(directory+solar_subdir+'FINAL_6819bywave.csv', delimiter=',')
by_temp = np.genfromtxt(directory+solar_subdir+'FINAL_6819fetemp', delimiter=',', skip_header=1)
by_sn = np.genfromtxt(directory+solar_subdir+'FINAL_6819fesn', delimiter=',', skip_header=1)

print(by_sn)

# first plot the average/error in fe/h as a function of fe line

plt.figure(figsize=(8, 4))

plt.plot(by_wave[:, 0], by_wave[:, 1]-7.5, marker='s', linestyle='None', markerfacecolor='FireBrick', markeredgewidth=2.0, markeredgecolor='k', markersize=12, zorder=2)
plt.errorbar(by_wave[:, 0], by_wave[:, 1]-7.5, yerr=by_wave[:, 2], capsize=5.0, ecolor='FireBrick', linestyle='None', zorder=1)

plt.plot([0, 10000], [-0.02, -0.02], linestyle='--', marker='None', linewidth=3.0, color='RoyalBlue', zorder=0)

plt.xlim([6570, 6875])
plt.xlabel(r'$\lambda$ (Angstroms)', fontsize=12)
plt.ylabel('[Fe/H] (dex)', fontsize=12)

plt.savefig(directory+'6819_bywave', format='pdf')
plt.show()

# now work on the temperature plot

plt.figure(figsize=(8, 4))

by_temp = by_temp[np.argsort(by_temp[:, 1])]


plt.scatter(by_temp[:57, 1], by_temp[:57, 3]-7.5, edgecolor='k', s=75, linewidth=2.0, c='FireBrick', zorder=1, label='Giants')
plt.errorbar(by_temp[:57, 1], by_temp[:57, 3]-7.5, yerr=by_temp[:57, 4], ecolor='FireBrick', capsize=2.0, linestyle='None', zorder=0)

plt.scatter(by_temp[57:, 1], by_temp[57:, 3]-7.5, edgecolor='k', s=75, linewidth=2.0, c='RoyalBlue', zorder=1, label='Dwarfs')
plt.errorbar(by_temp[57:, 1], by_temp[57:, 3]-7.5, yerr=by_temp[57:, 4], ecolor='RoyalBlue', capsize=2.0, linestyle='None', zorder=0)

plt.plot([0, 10000], [-0.02, -0.02], linestyle='--', marker='None', linewidth=3.0, color='k', zorder=-1)


plt.legend(loc=4, fontsize=12)
plt.ylim([-0.65, 0.65])
plt.xlim([4150, 7750])

plt.xlabel('Temperature (K)', fontsize=12)
plt.ylabel('[Fe/H] (dex)', fontsize=12)

plt.savefig(directory+'6819_bytemp', format='pdf')
plt.show()

# finally work on the SN plot

plt.figure(figsize=(8, 4))

plt.plot(by_sn[:, 1], by_sn[:, 4], marker='o', linestyle='None', markerfacecolor='RoyalBlue', markeredgewidth=2.0, markeredgecolor='k', markersize=12, zorder=2)

plt.xlim([0, 370])
plt.xlabel(r'SN Ratio', fontsize=12)
plt.ylabel('$\sigma$ [Fe/H] (dex)', fontsize=12)

plt.savefig(directory+'6819_bysn', format='pdf')
plt.show()