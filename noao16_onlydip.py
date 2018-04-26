"""NOAO 2016 plot except the bottom plot of gamma dor stars has been removed and only the dip is show for Hyades/6819"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
import math
import matplotlib.gridspec as gridspec

directory = '/home/donald/Desktop/PYTHON/misc_data/'

ngc6819dip=pd.read_csv(directory+'lidipvrmainseq_measured.csv')
ngc6819_teff=ngc6819dip['Tmsvr'].values
ngc6819_li=ngc6819dip['li'].values
ngc6819_li_unc=ngc6819dip['sigli'].values

ngc6819dip=pd.read_csv(directory+'lidipvrmainseq_uplim.csv')
ngc6819_teff_ul=ngc6819dip['Tmsvr'].values
ngc6819_li_ul=ngc6819dip['li'].values

hyadesfit=pd.read_csv(directory+'liprofvr.csv')
hyades_teff=hyadesfit['plus150'].values
hyades_fit=hyadesfit['Li'].values

plt.figure(figsize=(8, 4))

plt.errorbar(ngc6819_teff,ngc6819_li,yerr=ngc6819_li_unc,marker='o',color='RoyalBlue',linestyle='None',markeredgewidth=1,markersize=10,markeredgecolor='White',capsize=3,zorder=1, label='NGC 6819')

plt.scatter(ngc6819_teff_ul,ngc6819_li_ul,marker='v',color='White',linewidth=2,edgecolor='FireBrick',s=70,zorder=3)
plt.scatter(ngc6819_teff_ul,ngc6819_li_ul,marker='v',color='White',linewidth=2,edgecolor='White',s=95,zorder=2)

plt.plot(hyades_teff,hyades_fit,color='White',linewidth=5,zorder=4,antialiased=True)
plt.plot(hyades_teff,hyades_fit,color='DimGrey',linewidth=3,zorder=5,antialiased=True, label='Hyades')

plt.xlim([6050,7150])
plt.ylim([1.2,3.8])

plt.legend(loc=3, fontsize=10)

plt.xlabel('Temperature (K)', fontsize=12)
plt.ylabel('A(Li) (dex)', fontsize=12)

plt.savefig(directory+'noao16_dip', format='pdf', bbox_inches='tight')

plt.show()