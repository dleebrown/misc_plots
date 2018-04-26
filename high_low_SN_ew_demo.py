"""
Thesis plot with two panels: a mock spectrum showing a clean line and blend at high sn, and the same spectrum at low SN
EW is diagrammed as well
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import NullFormatter

# define a function that takes in a 1D array of x-values and computes a gaussian profile
def gaussian(meanval, sigval, inputx, scalefactor):
    gcoeff = 1/(sigval*math.sqrt(2*math.pi))
    gexp = - 0.5 * ((inputx - meanval)/sigval)**2
    output = gcoeff * np.exp(gexp) * scalefactor
    return output

# define a function to downsample spectrum onto coarser grid
# coarseness should be (0, 1.0] where 1.0 is same as input grid
def downsample(input_x, input_y, coarseness):
    step_size = 1.0/coarseness
    output_xgrid = np.arange(0, np.size(input_x), step_size)
    interp_y = np.interp(output_xgrid, input_x, input_y)
    return output_xgrid, interp_y

# function to randomly add noise to spectrum
# noise level is the factor to scale normally distributed noise by
def noisespec(input_y, noise_level):
    np.random.seed(277)
    noise_to_add = np.random.randn(1, np.size(input_y))
    return noise_level*noise_to_add


# first generate the continuum at arbitrary resolution

num_px = 2000
pixel_num = np.arange(0, num_px, 1)
cont_level = np.ones((1, num_px))

# now generate a single line 33% of the way into the spectrum
cont_level[0, :] = cont_level[0, :] - gaussian(num_px*0.33, 60.0, pixel_num, 20.0)

# now generate a blend of two lines 66% of the way into the spectrum
cont_level[0, :] = cont_level[0, :] - gaussian(num_px*0.62, 50.0, pixel_num, 16.0)
cont_level[0, :] = cont_level[0, :] - gaussian(num_px*0.69, 60.0, pixel_num, 12.0)

# now interpolate the super-high-res spectrum onto a coarser grid and plot as a check
coarse_grid, coarse_spec = downsample(pixel_num, cont_level[0, :], 0.02)

# now generate two separate noise solutions: 1 with high noise, 1 with low noise

add_low_noise = noisespec(coarse_spec, 0.002)

add_high_noise = noisespec(coarse_spec, 0.02)

# control some of the parameters in common between the plots
fontsize_axis = 16
fontsize_labels = 16
xrange = [0.0, 1900]
true_spec_color = 'DodgerBlue'
measured_spec_color = 'FireBrick'
spec_linewidth = 3.5
spec_order = 2
true_cont_color = 'DimGray'
fit_cont_color = 'k'
cont_width = 3.0
cont_style = '--'
cont_zorder = 0

# two panel plot
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 1])
fig = plt.figure(figsize=(11, 6))
plt.subplots_adjust(hspace=0.001)

# plot the high-SN example
highsn = plt.subplot(gs[0])
highsn.plot(coarse_grid, coarse_spec+add_low_noise[0, :], linewidth=spec_linewidth, color=measured_spec_color, zorder=1)
highsn.plot([0, 3000], [1.0, 1.0], linewidth=cont_width, color=true_cont_color, linestyle=cont_style, zorder=cont_zorder+1)
highsn.plot(pixel_num, cont_level[0, :], linewidth=spec_linewidth, color=true_spec_color, linestyle='-.', zorder=4)
highsn.plot([0, 3000], [1.0, 1.0], linewidth=cont_width, color=fit_cont_color, zorder=cont_zorder)


# remove axis ticks on high-sn, change plot lim
plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')
plt.ylim([0.75, 1.05])

# plot low-sn plot below
lowsn = plt.subplot(gs[1], sharex=highsn)
lowsn.plot(pixel_num, cont_level[0, :] - (1-np.arange(0.98, 1.0, 0.02/3000)[:2000]), linewidth=spec_linewidth, color=true_spec_color, linestyle='-.', zorder=4, label='True Spectrum')
lowsn.plot(coarse_grid, coarse_spec+add_high_noise[0, :]-0.02, linewidth=spec_linewidth, color=measured_spec_color, zorder=3, label='Measured Spectrum')
lowsn.plot([0, 3000], [1.0, 1.0], linewidth=cont_width, color=fit_cont_color, zorder=cont_zorder, label='Fit Continuum')
lowsn.plot([0, 3000], [0.98, 1.0], linewidth=cont_width, color=true_cont_color, linestyle=cont_style, zorder=cont_zorder, label='True Continuum')

# remove ticks here too
plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')


# add labels
plt.ylabel('                             Normalized flux', fontsize=fontsize_labels)
plt.xlabel('Wavelength', fontsize=fontsize_labels)

# add legend
plt.legend(bbox_to_anchor=(1.005, 0.28), frameon=False, prop={'size': 12}, ncol=2)

# add labels for high and low SN to the subplots

plt.text(20, 0.76, 'Low SN', fontsize=16)

plt.text(20, 1.062, 'High SN', fontsize=16)

# add labels to the lines in the top plot
plt.text(550, 1.12, 'Isolated line', fontsize=12)
plt.text(1150, 1.12, 'Blended lines', fontsize=12)

# adjust plot limits
plt.xlim(xrange)
plt.ylim([0.75, 1.05])

plt.savefig('/home/donald/Desktop/high_low_sn_ew_demo', format='pdf', bbox_inches='tight')

plt.show()




"""
# for the first plot show what an equivalent width looks like on the first line

fig4, splot = plt.subplots()
splot.plot(coarse_grid, coarse_spec+add_noise[0, :], linewidth=spec_linewidth, color=spec_color, zorder=spec_order)
splot.plot([0, 3000], [1.0, 1.0], linewidth=cont_width, color=cont_color, linestyle=cont_style, zorder=cont_zorder)
splot.add_patch(patches.Rectangle((552.5, 0.0), 215, 1.0, hatch='////', linewidth=2, edgecolor='FireBrick', facecolor='None'))

plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')

splot.set_xlabel(xlabel, fontsize=fontsize_labels)
splot.set_ylabel(ylabel, fontsize=fontsize_labels)

splot.set_xlim(xrange)

plt.savefig('ew_demo', format='pdf', bbox_inches='tight')

plt.show()

# for the second plot show how synth works by overplotting the original high-res spectrum
fig5, splot = plt.subplots()
splot.plot(coarse_grid, coarse_spec+add_noise[0, :], linewidth=spec_linewidth, color=spec_color, zorder=spec_order)
splot.plot([0, 3000], [1.0, 1.0], linewidth=cont_width, color=cont_color, linestyle=cont_style, zorder=cont_zorder)
# add some arbitrary scaling to make the fit more apparent
cont_level[0, 0:int(np.size(cont_level)*0.5)] = cont_level[0, 0:int(np.size(cont_level)*0.5)]*1.15-0.15
cont_level[0, int(np.size(cont_level)*0.5):] = cont_level[0, int(np.size(cont_level)*0.5):]*0.85+0.15

splot.plot(pixel_num, cont_level[0, :], linewidth=2, color='FireBrick', linestyle='-.', zorder=3)

plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')

splot.set_xlabel(xlabel, fontsize=fontsize_labels)
splot.set_ylabel(ylabel, fontsize=fontsize_labels)

splot.set_xlim(xrange)

plt.savefig('synth_demo', format='pdf', bbox_inches='tight')

plt.show()
"""