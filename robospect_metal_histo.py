"""makes a histogram of robospect [fe/h] values
"""

import numpy as np
import matplotlib.pyplot as plt

directory = '/home/donald/Desktop/'
filename = 'PYTHON/misc_data/anna_robo_smr_compare.csv'
# sunname = 'jun2011_3133.fits_infer.out'

data = np.genfromtxt(directory+filename, delimiter=',')

temperature_data = data[1:, 1]
anna_met = data[1:, 3]
anna_emet = data[1:, 4]

robo_met = data[1:, 5]
robo_emet = data[1:, 6]

nbins_metal = 20
#nbins_temp = 20

n, bins, patches = plt.hist(robo_met, bins=nbins_metal, color='DarkSlateGray', edgecolor='White', linewidth=3.5)
plt.xlabel('EW [Fe/H]', fontsize=16)
plt.ylabel('N Stars', fontsize=16)
plt.ylim([0, 13])
plt.xlim([-0.1, 0.72])
plt.savefig(directory+'robo_metal_distro', format='pdf')
plt.show()
