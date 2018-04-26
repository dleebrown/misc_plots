__author__ = 'donald'
#d4k vs mass Scatter plot with:
#color-coded SF and Q galaxies
#galaxy size -> mass
#squares for galaxies with no spec
#hollow points for galaxies below mass cutoff

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
import math

#import quiescent cluster galaxies with spectra info, set point size
cluster_spec_quiescent=pd.read_csv('cluster_uvjfastd4k_spec_q.csv')
c_s_d4kn_q=cluster_spec_quiescent['d4kn'].values
c_s_lu_q=abs(cluster_spec_quiescent['unc_d4kn_low'].values)
c_s_uu_q=abs(cluster_spec_quiescent['unc_d4kn_high'].values)
c_s_mass_q=cluster_spec_quiescent['lmass'].values
c_s_q_error=[c_s_lu_q,c_s_uu_q]

#import star forming cluster galaxies with spectra info, set point size
cluster_spec_starform=pd.read_csv('cluster_uvjfastd4k_spec_sf.csv')
c_s_d4kn_sf=cluster_spec_starform['d4kn'].values
c_s_lu_sf=abs(cluster_spec_starform['unc_d4kn_low'].values)
c_s_uu_sf=abs(cluster_spec_starform['unc_d4kn_high'].values)
c_s_mass_sf=cluster_spec_starform['lmass'].values
c_s_sf_error=[c_s_lu_sf,c_s_uu_sf]

#import star forming cluster galaxies with spectra info but no mass completeness, set point size
cluster_spec_starform_nm=pd.read_csv('cluster_uvjfastd4k_spec_sf_nomass.csv')
c_s_d4kn_sf_nm=cluster_spec_starform_nm['d4kn'].values
c_s_lu_sf_nm=abs(cluster_spec_starform_nm['unc_d4kn_low'].values)
c_s_uu_sf_nm=abs(cluster_spec_starform_nm['unc_d4kn_high'].values)
c_s_mass_sf_nm=cluster_spec_starform_nm['lmass'].values
c_s_sf_nm_error=[c_s_lu_sf_nm,c_s_uu_sf_nm]

#import quiescent cluster galaxies without spectra info, set point size
cluster_nospec_quiescent=pd.read_csv('cluster_uvjfastd4k_spec_q_nomass.csv')
c_ns_d4kn_q=cluster_nospec_quiescent['d4kn'].values
c_ns_lu_q=abs(cluster_nospec_quiescent['unc_d4kn_low'].values)
c_ns_uu_q=abs(cluster_nospec_quiescent['unc_d4kn_high'].values)
c_ns_mass_q=cluster_nospec_quiescent['lmass'].values
c_ns_q_error=[c_ns_lu_q,c_ns_uu_q]

#import star forming cluster galaxies without spectra info, set point size
#cluster_nospec_starform=pd.read_csv('cluster_uvjfastd4k_nospec_sf.csv')
#c_ns_d4kn_sf=cluster_nospec_starform['d4kn'].values
#c_ns_lu_sf=abs(cluster_nospec_starform['unc_d4kn_low'].values)
#c_ns_uu_sf=abs(cluster_nospec_starform['unc_d4kn_high'].values)
#c_ns_mass_sf=cluster_nospec_starform['lmass'].values
#c_ns_sf_error=[c_ns_lu_sf,c_ns_uu_sf]

#import star forming cluster galaxies without spectra info or mass completeness, set point size
#cluster_nospec_starform_nm=pd.read_csv('cluster_uvjfastd4k_nospec_sf_nomass.csv')
#c_ns_d4kn_sf_nm=cluster_nospec_starform_nm['d4kn'].values
#c_ns_lu_sf_nm=abs(cluster_nospec_starform_nm['unc_d4kn_low'].values)
#c_ns_uu_sf_nm=abs(cluster_nospec_starform_nm['unc_d4kn_high'].values)
#c_ns_mass_sf_nm=cluster_nospec_starform_nm['lmass'].values
#c_ns_sf_nm_error=[c_ns_lu_sf_nm,c_ns_uu_sf_nm]

#import models with zform=2
models_z2=pd.read_csv('z02_zform2.csv')

#import models with zform=3
models_z3=pd.read_csv('z02_zform3.csv')

#import models with zform=4
models_z4=pd.read_csv('z02_zform4.csv')

#import models with zform=2.5
models_z25=pd.read_csv('z02_zform25.csv')

#plot the galaxy points
fig, splot = plt.subplots()

#kill the gridlines
splot.grid(False)

#now a series of ssp sfh with zform = 4,3,2.5,and 2
splot.plot([8.6,11.6],[models_z4['ssp_dn4k'][0],models_z4['ssp_dn4k'][0]],color='goldenrod',linestyle='--',linewidth=3,alpha=0.7,label='$z_f$=4.0')
splot.plot([8.6,11.6],[models_z3['ssp_dn4k'][0],models_z3['ssp_dn4k'][0]],color='MediumOrchid',linestyle='--',linewidth=3,alpha=0.7,label='$z_f$=3.0')
splot.plot([8.6,11.6],[models_z25['ssp_dn4k'][0],models_z25['ssp_dn4k'][0]],color='RoyalBlue',linestyle='--',linewidth=3,alpha=0.7,label='$z_f$=2.5')
splot.plot([8.6,11.6],[models_z2['ssp_dn4k'][0],models_z2['ssp_dn4k'][0]],color='Gray',linestyle='--',linewidth=3,alpha=0.7,label='$z_f$=2.0')
splot.plot([8.6,11.6],[models_z3['csf_dn4k'][0],models_z3['csf_dn4k'][0]],color='Gray',linestyle='-',linewidth=3,alpha=0.5,label='Constant SF')

#plot the d4kn vs mass relations for the different galaxy subsets
splot.errorbar(c_s_mass_q, c_s_d4kn_q,yerr=c_s_q_error,c='FireBrick',marker='o',markersize=13, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='k',capsize=5)
splot.errorbar(c_s_mass_sf, c_s_d4kn_sf,yerr=c_s_sf_error,c='RoyalBlue',marker='o',markersize=13, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='k',capsize=5)
splot.errorbar(c_s_mass_sf_nm, c_s_d4kn_sf_nm,yerr=c_s_sf_nm_error,c='RoyalBlue',marker='o',markerfacecolor='White',markersize=14, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='RoyalBlue',capsize=5)
splot.errorbar(c_ns_mass_q, c_ns_d4kn_q,yerr=c_ns_q_error,c='FireBrick',marker='o',markerfacecolor='White',markersize=14, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='FireBrick',capsize=5)
#splot.errorbar(c_ns_mass_sf, c_ns_d4kn_sf,yerr=c_ns_sf_error,c='RoyalBlue',marker='s',markersize=13, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='k',capsize=5)
#splot.errorbar(c_ns_mass_sf_nm, c_ns_d4kn_sf_nm,yerr=c_ns_sf_nm_error,c='RoyalBlue',marker='s',markerfacecolor='White',markersize=13, alpha=1.0,linestyle='None',markeredgewidth=1.5,markeredgecolor='RoyalBlue',capsize=5)

#add arrows that correspond to the locations of the model lines if metallicity were changed to 0.05 or 0.004 (two arrows for each model)
splot.add_patch(patches.Arrow(8.80,models_z3['ssp_dn4k'][0],0,models_z3['ssp_dn4k'][1]-models_z3['ssp_dn4k'][0],color='MediumOrchid',alpha=1,edgecolor='none',width=0.15))
splot.add_patch(patches.Arrow(8.80,models_z3['ssp_dn4k'][0],0,models_z3['ssp_dn4k'][2]-models_z3['ssp_dn4k'][0],color='MediumOrchid',alpha=1,edgecolor='none',width=0.15))

splot.add_patch(patches.Arrow(8.70,models_z4['ssp_dn4k'][0],0,models_z4['ssp_dn4k'][1]-models_z4['ssp_dn4k'][0],color='goldenrod',alpha=1,edgecolor='none',width=0.15))
splot.add_patch(patches.Arrow(8.70,models_z4['ssp_dn4k'][0],0,models_z4['ssp_dn4k'][2]-models_z4['ssp_dn4k'][0],color='goldenrod',alpha=1,edgecolor='none',width=0.15))

splot.add_patch(patches.Arrow(8.90,models_z25['ssp_dn4k'][0],0,models_z25['ssp_dn4k'][1]-models_z25['ssp_dn4k'][0],color='RoyalBlue',alpha=1,edgecolor='none',width=0.15))
splot.add_patch(patches.Arrow(8.90,models_z25['ssp_dn4k'][0],0,models_z25['ssp_dn4k'][2]-models_z25['ssp_dn4k'][0],color='RoyalBlue',alpha=1,edgecolor='none',width=0.15))

#stick a legend on the plot in the upper left
splot.legend(loc=2, prop={'size':14},labelspacing=0)

#axes labels
splot.set_xlabel(r'$log(M/M_\odot)$', fontsize=18)
splot.set_ylabel(r'$D_n(4000)$', fontsize=18)

splot.text(11.25,0.15,'SSP',fontsize=18,color='k')

fig.tight_layout()

plt.ylim(0.0,2.6)
plt.xlim(8.65,11.6)
plt.show()