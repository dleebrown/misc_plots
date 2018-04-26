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


plt.errorbar(temperature_data, robo_met, yerr=robo_emet, zorder=1, linestyle='None', linewidth=2, capsize=4.5, ecolor='RoyalBlue')
plt.scatter(temperature_data, robo_met, marker='o', s=45, linewidth=1.8, edgecolor='RoyalBlue', facecolor='White', zorder=2)

# add labels
plt.ylabel('EW [Fe/H] (dex)', fontsize=14)
plt.xlabel('ANNA Temperature (K)', fontsize=14)

# adjust plot limits
#plt.ylim([0.75, 1.05])


plt.savefig('/home/donald/Desktop/robo_metal_vs_anna_temp', format='pdf', bbox_inches='tight')

plt.show()