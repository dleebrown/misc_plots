"""plot [O/Fe] vs [Fe/H] for the stars in the sample with oxygen measurements"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

directory = '/home/donald/Desktop/PYTHON/misc_data/'

inputdata = '/home/donald/Desktop/PYTHON/misc_data/oxygen_measures.csv'

data = np.genfromtxt(inputdata, delimiter=',', skip_header=1)

plt.figure(figsize=(8,3))
plt.errorbar(data[:, 1], data[:, 5], yerr=data[:, 6], xerr=0.075, linestyle='None', capsize=3.0, ecolor='RoyalBlue', zorder=1)
plt.scatter(data[:, 1], data[:, 5], color='RoyalBlue', marker='o', edgecolor='k', linewidth=1.5, s=100, zorder=3)

plt.plot([0.2, 0.2], [-1, 1], linestyle='--', c='FireBrick', linewidth=3.0, zorder=0)

plt.ylim([-0.65, 0.35])

plt.ylabel('[O/Fe]', fontsize=12)
plt.xlabel('[Fe/H]', fontsize=12)

plt.savefig(directory+'oxygen_smr', bbox_inches='tight', format='pdf')

plt.show()