"""make two multi-panel plots showing the impact of changing different atmospheric parameters on final spectrum"""

# first read in the data

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

directory = '/home/donald/Desktop/PYTHON/misc_data/'
solar_subdir = 'all_sun_models/'

baseline_model = np.genfromtxt(directory+solar_subdir+'og_sun')


# define some standardized plot params
plotting_xrange = [6702.6, 6706.5]
plotting_yrange = [0.53, 1.035]
ylabel = 'Normalized Flux'
xlabel = 'Wavelength (Angstroms)'
fsize = 12

base_ls = '-'
base_lw = 2.5
base_lc = 'RoyalBlue'

mod_ls = ':'
mod_lw = 3.0
mod_ls2 = '-'
mod_lw2 = 1.0
mod_lc = 'FireBrick'

# now plot the baseline model in a simple plot to set plotting ranges
plt.figure(figsize=(7, 4))
plt.plot(baseline_model[:, 0], baseline_model[:, 1], color=base_lc, linewidth=base_lw, linestyle=base_ls)
plt.xlim(plotting_xrange)
plt.ylim(plotting_yrange)

plt.xlabel(xlabel, fontsize=fsize)
plt.ylabel(ylabel, fontsize=fsize)

plt.show()

# looks good so now we can move on - make the plot of changing the atmospheric parameters

# read in the data first

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(10, 5))
f.subplots_adjust(hspace=0, wspace=0)

hot_model = np.genfromtxt(directory+solar_subdir+'hot_sun')
lowgrav_model = np.genfromtxt(directory+solar_subdir+'lowgrav_sun')
metalrich_model = np.genfromtxt(directory+solar_subdir+'metalrich_sun')
turbulent_model = np.genfromtxt(directory+solar_subdir+'turbulent_sun')

# plot the baseline model
ax1.plot(baseline_model[:, 0], baseline_model[:, 1], color=base_lc, linewidth=base_lw, linestyle=base_ls, label='Sun')
ax1.plot(hot_model[:, 0], hot_model[:, 1], color=mod_lc, linewidth=mod_lw, linestyle=mod_ls, label='T+100 K')
ax1.plot(hot_model[:, 0], hot_model[:, 1], color=mod_lc, linewidth=mod_lw2, linestyle=mod_ls2)
ax1.legend(loc=4, fontsize=10, labelspacing=-0.05)
ax1.set_xticks([6703, 6704, 6705, 6706])

ax2.plot(baseline_model[:, 0], baseline_model[:, 1], color=base_lc, linewidth=base_lw, linestyle=base_ls, label='Sun')
ax2.plot(lowgrav_model[:, 0], lowgrav_model[:, 1], color=mod_lc, linewidth=mod_lw, linestyle=mod_ls, label='log(g)-1.4 dex')
ax2.plot(lowgrav_model[:, 0], lowgrav_model[:, 1], color=mod_lc, linewidth=mod_lw2, linestyle=mod_ls2)
ax2.legend(loc=4, fontsize=10, labelspacing=-0.05)
ax2.set_xticks([6703, 6704, 6705, 6706])

ax3.plot(baseline_model[:, 0], baseline_model[:, 1], color=base_lc, linewidth=base_lw, linestyle=base_ls, label='Sun')
ax3.plot(metalrich_model[:, 0], metalrich_model[:, 1], color=mod_lc, linewidth=mod_lw, linestyle=mod_ls, label='[Fe/H]+0.2 dex')
ax3.plot(metalrich_model[:, 0], metalrich_model[:, 1], color=mod_lc, linewidth=mod_lw2, linestyle=mod_ls2)
ax3.legend(loc=4, fontsize=10, labelspacing=-0.05)
ax3.set_xticks([6703, 6704, 6705, 6706])

ax4.plot(baseline_model[:, 0], baseline_model[:, 1], color=base_lc, linewidth=base_lw, linestyle=base_ls, label='Sun')
ax4.plot(turbulent_model[:, 0], turbulent_model[:, 1], color=mod_lc, linewidth=mod_lw, linestyle=mod_ls, label=r'$v_t$+0.46 km/s')
ax4.plot(turbulent_model[:, 0], turbulent_model[:, 1], color=mod_lc, linewidth=mod_lw2, linestyle=mod_ls2)
ax4.legend(loc=4, fontsize=10, labelspacing=-0.05)
ax4.set_xticks([6703, 6704, 6705, 6706])

ax1.set_xlim(plotting_xrange)
ax2.set_xlim(plotting_xrange)
ax3.set_xlim(plotting_xrange)
ax4.set_xlim(plotting_xrange)

ax1.set_ylim(plotting_yrange)
ax2.set_ylim(plotting_yrange)
ax3.set_ylim(plotting_yrange)
ax4.set_ylim(plotting_yrange)

ax1.set_ylabel('Rel. Flux')
ax3.set_ylabel('Rel. Flux')
ax3.set_xlabel(r'$\lambda$ (Angstroms)')
ax4.set_xlabel(r'$\lambda$ (Angstroms)')

plt.savefig(directory+'atm_alter_synth', format='pdf')
plt.show()

# okay now make a similar plot for the other parameters

# read in the data first

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(10, 5))
f.subplots_adjust(hspace=0, wspace=0)

rot_model = np.genfromtxt(directory+solar_subdir+'rotvel_sun')
rad_model = np.genfromtxt(directory+solar_subdir+'radvel_sun')
lowres_model = np.genfromtxt(directory+solar_subdir+'lowres_sun')
sn_model = np.genfromtxt(directory+solar_subdir+'lowres_sun')


# plot the baseline model
ax1.plot(baseline_model[:, 0], baseline_model[:, 1], color=base_lc, linewidth=base_lw, linestyle=base_ls, label='Sun')
ax1.plot(rot_model[:, 0], rot_model[:, 1], color=mod_lc, linewidth=mod_lw, linestyle=mod_ls, label=r'$V_{rot}$+15 km/s')
ax1.plot(rot_model[:, 0], rot_model[:, 1], color=mod_lc, linewidth=mod_lw2, linestyle=mod_ls2)
ax1.legend(loc=4, fontsize=10, labelspacing=-0.05)
ax1.set_xticks([6703, 6704, 6705, 6706])

ax2.plot(baseline_model[:, 0], baseline_model[:, 1], color=base_lc, linewidth=base_lw, linestyle=base_ls, label='Sun')

ax2.plot(baseline_model[:, 0]+0.44, baseline_model[:, 1], color=mod_lc, linewidth=mod_lw, linestyle=mod_ls, label=r'$V_{rad}$+20 km/s')
ax2.plot(baseline_model[:, 0]+0.44, baseline_model[:, 1], color=mod_lc, linewidth=mod_lw2, linestyle=mod_ls2)
ax2.legend(loc=4, fontsize=10, labelspacing=-0.05)
ax2.set_xticks([6703, 6704, 6705, 6706])

ax3.plot(baseline_model[:, 0], baseline_model[:, 1], color=base_lc, linewidth=base_lw, linestyle=base_ls, label='Sun')
ax3.plot(lowres_model[:, 0], lowres_model[:, 1], color=mod_lc, linewidth=mod_lw, linestyle=mod_ls, label='R~13,000')
ax3.plot(lowres_model[:, 0], lowres_model[:, 1], color=mod_lc, linewidth=mod_lw2, linestyle=mod_ls2)
ax3.legend(loc=4, fontsize=10, labelspacing=-0.05)
ax3.set_xticks([6703, 6704, 6705, 6706])

# now add noise to the lowres model to simulate a real spectrum

noise = np.random.normal(loc=0.0, scale=(1.0/100), size=(np.size(sn_model[:, 1])))

ax4.plot(baseline_model[:, 0], baseline_model[:, 1], color=base_lc, linewidth=base_lw, linestyle=base_ls, label='Sun')
ax4.plot(sn_model[:, 0], sn_model[:, 1]+noise, color=mod_lc, linewidth=mod_lw, linestyle=mod_ls, label='SN = 100')
ax4.plot(sn_model[:, 0], sn_model[:, 1]+noise, color=mod_lc, linewidth=mod_lw2, linestyle=mod_ls2)
ax4.legend(loc=4, fontsize=10, labelspacing=-0.05)
ax4.set_xticks([6703, 6704, 6705, 6706])


ax1.set_xlim(plotting_xrange)
ax2.set_xlim(plotting_xrange)
ax3.set_xlim(plotting_xrange)
ax4.set_xlim(plotting_xrange)

ax1.set_ylim(plotting_yrange)
ax2.set_ylim(plotting_yrange)
ax3.set_ylim(plotting_yrange)
ax4.set_ylim(plotting_yrange)

ax1.set_ylabel('Rel. Flux')
ax3.set_ylabel('Rel. Flux')
ax3.set_xlabel(r'$\lambda$ (Angstroms)')
ax4.set_xlabel(r'$\lambda$ (Angstroms)')

plt.savefig(directory+'kin_alter_synth', format='pdf')
plt.show()