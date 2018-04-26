import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches

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
    noise_to_add = np.random.randn(1, np.size(input_y))
    return noise_level*noise_to_add


# first generate the continuum at arbitrary resolution

num_px = 2000
pixel_num = np.arange(0, num_px, 1)
cont_level = np.ones((1, num_px))

# now generate a single line 33% of the way into the spectrum
cont_level[0, :] = cont_level[0, :] - gaussian(num_px*0.33, 70.0, pixel_num, 8.0)

# now generate a blend of two lines 66% of the way into the spectrum
cont_level[0, :] = cont_level[0, :] - gaussian(num_px*0.62, 70.0, pixel_num, 10.0)
cont_level[0, :] = cont_level[0, :] - gaussian(num_px*0.776, 80.0, pixel_num, 5.0)


# plot the super-high-res spectrum as a check

fig = plt.plot(pixel_num, cont_level[0, :])

plt.show()

# now interpolate the super-high-res spectrum onto a coarser grid and plot as a check
coarse_grid, coarse_spec = downsample(pixel_num, cont_level[0, :], 0.02)

fig2 = plt.plot(coarse_grid, coarse_spec)

plt.show()

# now add noise to the downsampled spectrum and plot as a check

add_noise = noisespec(coarse_spec, 0.001)

fig3 = plt.plot(coarse_grid, coarse_spec+add_noise[0, :])

plt.show()


# control some of the parameters in common between the plots
fontsize_axis = 16
fontsize_labels = 16
xlabel = 'Wavelength'
ylabel = 'Normalized Flux'
xrange = [0.0, 1900]
spec_color = 'DarkCyan'
spec_linewidth = 3.0
spec_order = 1
cont_color = 'DimGray'
cont_width = 3.0
cont_style = '--'
cont_zorder = 0

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
