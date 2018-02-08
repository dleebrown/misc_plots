"""
some simple plots showing the distributions of metallicity and temperature for the SMR stars
"""

import numpy as np
import matplotlib.pyplot as plt

data_file = '/home/donald/current_work/MY_THESIS/weighted_temp_met_SMR.csv'

data_in = np.genfromtxt(data_file, delimiter=',', skip_header=1)

weighted_temps = data_in[:, 1]
e_temps = data_in[:, 2]

weighted_mets = data_in[:, 3]
e_mets = data_in[:, 4]

nbins_temp = 15
nbins_met = 15

n, bins, patches = plt.hist(weighted_temps, bins=nbins_temp)
plt.show()

n2, bins2, patches2 = plt.hist(weighted_mets, bins=nbins_met)
plt.show()
