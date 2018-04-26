"""
some simple plots showing the distributions of metallicity and temperature for the SMR stars
"""

import numpy as np
import matplotlib.pyplot as plt

directory = '/home/donald/current_work/MY_THESIS/'
data_file = '/home/donald/current_work/MY_THESIS/weighted_temp_met_SMR.csv'

data_in = np.genfromtxt(data_file, delimiter=',', skip_header=1)

weighted_temps = data_in[:, 1]
e_temps = data_in[:, 2]

weighted_mets = data_in[:, 3]
e_mets = data_in[:, 4]

nbins_temp = 14
nbins_met = 18

n, bins, patches = plt.hist(weighted_temps, bins=nbins_temp, color='DarkSlateGray', edgecolor='White', linewidth=3.5)
plt.xlabel('Weighted Mean Surface Temperature (K)', fontsize=16)
plt.ylabel('N Stars', fontsize=16)
plt.xlim([5675, 7150])
plt.ylim([0, 28])
plt.savefig(directory+'mean_temp_distro', format='pdf')
plt.show()

n2, bins2, patches2 = plt.hist(weighted_mets, bins=nbins_met, color='SteelBlue', edgecolor='White', linewidth=3.0)
plt.xlabel('Weighted Mean [Fe/H] (dex)', fontsize=16)
plt.ylabel('N Stars', fontsize=16)
plt.ylim([0, 18])
plt.xlim([-0.45, 0.45])
plt.savefig(directory+'mean_metal_distro', format='pdf')
plt.show()


sun_met = 0.0148
sun_emet = 0.0371

sun_temp = 5773.89
sun_etemp = 55.655
plt.rcParams["figure.figsize"] = (12, 12)

plt.errorbar(weighted_temps, weighted_mets, linestyle='None', xerr=e_temps, yerr=e_mets, ecolor='SteelBlue',
             elinewidth=2, capsize=5, capthick=2, fmt='o', ms=12, mew=2.2, markerfacecolor='SteelBlue',
             markeredgecolor='White', zorder=0)


plt.errorbar(sun_temp, sun_met, linestyle='None', xerr=sun_etemp, yerr=sun_emet, ecolor='GoldenRod',
             elinewidth=2, capsize=5, capthick=2, fmt='*', ms=25, mew=1, markerfacecolor='GoldenRod',
             markeredgecolor='White', zorder=1)

# dummy points for the legend
#plt.scatter(100, 100, c='SteelBlue', label='SMR')
#plt.scatter(100, 100, c='GoldenRod', marker='*', label='Sun')
plt.xlabel('Weighted Mean Surface Temperature (K)', fontsize=16)
plt.ylabel('Weighted Mean [Fe/H] (dex)', fontsize=16)

plt.ylim([-0.6, 0.6])
plt.xlim([5620, 7400])

plt.text(5730, -0.05, 'Sun', fontsize=16)
plt.savefig(directory+'big_smr_teff_met', format='pdf')
plt.show()


# now a zoom-in avoiding any outliers

plt.rcParams["figure.figsize"] = (12, 12)

plt.errorbar(weighted_temps, weighted_mets, linestyle='None', xerr=e_temps, yerr=e_mets, ecolor='SteelBlue',
             elinewidth=2, capsize=5, capthick=2, fmt='o', ms=12, mew=2.2, markerfacecolor='SteelBlue',
             markeredgecolor='White', zorder=0)


plt.errorbar(sun_temp, sun_met, linestyle='None', xerr=sun_etemp, yerr=sun_emet, ecolor='GoldenRod',
             elinewidth=2, capsize=5, capthick=2, fmt='*', ms=30, mew=1, markerfacecolor='GoldenRod',
             markeredgecolor='White', zorder=1)

# dummy points for the legend
#plt.scatter(100, 100, c='SteelBlue', label='SMR')
#plt.scatter(100, 100, c='GoldenRod', marker='*', label='Sun')
plt.xlabel('Weighted Mean Surface Temperature (K)', fontsize=16)
plt.ylabel('Weighted Mean [Fe/H] (dex)', fontsize=16)

plt.ylim([-0.06, 0.48])
plt.xlim([5620, 6425])

plt.text(5755, -0.04, 'Sun', fontsize=16)
plt.text(6250, 0.0, 'Omitted: 7', fontsize=16)
plt.savefig(directory+'zoom_smr_teff_met', format='pdf')
plt.show()

# now plot the correlations between uncertainties

plt.scatter(e_temps, e_mets, c='DarkSlateGray', edgecolors='White', linewidths=1.4, s=150)
plt.xlabel('Temperature Uncertainty (K)', fontsize=16)
plt.ylabel('[Fe/H] Uncertainty (dex)', fontsize=16)
plt.xlim([40, 275])
plt.ylim([0.025, 0.29])
plt.savefig(directory+'smr_big_uncertainties', format='pdf')
plt.show()

plt.scatter(e_temps, e_mets, c='DarkSlateGray', edgecolors='White', linewidths=1.4, s=150)
plt.xlabel('Temperature Uncertainty (K)', fontsize=16)
plt.ylabel('[Fe/H] Uncertainty (dex)', fontsize=16)
plt.xlim([40, 100])
plt.ylim([0.028, 0.115])
plt.text(85, 0.035, 'Omitted: 6', fontsize=16)
plt.savefig(directory+'smr_zoom_uncertainties', format='pdf')
plt.show()
