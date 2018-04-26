"""reads in a file containing a bunch of ANNA outputs and creates histograms of temperature and metallicity
also creates a plot of metallicity vs temperature
also reads in a file of solar outputs and plots the sun on the temp vs metal plot
also plots the canonical solar values on the temp vs metal plot
"""

import numpy as np
import matplotlib.pyplot as plt

directory = '/home/donald/current_work/MY_THESIS/thesis_anna_infer_r1'
filename = 'concatenated_outputs'
sunname = 'jun2011_3133.fits_infer.out'

data = np.genfromtxt(directory+'/'+filename, skip_header=0)

tempdata = data[:, 1]
metaldata = data[:, 3]

nbins_metal = 20
nbins_temp = 20

n, bins, patches = plt.hist(metaldata, bins=nbins_metal)
plt.show()

n2, bins2, patches2 = plt.hist(tempdata, bins=nbins_temp)
plt.show()

sun_data = np.genfromtxt(directory+'/'+sunname, skip_header=1, delimiter=',')
sun_infertemp = sun_data[:, 1]
sun_infermetal = sun_data[:, 3]

plt.scatter(tempdata, metaldata)
plt.scatter(sun_infertemp, sun_infermetal, color='Red')
plt.scatter(5770.0, 0.0, color='Green', s=60)
plt.show()
