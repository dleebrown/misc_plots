"""imports a csv file to plot robospect, ispec, and anna results as a function of SN. for AAS 2018
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

input_data = np.genfromtxt('../misc_data/annasn_TEST.csv', delimiter=',')
input_data = input_data[1:, :]

sn_values = input_data[:, 0]
anna_values = input_data[:, 4]
robo_values = input_data[:, 5]
ispec_values = input_data[:, 6]
anna200_values = input_data[:, 7]

fig, (splot2, splot1) = plt.subplots(2, 1, sharex=True, figsize=(13, 4.5), gridspec_kw={'height_ratios': [1, 4]})
fig.subplots_adjust(hspace=0.1)

annacolor = 'RoyalBlue'
anna200color = 'DimGray'
robocolor = 'SeaGreen'
ispeccolor = 'FireBrick'
edgecolor = 'White'
edgwidth = 3
linestyle = '-'

#plt.yscale('log')

# stick the data on the bottom plot (omitting outlier)
linesize = 4
splot1.plot(sn_values, anna_values, c=annacolor, linewidth=linesize, linestyle=linestyle, label='ANNA (varied SN)', zorder=0)
splot1.plot(sn_values, anna200_values, c=anna200color, linewidth=linesize, linestyle=linestyle, label='ANNA (SN=200)', zorder=0)
splot1.plot(sn_values[:-1], robo_values[:-1], c=robocolor, linewidth=linesize, linestyle=linestyle, label='ROBOSPECT (EW)', zorder=0)
# plt.plot(sn_values, ispec_values, c=ispeccolor, linewidth=linesize, linestyle=linestyle, label='iSPEC (synthesis)', zorder=0)

pointsize = 270
pointstyle = 's'
splot1.scatter(sn_values, anna_values, c=annacolor, marker=pointstyle, edgecolor=edgecolor, linewidth=edgwidth, s=pointsize, zorder=1)
splot1.scatter(sn_values, anna200_values, c=anna200color, marker=pointstyle, edgecolor=edgecolor, linewidth=edgwidth, s=pointsize, zorder=1)
splot1.scatter(sn_values[:-1], robo_values[:-1], c=robocolor, marker=pointstyle, edgecolor=edgecolor, linewidth=edgwidth, s=pointsize, zorder=1)
# plt.scatter(sn_values, ispec_values, c=ispeccolor, marker=pointstyle, edgecolor=edgecolor, linewidth=edgwidth, s=pointsize, zorder=1)

plt.legend(bbox_to_anchor=(0.98, 1.24), fontsize=16, frameon=False)

#splot.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

# now plot the outlier on the top plot (with no lines)
#splot2.plot(sn_values[-1], robo_values[-1], c=robocolor, linewidth=linesize, linestyle=linestyle, label='ROBOSPECT (EW)', zorder=0)
splot2.scatter(sn_values[-1], robo_values[-1], c=robocolor, marker=pointstyle, edgecolor=edgecolor, linewidth=edgwidth, s=pointsize, zorder=1)

# show different ranges for the plots
splot2.set_ylim(0.33, 0.38)
splot1.set_ylim(0.00, 0.13)

xvalues = [10, 25, 50, 100, 200]
yvalues1 = [0.02, 0.05, 0.08, 0.11]
splot1.set_yticks(yvalues1)

yvalues2 = [0.36]
splot2.set_yticks(yvalues2)

# now add a dotted line from the last point on the bottom to the outlier point (stick under other points)
splot1.plot((sn_values[-2], sn_values[-1]), (robo_values[-2], 0.157), linestyle=':', linewidth=4, c=robocolor, zorder=0, clip_on=False)
splot1.scatter(sn_values[-1], 0.1559, c='none', marker=pointstyle, edgecolor='White', linewidth=edgwidth, s=pointsize, zorder=3, clip_on=False)

splot2.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
splot2.spines['bottom'].set_visible(False)
splot1.spines['top'].set_visible(False)
#splot2.xaxis.tick_top()
splot2.tick_params(labeltop='off')  # don't put tick labels at the top
splot1.xaxis.tick_bottom()
splot2.tick_params(labelsize=16)

plt.xticks(xvalues, rotation=0, ha='center', fontsize=16)
plt.yticks(fontsize=16)
plt.ylabel('            MAD [Fe/H]', fontsize=16)
plt.xlabel('Signal-to-Noise', fontsize=16)

# this portion of code is from: https://matplotlib.org/2.0.0/examples/pylab_examples/broken_axis.html
d = .01  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
scale_xform = 4

kwargs = dict(transform=splot2.transAxes, color='k', linewidth=3.0, clip_on=False)
splot2.plot((-d, +d), (-d*scale_xform, +d*scale_xform), **kwargs)        # top-left diagonal
splot2.plot((1 - d, 1 + d), (-d*scale_xform, +d*scale_xform), **kwargs)  # top-right diagonal

kwargs.update(transform=splot1.transAxes)  # switch to the bottom axes
splot1.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
splot1.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagona
# end copied code


plt.savefig('anna_snplot', format='pdf',bbox_inches='tight')


plt.show()

