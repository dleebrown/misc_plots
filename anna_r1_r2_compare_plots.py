"""
generate some plots comparing different runs of anna on the SMR stars
"""

import numpy as np
import matplotlib.pyplot as plt

directory = '/home/donald/current_work/MY_THESIS/'
filename = 'compare_r1_r2.csv'
# sunname = 'jun2011_3133.fits_infer.out'

data = np.genfromtxt(directory+'/'+filename, delimiter=',', skip_header=1)

tempdata = data[:, 1]
metaldata = data[:, 3]

dtempdata = data[:, 12]
dmetaldata = data[:, 14]


nbins_metal = 20
nbins_temp = 20

n, bins, patches = plt.hist(metaldata, bins=nbins_metal)
plt.show()

n2, bins2, patches2 = plt.hist(tempdata, bins=nbins_temp)
plt.show()

"""
sun_data = np.genfromtxt(directory+'/'+sunname, skip_header=1, delimiter=',')
sun_infertemp = sun_data[:, 1]
sun_infermetal = sun_data[:, 3]
"""

plt.scatter(tempdata, metaldata)
# plt.scatter(sun_infertemp, sun_infermetal, color='Red')
# plt.scatter(5770.0, 0.0, color='Green', s=60)
plt.show()


plt.scatter(tempdata, dtempdata)
plt.show()

plt.scatter(tempdata, dmetaldata)
plt.show()

plt.scatter(metaldata, dtempdata)
plt.show()

plt.scatter(metaldata, dmetaldata)
plt.show()
