"""
Thesis plot showing the robospect [Fe/H] with uncertainty vs ANNA temperature
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import NullFormatter

input_data = '/home/donald/Desktop/PYTHON/misc_data/anna_robo_smr_compare.csv'

data = np.genfromtxt(input_data, delimiter=',')

temperature_data = data[1:, 1]
anna_met = data[1:, 3]
anna_emet = data[1:, 4]

robo_met = data[1:, 5]
robo_emet = data[1:, 6]


residuals = robo_met - anna_met
combine_errors = np.sqrt(robo_emet**2+anna_emet**2)

# two panel plot
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 0.4])
fig = plt.figure(figsize=(8, 8))
plt.subplots_adjust(hspace=0.001)

# plot the top panel: robo vs ANNA
roboanna = plt.subplot(gs[0])
#roboanna.errorbar(anna_met, robo_met, yerr=robo_emet, xerr=anna_emet, zorder=1, linestyle='None', linewidth=2, capsize=4.5, ecolor='RoyalBlue')
roboanna.plot([-0.4, 0.8], [-0.4, 0.8], linewidth=3.0, linestyle='--', color='IndianRed', zorder=0)
roboanna.scatter(anna_met, robo_met, marker='o', s=60, linewidth=1.9, edgecolor='RoyalBlue', facecolor='White', zorder=2)

plt.ylabel('EW [Fe/H] (dex)', fontsize=14)
plt.tick_params(axis='both', top='off', right='off', bottom='off', labeltop='off', labelright='off', labelbottom='off')
plt.tick_params(axis='both', which='major', labelsize=12)


# adjust plot limits
plt.xlim([0.08, 0.40])
plt.ylim([-0.08, 0.475])

residplot = plt.subplot(gs[1], sharex=roboanna)
residplot.errorbar(anna_met, residuals, yerr=combine_errors, zorder=3, linestyle='None', linewidth=2, capsize=4.5, ecolor='IndianRed')
residplot.plot([-0.4, 0.8], [0.0, 0.0], linewidth=3.0, linestyle='--', color='RoyalBlue')
residplot.scatter(anna_met, residuals, linewidth=1.9, edgecolor='IndianRed', facecolor='White', s=60, marker='o', zorder=4)

# add labels
plt.ylabel(r'$\Delta$EW [Fe/H] (dex)', fontsize=14)
plt.xlabel('ANNA [Fe/H]', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)


# adjust plot limits
plt.xlim([0.075, 0.39])
plt.ylim([-0.72, 0.72])

# limits chosen such that 5 points omitted


plt.savefig('/home/donald/Desktop/robo_anna_metal_compare', format='pdf', bbox_inches='tight')

plt.show()