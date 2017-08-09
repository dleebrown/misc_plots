import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
import math
import matplotlib
import pylab

"""Plot photo z vs joint fit z distributions to show how much better joint fit zs are.
"""

matplotlib.rcParams['hatch.color'] = 'DimGray'

input_data = np.loadtxt('/home/donald/Desktop/joinedz', delimiter=',', skiprows=1)

phot_z = input_data[:, 2]
joint_z = input_data[:, 1]
bins = np.linspace(1.45, 1.75, 30)

jointhist = plt.hist(joint_z, bins, facecolor='RoyalBlue', edgecolor='k', alpha=1.0, label='Joint z')
phothist = plt.hist(phot_z, bins, facecolor='None', edgecolor='k', hatch='\/\/\/\/\/', label='Phot z')

plt.tick_params(labelsize=12)
plt.xlabel(r'z',fontsize=16)
plt.ylabel(r'N',fontsize=16)
plt.xlim(1.45,1.75)
plt.legend(loc=2, prop={'size':16})
plt.savefig('redshift_distros', format='pdf',bbox_inches='tight')

plt.show()

