# plot the results from ANNA_test.py in a 4-panel vertical plot


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import NullFormatter

directory = '/home/donald/Desktop/PYTHON/misc_data/'

test_data = np.genfromtxt(directory+'test_stats.615.out', delimiter=',', skip_header=1)

true_temp = test_data[:, 1]
true_grav = test_data[:, 2]
true_met = test_data[:, 3]
true_vt = test_data[:, 4]

delta_temp = test_data[:, 6]
delta_grav = test_data[:, 7]
delta_met = test_data[:, 8]-0.02
delta_vt = test_data[:, 9]

nullfmt = NullFormatter()

gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 1])
fig = plt.figure(figsize=(12, 10))
plt.subplots_adjust(hspace=0.701)

tempplot = plt.subplot(gs[0])
tempplot.scatter(true_temp, delta_temp, s=15, color='RoyalBlue', zorder=1)
tempplot.set_xlim([5200, 5700])
tempplot.set_ylim([-250, 250])
tempplot.set_xlabel(r'$T_{eff}$ (K)', fontsize=16)
tempplot.set_ylabel(r'$\Delta T_{eff}$ (K)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)


gravplot = plt.subplot(gs[1])
gravplot.scatter(true_grav, delta_grav, s=15, color='RoyalBlue', zorder=1)
gravplot.set_xlim([3.0, 4.5])
gravplot.set_ylim([-0.5, 0.5])
gravplot.set_ylabel(r'$\Delta log(g)$ (dex)', fontsize=16)
gravplot.set_xlabel(r'$log(g)$ (dex)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14)




metplot = plt.subplot(gs[2])
metplot.scatter(true_met, delta_met, s=15, color='RoyalBlue', zorder=1)
metplot.set_xlim([-0.20, 0.20])
metplot.set_ylim([-0.15, 0.15])
metplot.set_ylabel(r'$\Delta$[Fe/H] (dex)', fontsize=16)
metplot.set_xlabel(r'[Fe/H] (dex)', fontsize=16)


plt.tick_params(axis='both', which='major', labelsize=14)


plt.savefig('../anna_test_results', format='pdf')
plt.show()
