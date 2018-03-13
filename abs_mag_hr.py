"""make an HR diagram using the ANNA SMR + Li measurements - color code the metallicity bins and shape code by
Li abundance
Now includes isochrones!"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

directory = '/home/donald/Desktop/PYTHON/misc_data/'
iso_subdir = 'smr_isochrones/'

input_data = '/home/donald/Desktop/PYTHON/misc_data/smr_mv_temp.csv'

# read in the isochrones - some or none of these will be used

age1_met29 = np.genfromtxt(directory+iso_subdir+'age1_met29.dat', skip_header=8)
age1_met29[:, 5] = 10**age1_met29[:, 5]

age4_met23 = np.genfromtxt(directory+iso_subdir+'age4_met23.dat', skip_header=8)
age4_met23[:, 5] = 10**age4_met23[:, 5]

age4_met29 = np.genfromtxt(directory+iso_subdir+'age4_met29.dat', skip_header=8)
age4_met29[:, 5] = 10**age4_met29[:, 5]

age4_met35 = np.genfromtxt(directory+iso_subdir+'age4_met35.dat', skip_header=8)
age4_met35[:, 5] = 10**age4_met35[:, 5]

age55_met23 = np.genfromtxt(directory+iso_subdir+'age55_met23.dat', skip_header=8)
age55_met23[:, 5] = 10**age55_met23[:, 5]

age55_met29 = np.genfromtxt(directory+iso_subdir+'age55_met29.dat', skip_header=8)
age55_met29[:, 5] = 10**age55_met29[:, 5]

age55_met35 = np.genfromtxt(directory+iso_subdir+'age55_met35.dat', skip_header=8)
age55_met35[:, 5] = 10**age55_met35[:, 5]

age7_met23 = np.genfromtxt(directory+iso_subdir+'age7_met23.dat', skip_header=8)
age7_met23[:, 5] = 10**age7_met23[:, 5]

age7_met29 = np.genfromtxt(directory+iso_subdir+'age7_met29.dat', skip_header=8)
age7_met29[:, 5] = 10**age7_met29[:, 5]

age7_met35 = np.genfromtxt(directory+iso_subdir+'age7_met35.dat', skip_header=8)
age7_met35[:, 5] = 10**age7_met35[:, 5]

age35_met23 = np.genfromtxt(directory+iso_subdir+'age35_met23.dat', skip_header=8)
age35_met23[:, 5] = 10**age35_met23[:, 5]

age35_met29 = np.genfromtxt(directory+iso_subdir+'age35_met29.dat', skip_header=8)
age35_met29[:, 5] = 10**age35_met29[:, 5]

age35_met35 = np.genfromtxt(directory+iso_subdir+'age35_met35.dat', skip_header=8)
age35_met35[:, 5] = 10**age35_met35[:, 5]

# import a grid of 3.5 gyr isochrones from Z=0.258 to 0.034 in steps of dZ = 0.0001
grid35 = np.genfromtxt(directory+iso_subdir+'age35_densegrid.dat')
grid4 = np.genfromtxt(directory+iso_subdir+'age4_densegrid.dat')


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
    plt.scatter(alldata[high_l[i], 2], alldata[high_l[i], 0], c=colors[i], linewidth=1.2, s=120, edgecolor='k', marker='o', label=labels[i], zorder=5)
    plt.scatter(alldata[low_l[i], 2], alldata[low_l[i], 0], c=colors[i], linewidth=1.2, s=120, edgecolor='k', marker='v', zorder=7)
    plt.scatter(alldata[low_l[i], 2], alldata[low_l[i], 0], c='None', linewidth=2.2, s=240, edgecolor='k', marker='v', zorder=6)

# would be awesome to plot some isochrones on this plot to see what they should look like (reddening would not fix the trends)
# so actually plot them then
# plot a 1gyr isochrone to show the young MS over these temperatures
plt.plot(age1_met29[:-30, 5], age1_met29[:-30, 25], c='FireBrick', linewidth=3.0, linestyle='--', zorder=1, label='1 Gyr')

# now plot a 3.5gyr isochrone with spread in metallicity similar to the sample. fill between to illustrate the band
# covered by changing metallicity. there's no easy way to fill between so just make a bunch of isochrones of metallicity
# and adjust linewidth to create illusion of filled between.

# these are just for labeling purposes
plt.plot(age35_met29[:-1, 5], age35_met29[:-1, 25], c='Plum', label='3.5 Gyr', zorder=0, linewidth=3)
#plt.plot(age35_met23[:-1, 5], age35_met23[:-1, 25], c='DarkOrange')
#plt.plot(age35_met35[:-1, 5], age35_met35[:-1, 25], c='DarkOrange')

plt.plot(age4_met29[:-1, 5], age4_met29[:-1, 25], c='MediumAquaMarine', label='4.0 Gyr', linewidth=3, zorder=0)
#plt.plot(age55_met23[:-1, 5], age55_met23[:-1, 25], c='RoyalBlue')
#plt.plot(age7_met23[:-1, 5], age7_met23[:-1, 25], c='RoyalBlue')

# loop over the imported grid of age = 3.5 gyr isochrones - this is real nasty code
metal_grid = np.arange(0.0258, 0.034, 0.0001)
for i in range(np.size(np.arange(0.0258, 0.034, 0.0001))):
    current_metallicity = 0.0258+i*0.0001
    temp_temp = []
    temp_mv = []
    for j in range(np.size(grid35[:, 5])):
        if grid35[j, 0] == current_metallicity:
            temp_temp.append(grid35[j, 5])
            temp_mv.append(grid35[j, 25])
    temp_temp = np.array(temp_temp)
    temp_temp = 10**temp_temp
    plt.plot(temp_temp[:-1], temp_mv[:-1], color='Plum', linewidth=3, zorder=2)

for i in range(np.size(np.arange(0.0258, 0.034, 0.0001))):
    current_metallicity = 0.0258+i*0.0001
    temp_temp = []
    temp_mv = []
    for j in range(np.size(grid4[:, 5])):
        if grid4[j, 0] == current_metallicity:
            temp_temp.append(grid4[j, 5])
            temp_mv.append(grid4[j, 25])
    temp_temp = np.array(temp_temp)
    temp_temp = 10**temp_temp
    plt.plot(temp_temp[:-1], temp_mv[:-1], color='MediumAquaMarine', linewidth=3.3, zorder=3)

# now work on controlling the figure layout
plt.legend(loc=2, fontsize=10, ncol=2)
plt.xlabel('Temperature (K)', fontsize=14)
plt.ylabel(r'$M_V$ (mag)', fontsize=14)

# now add points corresponding to the cool side dip mass for the hyades (+0.15) and 6253 (+0.4) for each age used
# 4 gyr 1.27 mass first
#plt.scatter(5906, 3.297, c='k', marker='*', s=200, zorder=9)

# 4 gyr 1.34 mass next
plt.scatter(5821, 3.018, c='Plum', marker='*', edgecolor='k', s=350, linewidth=1.2, zorder=4)

# now 3.5 gyr stuff
plt.scatter(5988, 3.083, c='MediumAquaMarine', marker='*', edgecolor='k', linewidth=1.2, s=350, zorder=4)
#plt.scatter(6031, 3.329, c='k', marker='*', s=200, zorder=9)

# these are limits so I can see the isochrone better
#plt.xlim([4000, 7000])
#plt.ylim([0.5, 8.7])

# these are limits for the actual plot
#plt.xlim([5795, 6245])
#plt.ylim([1.8, 4.7])

# limits for plot with isochrones added
plt.xlim([5675, 6300])
plt.ylim([1.50, 4.75])

# invert the axes
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

plt.savefig(directory+'smr_hr_diagram', format='pdf', bbox_inches='tight')
plt.show()


