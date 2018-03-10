"""make an HR diagram using the ANNA SMR + Li measurements - color code the metallicity bins and shape code by
Li abundance"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

directory = '/home/donald/Desktop/PYTHON/misc_data/'

input_data = '/home/donald/Desktop/PYTHON/misc_data/smr_mv_temp.csv'

alldata = np.genfromtxt(input_data, skip_header=1, delimiter=',')
alldata = alldata[:, 1:]

# now bin by 3 metallicities:

nbins = 3
max_metal = np.max(alldata[:, 3])
min_metal = np.min(alldata[:, 3])

bin_size = (max_metal-min_metal)/nbins
metal_bins = np.arange(min_metal, max_metal, bin_size)

alldata = alldata[np.argsort(alldata[:, 3])]

# indices of the metallicities will be stored as list of lists from lowest to highest metallicity
high_l = []
low_l = []

# bin by metallicity and lithium abundance
for i in range(nbins):
    temp_high_l = []
    temp_low_l = []
    current_metal_leftedge = min_metal + i*bin_size
    for m in range(np.size(alldata[:, 3])):
        if current_metal_leftedge <= alldata[m, 3] <= (current_metal_leftedge + bin_size):
            if alldata[m, 1] < 1.95:
                temp_low_l.append(m)
            else:
                temp_high_l.append(m)
    high_l.append(temp_high_l)
    low_l.append(temp_low_l)

for i in range(nbins):
    current_metal_leftedge = min_metal + i * bin_size
    print(current_metal_leftedge)
    print(current_metal_leftedge+bin_size)

# now actually do the plotting
plt.figure(figsize=(8, 4))

# low to high metallicity
colors = ['RoyalBlue', 'DarkOrange', 'FireBrick']
labels = ['0.200 < [Fe/H] < 0.262', '0.262 < [Fe/H] < 0.323', '0.323 < [Fe/H] < 0.385']

for i in range(nbins):
    plt.scatter(alldata[high_l[i], 2], alldata[high_l[i], 0], c=colors[i], linewidth=1.2, s=120, edgecolor='k', marker='o', label=labels[i], zorder=1)
    plt.scatter(alldata[low_l[i], 2], alldata[low_l[i], 0], c=colors[i], linewidth=1.2, s=120, edgecolor='k', marker='v', zorder=3)
    plt.scatter(alldata[low_l[i], 2], alldata[low_l[i], 0], c='None', linewidth=2.2, s=240, edgecolor='k', marker='v', zorder=2)

# would be awesome to plot some isochrones on this plot to see what they should look like (reddening would not fix the trends)

plt.legend(loc=2, fontsize=10, frameon=False)
plt.xlabel('Temperature (K)', fontsize=14)
plt.ylabel(r'$M_V$ (mag)', fontsize=14)

plt.ylim([1.8, 4.7])
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

plt.savefig(directory+'smr_hr_diagram', format='pdf', bbox_inches='tight')
plt.show()


