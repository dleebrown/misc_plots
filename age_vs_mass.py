#d4k vs age Scatter plot with:
#color-coded SF and Q galaxies
#point size -> mass
#squares for galaxies with no spec
#hollow points for galaxies below mass cutoff

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
import math
import matplotlib
matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)

#these variable assignments are all fubared because i just hacked the d4k vs age plot
#import quiescent cluster galaxies with spectra info, set point size
cluster_spec_quiescent=pd.read_csv('cluster_uvjfastd4k_spec_q.csv')
c_s_d4kn_q=cluster_spec_quiescent['lage'].values
c_s_lu_q=abs(cluster_spec_quiescent['unc_d4kn_low'].values)
c_s_uu_q=abs(cluster_spec_quiescent['unc_d4kn_high'].values)
c_s_mass_q=cluster_spec_quiescent['lmass'].values
c_s_q_error=[c_s_lu_q,c_s_uu_q]
c_s_age_q=cluster_spec_quiescent['lage'].values
#for entry in range(len(c_s_mass_q)):
#    c_s_mass_q[entry]=math.exp(c_s_mass_q[entry])
#size_c_s_q= (400*c_s_mass_q / np.max(c_s_mass_q))

#import star forming cluster galaxies with spectra info, set point size
cluster_spec_starform=pd.read_csv('cluster_uvjfastd4k_spec_sf.csv')
c_s_d4kn_sf=cluster_spec_starform['d4kn'].values
c_s_lu_sf=abs(cluster_spec_starform['unc_d4kn_low'].values)
c_s_uu_sf=abs(cluster_spec_starform['unc_d4kn_high'].values)
c_s_mass_sf=cluster_spec_starform['lmass'].values
c_s_sf_error=[c_s_lu_sf,c_s_uu_sf]
c_s_age_sf=cluster_spec_starform['lage'].values
#for entry in range(len(c_s_mass_sf)):
#    c_s_mass_sf[entry]=math.exp(c_s_mass_sf[entry])
#size_c_s_sf= (400*c_s_mass_sf / np.max(c_s_mass_q))

#import star forming cluster galaxies with spectra info but no mass completeness, set point size
cluster_spec_starform_nm=pd.read_csv('cluster_uvjfastd4k_spec_sf_nomass.csv')
c_s_d4kn_sf_nm=cluster_spec_starform_nm['d4kn'].values
c_s_lu_sf_nm=abs(cluster_spec_starform_nm['unc_d4kn_low'].values)
c_s_uu_sf_nm=abs(cluster_spec_starform_nm['unc_d4kn_high'].values)
c_s_mass_sf_nm=cluster_spec_starform_nm['lmass'].values
c_s_sf_nm_error=[c_s_lu_sf_nm,c_s_uu_sf_nm]
c_s_age_sf_nm=cluster_spec_starform_nm['lage'].values
#for entry in range(len(c_s_mass_sf_nm)):
#    c_s_mass_sf_nm[entry]=math.exp(c_s_mass_sf_nm[entry])
#size_c_s_sf_nm= (400*c_s_mass_sf_nm / np.max(c_s_mass_q))

#import quiescent cluster galaxies without spectra info, set point size
cluster_nospec_quiescent=pd.read_csv('cluster_uvjfastd4k_spec_q_nomass.csv')
c_ns_d4kn_q=cluster_nospec_quiescent['d4kn'].values
c_ns_lu_q=abs(cluster_nospec_quiescent['unc_d4kn_low'].values)
c_ns_uu_q=abs(cluster_nospec_quiescent['unc_d4kn_high'].values)
c_ns_mass_q=cluster_nospec_quiescent['lmass'].values
c_ns_q_error=[c_ns_lu_q,c_ns_uu_q]
c_ns_age_q=cluster_nospec_quiescent['lage'].values
#for entry in range(len(c_ns_mass_q)):
#    c_ns_mass_q[entry]=math.exp(c_ns_mass_q[entry])
#size_c_ns_q= (400*c_ns_mass_q / np.max(c_s_mass_q))


#import star forming cluster galaxies without spectra info, set point size
#cluster_nospec_starform=pd.read_csv('cluster_uvjfastd4k_nospec_sf.csv')
#c_ns_d4kn_sf=cluster_nospec_starform['d4kn'].values
#c_ns_lu_sf=abs(cluster_nospec_starform['unc_d4kn_low'].values)
#c_ns_uu_sf=abs(cluster_nospec_starform['unc_d4kn_high'].values)
#c_ns_mass_sf=cluster_nospec_starform['lmass'].values
#c_ns_sf_error=[c_ns_lu_sf,c_ns_uu_sf]
#c_ns_age_sf=cluster_nospec_starform['lage'].values
#for entry in range(len(c_ns_mass_sf)):
#    c_ns_mass_sf[entry]=math.exp(c_ns_mass_sf[entry])
#size_c_ns_sf= (400*c_ns_mass_sf / np.max(c_s_mass_q))

#import star forming cluster galaxies without spectra info or mass completeness, set point size
#cluster_nospec_starform_nm=pd.read_csv('cluster_uvjfastd4k_nospec_sf_nomass.csv')
#c_ns_d4kn_sf_nm=cluster_nospec_starform_nm['d4kn'].values
#c_ns_lu_sf_nm=abs(cluster_nospec_starform_nm['unc_d4kn_low'].values)
#c_ns_uu_sf_nm=abs(cluster_nospec_starform_nm['unc_d4kn_high'].values)
#c_ns_mass_sf_nm=cluster_nospec_starform_nm['lmass'].values
#c_ns_sf_nm_error=[c_ns_lu_sf_nm,c_ns_uu_sf_nm]
#c_ns_age_sf_nm=cluster_nospec_starform_nm['lage'].values
#for entry in range(len(c_ns_mass_sf_nm)):
#    c_ns_mass_sf_nm[entry]=math.exp(c_ns_mass_sf_nm[entry])
#size_c_ns_sf_nm= (400*c_ns_mass_sf_nm / np.max(c_s_mass_q))

#plot the galaxy points
fig, splot = plt.subplots()

#kill the gridlines
splot.grid(False)

#plot the d4kn vs mass relations for the different galaxy subsets
#may need to loop over and plot each individual point because errorbar doesn't seem to support changing the point size...
#the point size scaling for errorbar is very different from scatter...new plan is to plot the errorbars under a normal scatterplot - eliminates need for looping
#splot.errorbar(c_s_age_q, c_s_d4kn_q,yerr=c_s_q_error,c='FireBrick',marker='o',markersize=1, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='k',capsize=5)
#splot.errorbar(c_s_age_sf, c_s_d4kn_sf,yerr=c_s_sf_error,c='RoyalBlue',marker='o',markersize=1, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='k',capsize=5)
#splot.errorbar(c_s_age_sf_nm, c_s_d4kn_sf_nm,yerr=c_s_sf_nm_error,c='RoyalBlue',marker='o',markerfacecolor='White',markersize=1, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='RoyalBlue',capsize=5)
#splot.errorbar(c_ns_age_q, c_ns_d4kn_q,yerr=c_ns_q_error,c='FireBrick',marker='o',markerfacecolor='White',markersize=1, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='FireBrick',capsize=5)
#splot.errorbar(c_ns_age_sf, c_ns_d4kn_sf,yerr=c_ns_sf_error,c='RoyalBlue',marker='s',markersize=1, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='k',capsize=5)
#splot.errorbar(c_ns_age_sf_nm, c_ns_d4kn_sf_nm,yerr=c_ns_sf_nm_error,c='RoyalBlue',marker='s',markerfacecolor='White',markersize=1, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='RoyalBlue',capsize=5)

#now plot the points
splot.scatter(cluster_spec_quiescent['lmass'].values, c_s_age_q, c='FireBrick', s=150, alpha=1.0,linewidths=2,zorder=6)
splot.scatter(cluster_spec_starform['lmass'].values, c_s_age_sf, c='RoyalBlue', s=150, alpha=1.0,linewidths=2,zorder=6)
splot.scatter(cluster_spec_starform_nm['lmass'].values, c_s_age_sf_nm, c='RoyalBlue', s=150,facecolors='White', edgecolors='RoyalBlue',alpha=1.0,linewidths=2,zorder=4)
#splot.scatter(cluster_nospec_quiescent['lmass'].values, c_ns_age_q, c='FireBrick',facecolors='White', edgecolors='FireBrick', s=150,marker='o',alpha=1.0,linewidths=2,zorder=5)
#splot.scatter(c_ns_age_sf, c_ns_d4kn_sf, c='RoyalBlue', s=size_c_ns_sf,marker='s',linewidths=2,alpha=1.0,zorder=5)
#splot.scatter(c_ns_age_sf_nm, c_ns_d4kn_sf_nm, c='RoyalBlue', s=size_c_ns_sf_nm,marker='s',facecolors='White',edgecolors='RoyalBlue',linewidths=2,alpha=1.0,zorder=5)
#axes labels
splot.set_xlabel(r'$log(M/M_\odot)$', fontsize=18)
splot.set_ylabel(r'$log(Age)$', fontsize=18)

fig.tight_layout()

plt.ylim(8.0,9.8)
plt.xlim(8.65,11.6)
plt.savefig('cluster_agemass', format='pdf',bbox_inches='tight')
plt.show()
