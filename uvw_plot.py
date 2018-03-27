"""makes plots of uvw space velocities color coded by metallicity - what is the origin of the super metal rich stars?
Source for the toomre diagram boundaries: Fuhrmann, K. 2000, http://www.xray.mpe.mpg.de/∼fuhrmann but actualy from
http://adsabs.harvard.edu/abs/2004oee..symp..154N
and consistent with alpha results from: https://www.aanda.org/articles/aa/pdf/2003/01/aaej234.pdf
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

directory = '/home/donald/Desktop/PYTHON/misc_data/'
iso_subdir = 'smr_isochrones/'

input_mpdata = '/home/donald/Desktop/PYTHON/misc_data/uvw_metalpoor.csv'
input_mrdata = '/home/donald/Desktop/PYTHON/misc_data/uvw_metalrich.csv'

mpdata = np.genfromtxt(input_mpdata, delimiter=',', skip_header=1)
mrdata = np.genfromtxt(input_mrdata, delimiter=',', skip_header=1)

mr_energy = np.sqrt(mrdata[:, 5]**2+mrdata[:, 7]**2)
mr_v = mrdata[:, 6]

mr_energy_lp = mr_energy[:9]
mr_energy_lr = mr_energy[9:]

mr_v_lp = mr_v[:9]
mr_v_lr = mr_v[9:]

mp_energy = np.sqrt(mpdata[:, 5]**2+mpdata[:, 7]**2)
mp_v = mpdata[:, 6]

thickthincircle = mpatches.Circle([0, 0], 85, facecolor='none', edgecolor='k', linestyle='--', linewidth=3.0)

fig, splot = plt.subplots(1, figsize=(6, 5))

splot.scatter(mp_v, mp_energy, color='RoyalBlue', edgecolor='k', linewidth=1.5, s=120, label='[Fe/H]<+0.20')
splot.scatter(mr_v_lp, mr_energy_lp, color='None', marker='s', edgecolor='FireBrick', linewidth=1.5, s=100, label='[Fe/H]>+0.20, A(Li)<1.95')
splot.scatter(mr_v_lr, mr_energy_lr, color='FireBrick', marker='s', edgecolor='k', linewidth=1.5, s=100, label='[Fe/H]>+0.20, A(Li)>1.95')


splot.add_patch(thickthincircle)

plt.xlim([-85, 0])
plt.ylim([0, 85])

plt.xlabel('V (km/s)', fontsize=12)
plt.ylabel(r'$(U^{1/2}+W^{1/2})^{1/2}$ (km/s)', fontsize=12)
plt.text(-81, 78, 'Thick Disk', fontsize=12)
plt.text(-81, 5, 'Thin Disk', fontsize=12)

leg = plt.legend(loc=1)
leg.get_frame().set_edgecolor('k')
leg.get_frame().set_linewidth(1.5)
leg.get_frame().set_facecolor('White')
leg.get_frame().set_alpha(1.0)

plt.savefig(directory+'toomre_smr', format='pdf')

plt.show()

# now make a UV plot

fig2, splot2 = plt.subplots(1, figsize=(6, 5))

splot2.scatter(mp_v, mpdata[:, 5], color='RoyalBlue', edgecolor='k', linewidth=1.5, s=120, label='[Fe/H]<+0.20')
splot2.scatter(mr_v_lp, mrdata[:9, 5], color='None', marker='s', edgecolor='FireBrick', linewidth=1.5, s=100, label='[Fe/H]>+0.20, A(Li)<1.95')
splot2.scatter(mr_v_lr, mrdata[9:, 5], color='FireBrick', marker='s', edgecolor='k', linewidth=1.5, s=100, label='[Fe/H]>+0.20, A(Li)>1.95')

plt.xlabel('V (km/s)', fontsize=12)
plt.ylabel('U (km/s)', fontsize=12)

leg = plt.legend(loc=1)
leg.get_frame().set_edgecolor('k')
leg.get_frame().set_linewidth(1.5)
leg.get_frame().set_facecolor('White')
leg.get_frame().set_alpha(1.0)

plt.xlim([-79, 9])
plt.ylim([-59, 99])

plt.savefig(directory+'uvdiagram_smr', format='pdf')

plt.show()
