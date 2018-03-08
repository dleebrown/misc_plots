"""plot my Li measurements vs ANNA-derived atmospheric parameters. thesis plot.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

directory = '/home/donald/Desktop/PYTHON/misc_data/'

input_data = '/home/donald/Desktop/PYTHON/misc_data/confirmed_SMR_Li.csv'

data = np.genfromtxt(input_data, delimiter=',', skip_header=1)

print(data)
# grab the data I need
data_array = np.zeros((np.size(data[:, 2]), 4))
data_array[:, 0] = data[:, 2]
data_array[:, 1] = data[:, 3]
data_array[:, 2] = data[:, 5]
data_array[:, 3] = data[:, 7]

# there is a break in Li measurements at 1.9 so sort these out and color code them
data_array = data_array[np.argsort(data_array[:, 0])]

lithium = data_array[:, 0]

# manually bin the data to give the best plotting control
num_bins = 10
bin_width = (np.max(lithium)-np.min(lithium))/num_bins
bin_centers = np.arange(np.min(lithium)+0.5*bin_width, np.max(lithium), bin_width)
binned_data = np.zeros((num_bins, 2))
binned_data[:, 0] = bin_centers
counter = 0
for i in range(num_bins):
    current_bin_right_edge = counter*bin_width+bin_width+np.min(lithium)
    for entry in lithium:
        if (current_bin_right_edge-bin_width) <= entry <= current_bin_right_edge:
            binned_data[i, 1] = binned_data[i, 1]+1
    counter += 1

print(binned_data)
# first make a distribution of Li measurements color coded by their population - this is actually a bar chart
# using the manually binned data so I can make fancy looking colors and stuff
matplotlib.rcParams['hatch.linewidth'] = 4.1
plt.bar(binned_data[:3, 0], binned_data[:3, 1], 0.85*bin_width, color='RoyalBlue')
plt.bar(binned_data[3, 0], binned_data[3, 1], 0.82*bin_width, color='RoyalBlue', hatch='//', edgecolor='FireBrick')
plt.bar(binned_data[3, 0], binned_data[3, 1], 0.82*bin_width, color='None', edgecolor='RoyalBlue')
plt.bar(binned_data[4:, 0], binned_data[4:, 1], 0.85*bin_width, color='FireBrick')

plt.xlabel('A(Li)', fontsize=14)
plt.ylabel('N Stars', fontsize=14)
plt.ylim([0, 10])
plt.xlim([1.29, 3.05])
plt.savefig(directory+'li_distro', format='pdf')
plt.show()

# now plot the li abundance vs surface temperature by color code
plt.scatter(data_array[:14, 1], data_array[:14, 0], s=90, color='FireBrick')
plt.scatter(data_array[14:, 1], data_array[14:, 0], s=90, color='RoyalBlue')
plt.ylim([1.15, 3.15])
plt.xlim([5750, 6275])
plt.xlabel('Temperature (K)', fontsize=14)
plt.ylabel('A(Li)', fontsize=14)
plt.savefig(directory+'li_vs_temp', format='pdf')
plt.show()


# now plot the li abundance vs metallicity
plt.scatter(data_array[:14, 2], data_array[:14, 0], s=90, color='FireBrick')
plt.scatter(data_array[14:, 2], data_array[14:, 0], s=90, color='RoyalBlue')
plt.ylim([1.15, 3.15])
plt.xlim([0.1750, 0.42])
plt.xlabel('[Fe/H]', fontsize=14)
plt.ylabel('A(Li)', fontsize=14)
plt.savefig(directory+'li_vs_metal', format='pdf')

plt.show()

# now vs gravity
plt.scatter(data_array[:14, 3], data_array[:14, 0], s=90, color='FireBrick')
plt.scatter(data_array[14:, 3], data_array[14:, 0], s=90, color='RoyalBlue')
plt.ylim([1.15, 3.15])
plt.xlim([3.9, 4.65])
plt.xlabel('log(g)', fontsize=14)
plt.ylabel('A(Li)', fontsize=14)
plt.savefig(directory+'li_vs_grav', format='pdf')

plt.show()

# now plot the metallicity and temperature on the dependent axes and Li abundance on the third axis
fig = plt.figure()
splot = fig.add_subplot(111, projection='3d')

# if i want to do color coded stuff then I need to redo the stuff I did to select data at the beginning
# and keep temps and metals attached to their Li measurements. 
splot.scatter(data_array[:14, 1], data_array[:14, 2], data_array[:14, 0], color='FireBrick', s=90)
splot.scatter(data_array[14:, 1], data_array[14:, 2], data_array[14:, 0], color='RoyalBlue', s=90)

splot.set_xlabel('Temperature (K)', fontsize=14)
splot.set_ylabel('[Fe/H] (dex)', fontsize=14)
splot.set_zlabel('A(Li)', fontsize=14)
plt.show()

# now do something a little fancier - for high Li stars, bin by metallicity and plot Li vs T with color codes
high_li_stars = data_array[14:, :]
# sort by metallicity
high_li_stars = high_li_stars[np.argsort(high_li_stars[:, 2])]

high_li_metals = high_li_stars[:, 2]

# manually bin the data to give the best plotting control
num_bins = 3
bin_width = (np.max(high_li_metals)-np.min(high_li_metals))/num_bins
bin_centers = np.arange(np.min(high_li_metals)+0.5*bin_width, np.max(high_li_metals), bin_width)
binned_metals = np.zeros((num_bins, 2))
binned_metals[:, 0] = bin_centers
counter = 0
for i in range(num_bins):
    current_bin_right_edge = counter*bin_width+bin_width+np.min(high_li_metals)
    for entry in high_li_metals:
        if (current_bin_right_edge-bin_width) <= entry <= current_bin_right_edge:
            binned_metals[i, 1] = binned_metals[i, 1]+1
    counter += 1

# now use the counts in these bins (10, 11, 10) to build the three data sets
low_metal = high_li_stars[0:10, :]
med_metal = high_li_stars[10:21, :]
high_metal = high_li_stars[21:, :]

plt.scatter(low_metal[:, 1], low_metal[:, 0], s=90, color='RoyalBlue', label='low [Fe/H]')
plt.scatter(med_metal[:, 1], med_metal[:, 0], s=90, color='Magenta', label='med [Fe/H]')
plt.scatter(high_metal[:, 1], high_metal[:, 0], s=90, color='FireBrick', label='high [Fe/H]')
plt.legend(loc=4, fontsize=14)
plt.xlabel('Temperature (K)', fontsize=16)
plt.ylabel('A(Li)', fontsize=16)
plt.savefig(directory+'li_vs_temp_binned', format='pdf')

plt.show()

