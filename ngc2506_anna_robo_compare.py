"""imports a csv file to plot robospect and anna results. for AAS 2018
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import NullFormatter

# import the data
imported = np.genfromtxt('latex_converted.csv', delimiter=',')
templist = []
annalist = []
robolist = []
deltalist = []
# remove the nans from robo or anna columns and sort into different lists
for i in range(len(imported[:, 0])):
    current_star = list(imported[i, :])
    if str(current_star[2]) != 'nan' and str(current_star[3]) != 'nan' and str(current_star[10]) != 'nan':
        templist.append(current_star[10])
        annalist.append(current_star[2])
        robolist.append(current_star[3])
        deltalist.append(current_star[2]-current_star[3])

# work on the plot now

resid_hist_color = 'LightSkyBlue'
abund_hist_color = 'LightSkyBlue'
resid_scatter_color = 'RoyalBlue'
abund_scatter_color = 'FireBrick'

nullfmt = NullFormatter()

gs = gridspec.GridSpec(2, 1, height_ratios=[1.618, 1])
fig = plt.figure(figsize=(11, 4.5))
plt.subplots_adjust(hspace=0.001)

abundances = plt.subplot(gs[0])
abundances.scatter(templist, annalist, s=45, color=abund_scatter_color, zorder=1)

residuals = plt.subplot(gs[1], sharex=abundances)
residuals.scatter(templist, deltalist, s=45, color=resid_scatter_color, zorder=2)

abundances.axhline(-0.26, linewidth=3.0, linestyle='--', color=abund_hist_color, zorder=0)
residuals.axhline(0.0, linewidth=3.0, linestyle='--', color=resid_hist_color, zorder=0)

div1 = make_axes_locatable(abundances)
div2 = make_axes_locatable(residuals)

hist_abund = div1.append_axes("right", 1.3, pad=0.075)
hist_resid = div2.append_axes("right", 1.3, pad=0.075)

hist_abund.xaxis.set_major_formatter(nullfmt)
hist_resid.xaxis.set_major_formatter(nullfmt)
hist_abund.yaxis.set_major_formatter(nullfmt)
hist_resid.yaxis.set_major_formatter(nullfmt)

hist_resid.xaxis.set_ticks_position('none')
hist_resid.yaxis.set_ticks_position('none')
hist_abund.yaxis.set_ticks_position('none')

abund_binwidth = 0.025
resid_binwidth = 0.06

abund_max = np.max(annalist)
abund_min = np.min(annalist)

resid_max = np.max(deltalist)
resid_min = np.min(deltalist)

"""
abund_lim = (int((abund_max-abund_min)/abund_binwidth) + 1)*abund_binwidth
resid_lim = (int(resid_xymax/resid_binwidth)+1)*resid_binwidth
"""

abund_bins = np.arange(abund_min, abund_max + abund_binwidth, abund_binwidth)
resid_bins = np.arange(resid_min, resid_max + resid_binwidth, resid_binwidth)


residuals_ylim = [-0.25, 0.25]
abundances_ylim = [-0.45, -0.1]

abundances_xlim = [4750, 5550]

#abundances.yaxis.set_major_locator(plt.MaxNLocator(5))

abundances.set_yticks([-0.4, -0.35, -0.3, -0.25, -0.20, -0.15])
residuals.set_yticks([-0.2, 0.0, 0.2])


abundances.set_ylabel('[Fe/H]', fontsize=13)
residuals.set_xlabel(r'Photometric T$_{eff}$ (K)', fontsize=13)

residuals.set_ylabel(r'$\Delta$ [Fe/H]', fontsize=13)

abundances.tick_params(labelsize=12)
residuals.tick_params(labelsize=12)

abundances.set_xlim(abundances_xlim)
abundances.set_ylim(abundances_ylim)

residuals.set_ylim(residuals_ylim)

hist_abund.hist(annalist, bins=abund_bins, normed=True, rwidth=0.75, color=abund_hist_color, orientation='horizontal')
hist_resid.hist(deltalist, bins=resid_bins, normed=True, rwidth=0.75, color=resid_hist_color, orientation='horizontal')

hist_abund.set_ylim(abundances_ylim)
hist_resid.set_ylim(residuals_ylim)


hist_abund.set_axis_off()
hist_resid.set_axis_off()



"""

hist_abund.scatter(templist, annalist)
hist_resid.scatter(templist, deltalist)

"""

plt.savefig('ngc2506_annaplot', format='pdf', bbox_inches='tight')

plt.show()

