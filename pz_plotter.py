__author__ = 'donald'

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.gridspec as gridspec
import math

gs=gridspec.GridSpec(3,1,height_ratios=[1,1,1])
fig=plt.figure(figsize=(3,5))
plt.subplots_adjust(hspace=0.001)


#30545################################################################################################################

g30545=plt.subplot(gs[2])

image1=fits.open('uds-18-G141_30545.new_zfit.pz.fits')
image2=fits.open('IRC0218A_JOIN_30545.multifit.pz.fits')

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

g30545.plot(g30545_zcoarse, g30545_zphot, color='RoyalBlue', linestyle='-.', linewidth=3, label='Phot. z')
g30545.plot(g30545_zfine, g30545_zjoin, color='FireBrick', linewidth=1.5, label='Joint z')

g30545.set_xlim([1.55,1.80])
g30545.set_xticks(np.arange(1.57,1.80,0.05))
g30545.tick_params(labelsize=10)

g30545.set_ylim([0.02, 0.67])
g30545.text(1.705,0.57,'3D-HST 30545',fontsize=8,color='k')
g30545.tick_params(axis='y', which='both', bottom='off', top='off')
g30545.axes.get_yaxis().set_ticks([])
g30545.set_xlabel(r'$z$', fontsize=11)
g30545.legend(bbox_to_anchor=(0.623, 0.80), loc=2, borderaxespad=0.,prop={'size':8},labelspacing=0.3)



#30737################################################################################################################

g30737=plt.subplot(gs[0], sharex=g30545)

image1=fits.open('uds-18-G141_30737.new_zfit.pz.fits')
image2=fits.open('IRC0218A_JOIN_30737.multifit.pz.fits')

image1.info()
image2.info()

g30737_zcoarse = image1[1].data

g30737_zphot = image1[2].data
#deal with log probs and normalize
g30737_zphot = np.exp(g30737_zphot)
g30737_zphot = g30737_zphot/(np.sum(g30737_zphot))

g30737_zfine = image2[3].data
g30737_zjoin = image2[4].data
g30737_zjoin = g30737_zjoin/np.sum(g30737_zjoin)

g30737.plot(g30737_zcoarse, g30737_zphot, color='RoyalBlue', linestyle='-.', linewidth=3)
g30737.plot(g30737_zfine, g30737_zjoin, color='FireBrick', linewidth=1.5)

#g30737.set_ylim([0,1])
#g30737.set_xlim([1.55,1.75])
g30737.set_ylim([0.005, 0.14])
g30737.text(1.705,0.119,'3D-HST 30737',fontsize=8,color='k')

g30737.tick_params(axis='y', which='both', bottom='off', top='off')
g30737.axes.get_yaxis().set_ticks([])


#33092################################################################################################################

g33092=plt.subplot(gs[1], sharex=g30545)

image1=fits.open('uds-18-G141_33092.new_zfit.pz.fits')
image2=fits.open('IRC0218A_JOIN_33092.multifit.pz.fits')

image1.info()
image2.info()

g33092_zcoarse = image1[1].data

g33092_zphot = image1[2].data
#deal with log probs and normalize
g33092_zphot = np.exp(g33092_zphot)
g33092_zphot = g33092_zphot/(np.sum(g33092_zphot)*3)

g33092_zfine = image2[3].data
g33092_zjoin = image2[4].data
g33092_zjoin = g33092_zjoin/np.sum(g33092_zjoin)

g33092.grid(False)
g33092.plot(g33092_zcoarse, g33092_zphot, color='RoyalBlue', linestyle='-.', linewidth=3)
g33092.plot(g33092_zfine, g33092_zjoin, color='FireBrick', linewidth=1.5)


#g33092.set_xlim([1.55,1.75])
g33092.set_ylim([0.005, 0.10])
g33092.text(1.705,0.085,'3D-HST 33092',fontsize=8,color='k')
g33092.tick_params(axis='y', which='both', bottom='off', top='off')
g33092.axes.get_yaxis().set_ticks([])
g33092.set_ylabel(r'$p(z)$', fontsize=11)


#plot#################################################################################################################


plt.setp(g30737.get_yticklabels(), visible=False)
plt.setp(g33092.get_yticklabels(), visible=False)
plt.setp(g30737.get_xticklabels(), visible=False)
plt.setp(g33092.get_xticklabels(), visible=False)
plt.setp(g30545.get_yticklabels(), visible=False)
plt.xlim([1.55,1.80])
plt.savefig("pz_stack",format='pdf', bbox_inches='tight')

plt.show()




