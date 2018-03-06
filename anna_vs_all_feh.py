"""copypastad together script to generate a plot comparing all the different fe/h results
"""

import numpy as np
import matplotlib.pyplot as plt

directory = '/home/donald/Desktop/PYTHON/misc_data/'

a_vs_cat = np.genfromtxt(directory+'anna_vs_catalog_tmet.csv', delimiter=',', skip_header=1)
a_vs_hyp_t = np.genfromtxt(directory+'anna_vs_hyp_t.csv', delimiter=',', skip_header=1)
a_vs_hyp_m = np.genfromtxt(directory+'anna_vs_hyp_met.csv', delimiter=',', skip_header=1)

input_data = '/home/donald/Desktop/PYTHON/misc_data/anna_robo_smr_compare.csv'

data = np.genfromtxt(input_data, delimiter=',')

temperature_data = data[1:, 1]
anna_met2 = data[1:, 3]
anna_emet = data[1:, 4]

robo_met = data[1:, 5]
robo_emet = data[1:, 6]

# define some plotting commands in common
cat_color = 'RoyalBlue'
cat_size = 145
cat_linecolor = 'k'
cat_linesize = 1.2

hyp_color = 'Gold'
hyp_size = 145
hyp_linecolor = 'k'
hyp_linesize = 1.2

# plot the ANNA metallicity vs the catalog metallicity along with the hypatia values and the robo values

anna_met = a_vs_cat[:, 3]
cat_met = a_vs_cat[:, 6]

anna_temp_m = a_vs_hyp_m[:, 3]
hyp_met = a_vs_hyp_m[:, 5]

fig = plt.figure(figsize=(8, 8))

plt.plot([-0.8, 0.9], [-0.8, 0.9], linewidth=90, linestyle='-', color='Plum', zorder=0)
plt.scatter(-0.8, 0.9, marker='s', c='Plum', s=145, linewidths=3.0, edgecolors='Plum', zorder=0, label=r'ANNA $\delta$[Fe/H]')

plt.scatter(anna_met, cat_met, marker='v', c=cat_color, s=cat_size, linewidths=cat_linesize, edgecolors=cat_linecolor, zorder=1, label='Phot only')
plt.scatter(anna_temp_m, hyp_met, marker='s', c=hyp_color, s=hyp_size, linewidths=hyp_linesize, edgecolors=hyp_linecolor, zorder=3, label='Hypatia')
plt.scatter(anna_met2, robo_met, marker='^', s=145, linewidth=1.5, edgecolor='k', facecolor='FireBrick', zorder=2, label='EW')


dev_met_phot = anna_met - cat_met
print('median [fe/h] dev anna cat: '+str(np.median(dev_met_phot)))
print('n_stars [fe/h] cat: '+str(np.size(dev_met_phot)))

dev_met = anna_temp_m - hyp_met
print('median [fe/h] dev anna hyp: '+str(np.median(dev_met)))
print('n_stars [fe/h] hyp: '+str(np.size(dev_met)))

plt.xlabel('ANNA [Fe/H] (dex)', fontsize=16)
plt.ylabel('Other [Fe/H] (dex)', fontsize=16)
plt.xlim([0.075, 0.40])
plt.ylim([-0.075, 0.575])
plt.text(0.31, -0.04, 'Omitted: 13', fontsize=16)
plt.legend(loc=2, fontsize=16)
plt.savefig(directory+'anna_vs_all', format='pdf')
plt.show()
