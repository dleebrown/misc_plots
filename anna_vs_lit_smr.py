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

plt.plot([4000, 9000], [4000, 9000], linewidth=3.0, linestyle='--', color='DarkCyan')
plt.scatter(anna_temp, cat_temp, c=cat_color, s=cat_size, linewidths=cat_linesize, edgecolors=cat_linecolor, label='Phot only')
plt.scatter(anna_temp_h, hyp_temp, c=hyp_color, s=hyp_size, linewidths=hyp_linesize, edgecolors=hyp_linecolor, label='Hypatia')

dev_temp_phot = anna_temp - cat_temp
print('median temp dev anna cat: '+str(np.median(dev_temp_phot)))
print('n_stars_cat temp: '+str(np.size(dev_temp_phot)))

dev_temp = anna_temp_h - hyp_temp
print('median temp dev anna hyp: '+str(np.median(dev_temp)))
print('n_stars_hyp temp: '+str(np.size(dev_temp)))

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

plt.plot([-0.8, 0.9], [-0.8, 0.9], linewidth=3.0, linestyle='--', color='DarkCyan')
plt.scatter(anna_met, cat_met, c=cat_color, s=cat_size, linewidths=cat_linesize, edgecolors=cat_linecolor, label='Phot only')
plt.scatter(anna_temp_m, hyp_met, c=hyp_color, s=hyp_size, linewidths=hyp_linesize, edgecolors=hyp_linecolor, label='Hypatia')

dev_met_phot = anna_met - cat_met
print('median [fe/h] dev anna cat: '+str(np.median(dev_met_phot)))
print('n_stars [fe/h] cat: '+str(np.size(dev_met_phot)))

dev_met = anna_temp_m - hyp_met
print('median [fe/h] dev anna hyp: '+str(np.median(dev_met)))
print('n_stars [fe/h] hyp: '+str(np.size(dev_met)))

plt.xlabel('ANNA [Fe/H] (dex)', fontsize=16)
plt.ylabel('Ref [Fe/H] (dex)', fontsize=16)
plt.xlim([0.0, 0.41])
plt.ylim([0.11, 0.6])
plt.text(0.3, 0.15, 'Omitted: 6', fontsize=16)
plt.legend(loc=2, fontsize=16)
plt.savefig(directory+'anna_vs_lit_met', format='pdf')
plt.show()
