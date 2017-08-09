#plots the lithium dip for NGC 6819 vs Teff, with the hyades fit overlaid, and also plots the distribution
#of gamma doradis stars below. Figure for observing proposal.

#the solid bars on the histogram are the gamma dor stars in fields of 3+, the shaded bar amounts represent 2-star field
#contributions

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
import math
import matplotlib.gridspec as gridspec

ngc6819dip=pd.read_csv('lidipvrmainseq_measured.csv')
ngc6819_teff=ngc6819dip['Tmsvr'].values
ngc6819_li=ngc6819dip['li'].values
ngc6819_li_unc=ngc6819dip['sigli'].values


ngc6819dip=pd.read_csv('lidipvrmainseq_uplim.csv')
ngc6819_teff_ul=ngc6819dip['Tmsvr'].values
ngc6819_li_ul=ngc6819dip['li'].values

hyadesfit=pd.read_csv('liprofvr.csv')
hyades_teff=hyadesfit['plus150'].values
hyades_fit=hyadesfit['Li'].values

#use all temps in order to create illusion of "stacked" histogram
gammadorall=pd.read_csv('gdor_allfield.csv')
gdor2_teff=gammadorall['Te'].values

gammador3=pd.read_csv('gdor_3field.csv')
gdor3_teff=gammador3['Te'].values

#call plot, relative sizes of subplots
gs=gridspec.GridSpec(2,1,height_ratios=[3.2,1])
fig=plt.figure()
plt.subplots_adjust(hspace=0.001)



#mess around with the lithium part
li6819=plt.subplot(gs[0])
li6819.errorbar(ngc6819_teff,ngc6819_li,yerr=ngc6819_li_unc,marker='o',color='RoyalBlue',linestyle='None',markeredgewidth=1,markersize=10,markeredgecolor='White',capsize=3,zorder=1)

li6819.scatter(ngc6819_teff_ul,ngc6819_li_ul,marker='v',color='White',linewidth=2,edgecolor='FireBrick',s=70,zorder=3)
li6819.scatter(ngc6819_teff_ul,ngc6819_li_ul,marker='v',color='White',linewidth=2,edgecolor='White',s=95,zorder=2)

li6819.plot(hyades_teff,hyades_fit,color='White',linewidth=5,zorder=4,antialiased=True)
li6819.plot(hyades_teff,hyades_fit,color='DimGrey',linewidth=3,zorder=5,antialiased=True)

li6819.set_ylabel(r'$A(Li)$', fontsize=14)

#adjust y ticks to not overlap
plt.yticks(np.arange(1.5,3.6,0.5))
plt.ylim(0,3.5)

#now the gamma dor part of the plot
gd_dist=plt.subplot(gs[1],sharex=li6819)
#backplot the entire distro first
n,bins,patches=gd_dist.hist(gdor2_teff,11,range=(6000,7100),rwidth=0.99,color='MediumAquaMarine',edgecolor='White',linewidth=2,hatch='///',zorder=1)
#n,bins,patches=gd_dist.hist(gdor2_teff,11,range=(6000,7100),rwidth=0.99,color='White',edgecolor='White',linewidth=2,hatch='///',alpha=0.3,zorder=2)
n,bins,patches=gd_dist.hist(gdor3_teff,11,range=(6000,7100),rwidth=0.99,color='SeaGreen',edgecolor='White',linewidth=2,zorder=3)

gd_dist.set_ylabel(r'$n$',fontsize=14)
gd_dist.set_xlabel(r'$Teff$',fontsize=14)
#again adjust yticks
plt.yticks(np.arange(2.0,10.5,2.0))
plt.ylim(0,10)

#gd_dist.set_xlim([6000,7100])

li6819.set_xticks(np.arange(6000,7400,200))
li6819.set_xlim([6000,7200])
li6819.set_ylim([1.2,3.8])
gd_dist.set_ylim([0,12])

#eliminate xlabels on 6819 plot
plt.setp(li6819.get_xticklabels(),visible=False)
plt.savefig("figure",format='pdf',bbox_inches='tight')

plt.show()
