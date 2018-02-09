"""Some plots comparing the ANNA SMR ensemble with various subsamples snagged from previous people's work
"""

import numpy as np
import matplotlib.pyplot as plt

directory = '/home/donald/current_work/MY_THESIS/anna_vs_lit/'

a_vs_cat = np.genfromtxt(directory+'anna_vs_catalog_tmet.csv', delimiter=',', skip_header=1)
a_vs_hyp_t = np.genfromtxt(directory+'anna_vs_hyp_t.csv', delimiter=',', skip_header=1)
a_vs_hyp_m = np.genfromtxt(directory+'anna_vs_hyp_met.csv', delimiter=',', skip_header=1)

# define some plotting commands in common
cat_color = 'RoyalBlue'
cat_size = 145
cat_linecolor = 'White'
cat_linesize = 1.5

hyp_color = 'FireBrick'
hyp_size = 120
hyp_linecolor = 'k'
hyp_linesize = 1.5

# plot the ANNA temperature vs the catalog temperature (phot+spec)
anna_temp = a_vs_cat[:, 1]
cat_temp = a_vs_cat[:, 5]

anna_temp_h = a_vs_hyp_t[:, 1]
hyp_temp = a_vs_hyp_t[:, 5]

plt.scatter(anna_temp, cat_temp, c=cat_color, s=cat_size, linewidths=cat_linesize, edgecolors=cat_linecolor, label='Phot only')
plt.scatter(anna_temp_h, hyp_temp, c=hyp_color, s=hyp_size, linewidths=hyp_linesize, edgecolors=hyp_linecolor, label='Hypatia')

plt.xlabel('ANNA Temp (K)', fontsize=16)
plt.ylabel('Ref Temp (K)', fontsize=16)
plt.xlim([5625, 6400])
plt.ylim([5750, 6500])
plt.text(6200, 5820, 'Omitted: 5', fontsize=16)
plt.legend(loc=2, fontsize=16)
plt.savefig(directory+'anna_vs_lit_temp', format='pdf')
plt.show()

# plot the ANNA metallicity vs the catalog metallicity along with the hypatia values

anna_met = a_vs_cat[:, 3]
cat_met = a_vs_cat[:, 6]

anna_temp_m = a_vs_hyp_m[:, 3]
hyp_met = a_vs_hyp_m[:, 5]

plt.scatter(anna_met, cat_met, c=cat_color, s=cat_size, linewidths=cat_linesize, edgecolors=cat_linecolor, label='Phot only')
plt.scatter(anna_temp_m, hyp_met, c=hyp_color, s=hyp_size, linewidths=hyp_linesize, edgecolors=hyp_linecolor, label='Hypatia')

plt.xlabel('ANNA [Fe/H] (dex)', fontsize=16)
plt.ylabel('Ref [Fe/H] (dex)', fontsize=16)
plt.xlim([0.0, 0.41])
plt.ylim([0.11, 0.6])
plt.text(0.3, 0.15, 'Omitted: 6', fontsize=16)
plt.legend(loc=2, fontsize=16)
plt.savefig(directory+'anna_vs_lit_met', format='pdf')
plt.show()
