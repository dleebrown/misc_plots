
#UVJ Scatter plot with:
#color-coded SF and Q galaxies
#SF cutoffs
#galaxy size -> mass
#squares for galaxies with no spec
#hollow points for galaxies below mass cutoff
#shadow plot of all galaxy uvj z>1

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import math
import matplotlib.patches as patches
import pylab
from scipy.interpolate import interp1d

matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)

#import quiescent cluster galaxies with spectra info, set point size
cluster_spec_quiescent=pd.read_csv('cluster_uvjfastd4k_spec_q.csv')
c_s_mass_q=cluster_spec_quiescent['lmass'].values
c_s_uv_q=cluster_spec_quiescent['U-V'].values
c_s_vj_q=cluster_spec_quiescent['V-J'].values
for entry in range(len(c_s_mass_q)):
    c_s_mass_q[entry]=math.exp(c_s_mass_q[entry])
size_c_s_q= (400*c_s_mass_q / np.max(c_s_mass_q))

#import star forming cluster galaxies with spectra info, set point size
cluster_spec_starform=pd.read_csv('cluster_uvjfastd4k_spec_sf.csv')
c_s_mass_sf=cluster_spec_starform['lmass'].values
c_s_uv_sf=cluster_spec_starform['U-V'].values
c_s_vj_sf=cluster_spec_starform['V-J'].values
for entry in range(len(c_s_mass_sf)):
    c_s_mass_sf[entry]=math.exp(c_s_mass_sf[entry])
size_c_s_sf= (400*c_s_mass_sf / np.max(c_s_mass_q))

#import star forming cluster galaxies with spectra info but no mass completeness, set point size
cluster_spec_starform_nm=pd.read_csv('cluster_uvjfastd4k_spec_sf_nomass.csv')
c_s_mass_sf_nm=cluster_spec_starform_nm['lmass'].values
c_s_uv_sf_nm=cluster_spec_starform_nm['U-V'].values
c_s_vj_sf_nm=cluster_spec_starform_nm['V-J'].values
for entry in range(len(c_s_mass_sf_nm)):
    c_s_mass_sf_nm[entry]=math.exp(c_s_mass_sf_nm[entry])
size_c_s_sf_nm= (400*c_s_mass_sf_nm / np.max(c_s_mass_q))

#import quiescent cluster galaxies without spectra info, set point size
cluster_nospec_quiescent=pd.read_csv('cluster_uvjfastd4k_spec_q_nomass.csv')
c_ns_mass_q=cluster_nospec_quiescent['lmass'].values
c_ns_uv_q=cluster_nospec_quiescent['U-V'].values
c_ns_vj_q=cluster_nospec_quiescent['V-J'].values
for entry in range(len(c_ns_mass_q)):
    c_ns_mass_q[entry]=math.exp(c_ns_mass_q[entry])
size_c_ns_q= (400*c_ns_mass_q / np.max(c_s_mass_q))

#import the uvj evolution for ssp
UVJ_ssp=pd.read_csv('ssp.csv')
UV_ssp=UVJ_ssp['U-V'].values
VJ_ssp=UVJ_ssp['V-J'].values
lage_ssp=UVJ_ssp['lage'].values
for entry in range(len(lage_ssp)):
    lage_ssp[entry]=10**lage_ssp[entry]
age_ssp=lage_ssp


#import the uvj evolution for exptau300
UVJ_exp=pd.read_csv('tau300.csv')
UV_exp=UVJ_exp['U-V'].values
VJ_exp=UVJ_exp['V-J'].values
lage_exp=UVJ_exp['lage'].values
for entry in range(len(lage_exp)):
    lage_exp[entry]=10**lage_exp[entry]
age_exp=lage_exp

#import star forming cluster galaxies without spectra info, set point size - no longer exists
#cluster_nospec_starform=pd.read_csv('cluster_uvjfastd4k_nospec_sf.csv')
#c_ns_mass_sf=cluster_nospec_starform['lmass'].values
#c_ns_uv_sf=cluster_nospec_starform['U-V'].values
#c_ns_vj_sf=cluster_nospec_starform['V-J'].values
#for entry in range(len(c_ns_mass_sf)):
#    c_ns_mass_sf[entry]=math.exp(c_ns_mass_sf[entry])
#size_c_ns_sf= (400*c_ns_mass_sf / np.max(c_s_mass_q))

#import star forming cluster galaxies without spectra info or mass completeness, set point size - no longer exists
#cluster_nospec_starform_nm=pd.read_csv('cluster_uvjfastd4k_nospec_sf_nomass.csv')
#c_ns_mass_sf_nm=cluster_nospec_starform_nm['lmass'].values
#c_ns_uv_sf_nm=cluster_nospec_starform_nm['U-V'].values
#c_ns_vj_sf_nm=cluster_nospec_starform_nm['V-J'].values
#for entry in range(len(c_ns_mass_sf_nm)):
#    c_ns_mass_sf_nm[entry]=math.exp(c_ns_mass_sf_nm[entry])
#size_c_ns_sf_nm= (400*c_ns_mass_sf_nm / np.max(c_s_mass_q))

#import all galaxies with sp redshifts z>1
background=pd.read_csv('all_cat_uvjfast_spec_z1.csv')
backuv=background['U-V'].values
backvj=background['V-J'].values

#plot the galaxy points
fig, splot = plt.subplots()

#kill the gridlines
splot.grid(False)

#plot the UVJ SF/Q cut lines
splot.plot([0.0,0.75],[1.3,1.3],color='k',linestyle='-',linewidth=2,zorder=2)
splot.plot([0.75,1.5],[1.3,1.9],color='k',linestyle='-',linewidth=2,zorder=2)
splot.plot([1.5,1.5],[1.9,2.5],color='k',linestyle='-',linewidth=2,zorder=2)

#plot the Av=1 extinction effects:
opt = {'head_width': 0.05, 'head_length': 0.05, 'width': 0.0075,
        'length_includes_head': True}
splot.add_patch(pylab.arrow(1.6,0.7,0.668757254244,0.487433775809,color='DarkGreen',**opt))
splot.hexbin(backvj,backuv,cmap='Greys',gridsize=40,vmin=0,vmax=8,zorder=1)
splot.text(1.45,0.6,'$A_{V}=1$',fontsize=16,color='DarkGreen')

#interpolates uvj evolution into uniform range in age for exp
smoothage=np.arange(10e6,2210e6,10e6)
interp_uv_exp=interp1d(age_exp,UV_exp,kind='cubic')
interp_vj_exp=interp1d(age_exp,VJ_exp,kind='cubic')
smooth_uv_exp=interp_uv_exp(smoothage)
smooth_vj_exp=interp_vj_exp(smoothage)
#does the same for ssp
interp_uv_ssp=interp1d(age_ssp,UV_ssp,kind='cubic')
interp_vj_ssp=interp1d(age_ssp,VJ_ssp,kind='cubic')
smooth_uv_ssp=interp_uv_ssp(smoothage)
smooth_vj_ssp=interp_vj_ssp(smoothage)


#plot the exp and ssp uvj evolution
splot.plot(smooth_vj_ssp,smooth_uv_ssp,linewidth=4,zorder=2,linestyle='--',color='DarkViolet')
splot.plot(smooth_vj_exp,smooth_uv_exp,linewidth=3,zorder=2,color='DarkGreen')


size=200
marker='D'
ecolor='White'
fcolor='DarkGreen'
#PLOT BC03 MODELS WITH TAU=300, Z=0.02 AND VARIOUS FORMATION REDSHIFTS
splot.scatter(smooth_vj_exp[np.where(smoothage==720e6)], smooth_uv_exp[np.where(smoothage==720e6)], marker=marker, c=fcolor, edgecolors=ecolor,s=size, alpha=1.0,linewidths=2,zorder=3)
#splot.scatter(smooth_vj_exp[np.where(smoothage==1150e6)], smooth_uv_exp[np.where(smoothage==1150e6)], marker=marker, c=fcolor, edgecolors=ecolor,s=size, alpha=1.0,linewidths=2,zorder=3)
agee=1390e6
splot.scatter(smooth_vj_exp[np.where(smoothage==agee)], smooth_uv_exp[np.where(smoothage==agee)], marker=marker, c=fcolor, edgecolors=ecolor,s=size, alpha=1.0,linewidths=2,zorder=3)
#splot.scatter(smooth_vj_exp[np.where(smoothage==1870e6)], smooth_uv_exp[np.where(smoothage==1870e6)], marker=marker, c=fcolor, edgecolors=ecolor,s=size, alpha=1.0,linewidths=2,zorder=3)
splot.scatter(smooth_vj_exp[np.where(smoothage==2200e6)], smooth_uv_exp[np.where(smoothage==2200e6)], marker=marker, c=fcolor, edgecolors=ecolor,s=size, alpha=1.0,linewidths=2,zorder=3)
#splot.scatter(smooth_vj_exp[np.where(smoothage==2460e6)], smooth_uv_exp[np.where(smoothage==2460e6)], marker=marker, c='White', edgecolors='DimGray',s=size, alpha=1.0,linewidths=2,zorder=3)

'''
#add some labels
splot.text(smooth_vj_exp[np.where(smoothage==720e6)]-0.019, smooth_uv_exp[np.where(smoothage==720e6)]-0.050,'1',fontsize=12,color='DimGray')
splot.text(smooth_vj_exp[np.where(smoothage==1150e6)]-0.019, smooth_uv_exp[np.where(smoothage==1150e6)]-0.050,'2',fontsize=12,color='DimGray')
splot.text(smooth_vj_exp[np.where(smoothage==1390e6)]-0.019, smooth_uv_exp[np.where(smoothage==1390e6)]-0.050,'3',fontsize=12,color='DimGray')
splot.text(smooth_vj_exp[np.where(smoothage==1870e6)]-0.019, smooth_uv_exp[np.where(smoothage==1870e6)]-0.050,'4',fontsize=12,color='DimGray')
splot.text(smooth_vj_exp[np.where(smoothage==2200e6)]-0.019, smooth_uv_exp[np.where(smoothage==2200e6)]-0.050,'5',fontsize=12,color='DimGray')
'''
ecolor='White'
marker='8'
fcolor='DarkViolet'
#PLOT BC03 MODELS WITH ssp, Z=0.02 AND VARIOUS FORMATION REDSHIFTS
splot.scatter(smooth_vj_ssp[np.where(smoothage==720e6)], smooth_uv_ssp[np.where(smoothage==720e6)], marker=marker, c=fcolor, edgecolors=ecolor,s=size, alpha=1.0,linewidths=2,zorder=3)
#splot.scatter(smooth_vj_ssp[np.where(smoothage==1150e6)], smooth_uv_ssp[np.where(smoothage==1150e6)], marker=marker, c=fcolor, edgecolors=ecolor,s=size, alpha=1.0,linewidths=2,zorder=3)
splot.scatter(smooth_vj_ssp[np.where(smoothage==1390e6)], smooth_uv_ssp[np.where(smoothage==1390e6)], marker=marker, c=fcolor, edgecolors=ecolor,s=size, alpha=1.0,linewidths=2,zorder=3)
#splot.scatter(smooth_vj_ssp[np.where(smoothage==1870e6)], smooth_uv_ssp[np.where(smoothage==1870e6)], marker=marker, c=fcolor, edgecolors=ecolor,s=size, alpha=1.0,linewidths=2,zorder=3)
splot.scatter(smooth_vj_ssp[np.where(smoothage==2200e6)], smooth_uv_ssp[np.where(smoothage==2200e6)], marker=marker, c=fcolor, edgecolors=ecolor,s=size, alpha=1.0,linewidths=2,zorder=3)
#splot.scatter(smooth_vj_ssp[np.where(smoothage==2460e6)], smooth_uv_ssp[np.where(smoothage==2460e6)], marker=marker, c='White', edgecolors='DimGray',s=size, alpha=1.0,linewidths=2,zorder=3)

#plot each of the cluster subsets
splot.scatter(c_s_vj_q, c_s_uv_q, c='FireBrick', s=size_c_s_q, alpha=1.0,linewidths=2,zorder=6)
splot.scatter(c_s_vj_sf, c_s_uv_sf, c='RoyalBlue', s=size_c_s_sf, alpha=1.0,linewidths=2,zorder=6)
#splot.scatter(c_ns_vj_q, c_ns_uv_q, c='FireBrick', s=size_c_ns_q,facecolors='White',edgecolors='FireBrick',alpha=1.0,linewidths=2,zorder=4)
#splot.scatter(c_ns_vj_sf, c_ns_uv_sf, c='RoyalBlue', s=size_c_ns_sf,marker='s',alpha=1.0,linewidths=2,zorder=5)
splot.scatter(c_s_vj_sf_nm, c_s_uv_sf_nm, s=size_c_s_sf_nm, facecolors='White', edgecolors='RoyalBlue',linewidths=2,alpha=1.0,zorder=4)
#splot.scatter(c_ns_vj_sf_nm, c_ns_uv_sf_nm, c='RoyalBlue', s=size_c_ns_sf,marker='s',facecolors='White',edgecolors='RoyalBlue',linewidths=2,alpha=1.0,zorder=3)
#text: axes labels, title, labels
splot.set_xlabel(r'$V-J$', fontsize=18)
splot.set_ylabel(r'$U-V$', fontsize=18)
splot.text(0.22,2.2,'Quiescent',fontsize=18,color='k')
splot.text(1.45,0.22,'Star Forming',fontsize=18,color='k')

#fig.tight_layout()
splot.set_aspect('equal')

#stick a legend on the plot in the upper left
#splot.legend(loc=2, prop={'size':18},labelspacing=-0.2)

splot.text(1.82,2.32,'IRC 0218', family='serif',weight='ultralight',fontsize=16, color='k')


#set plot limits
splot.set_xticks(np.arange(0.0,3.0,0.5))
splot.set_yticks(np.arange(0.5,3.0,0.5))

splot.set_xlim(0.0,2.5)
splot.set_ylim(0.0,2.5)

plt.savefig('cluster_uvj_models_whitaker', format='pdf',bbox_inches='tight')
plt.show()
