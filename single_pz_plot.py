from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.gridspec as gridspec
import math

g30545=plt.subplot()

image1=fits.open('../D4000_plots/joint_fit/pz_diagram/uds-18-G141_30545.new_zfit.pz.fits')
image2=fits.open('../D4000_plots/joint_fit/pz_diagram/IRC0218A_JOIN_30545.multifit.pz.fits')

image1.info()
image2.info()

g30545_zcoarse = image1[1].data

g30545_zphot = image1[2].data
#deal with log probs and normalize
g30545_zphot = np.exp(g30545_zphot)
g30545_zphot = 2*g30545_zphot/(np.sum(g30545_zphot))

g30545_zfine = image2[3].data
g30545_zjoin = image2[4].data
g30545_zjoin = g30545_zjoin/np.sum(g30545_zjoin)

g30545.plot(g30545_zcoarse, g30545_zphot, color='DimGray', linestyle='-.', linewidth=3.5, label='Phot z')
g30545.plot(g30545_zfine, g30545_zjoin, color='RoyalBlue', linewidth=3.5, label='Joint z')

g30545.set_xlim([1.60,1.70])
g30545.set_xticks(np.arange(1.57,1.70,0.025))
g30545.tick_params(labelsize=12)

g30545.set_ylim([0.02, 0.67])
g30545.text(1.6555,0.037,'3D-HST 30545',fontsize=16,color='k')
g30545.tick_params(axis='y', which='both', bottom='off', top='off')
g30545.axes.get_yaxis().set_ticks([])
g30545.set_xlabel(r'z', fontsize=16)
g30545.set_ylabel(r'Normalized P(z)', fontsize=16)

g30545.legend(loc=1,prop={'size':16})

plt.savefig('single_pz_plot', format='pdf',bbox_inches='tight')


plt.show()