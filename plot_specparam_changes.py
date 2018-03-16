"""make two multi-panel plots showing the impact of changing different atmospheric parameters on final spectrum"""

# first read in the data

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

directory = '/home/donald/Desktop/PYTHON/misc_data/'
solar_subdir = 'all_sun_models/'

baseline_model = np.genfromtxt(directory+solar_subdir+'og_sun')


# define some standardized plot params
plotting_xrange = [6702.6, 6705.9]
plotting_yrange = [0.63, 1.022]
ylabel = 'Normalized Flux'
xlabel = 'Wavelength (Angstroms)'
fsize = 12

base_ls = '-'
base_lw = 3.0
base_lc = 'RoyalBlue'

mod_ls = '--'
mod_lw = 3.0
mod_lc = 'FireBrick'

# now plot the baseline model in a simple plot to set plotting ranges
plt.figure(figsize=(7, 4))
plt.plot(baseline_model[:, 0], baseline_model[:, 1], color=base_lc, linewidth=base_lw, linestyle=base_ls)
plt.xlim(plotting_xrange)
plt.ylim(plotting_yrange)

plt.xlabel(xlabel, fontsize=fsize)
plt.ylabel(ylabel, fontsize=fsize)

plt.show()