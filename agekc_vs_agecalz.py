__author__ = 'donald'
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
import math
import matplotlib

matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)

#import quiescent cluster galaxies with spectra info, set point size
cluster_spec_quiescent=pd.read_csv('cluster_uvjfastd4k_spec_q.csv')
c_s_d4kn_q=cluster_spec_quiescent['d4kn'].values
c_s_lu_q=abs(cluster_spec_quiescent['unc_d4kn_low'].values)
c_s_uu_q=abs(cluster_spec_quiescent['unc_d4kn_high'].values)
c_s_mass_q=cluster_spec_quiescent['lmass(calz)-lmass(kc)'].values
c_s_q_age=cluster_spec_quiescent['lage(calz)-lage(kc)'].values

#import star forming cluster galaxies with mass info, set point size
cluster_spec_starform=pd.read_csv('cluster_uvjfastd4k_spec_sf.csv')
c_s_d4kn_sf=cluster_spec_starform['d4kn'].values
c_s_lu_sf=abs(cluster_spec_starform['unc_d4kn_low'].values)
c_s_uu_sf=abs(cluster_spec_starform['unc_d4kn_high'].values)
c_s_mass_sf=cluster_spec_starform['lmass(calz)-lmass(kc)'].values
c_s_sf_age=cluster_spec_starform['lage(calz)-lage(kc)'].values

#import star forming cluster galaxies with spectra info but no mass completeness, set point size
cluster_spec_starform_nm=pd.read_csv('cluster_uvjfastd4k_spec_sf_nomass.csv')
c_s_d4kn_sf_nm=cluster_spec_starform_nm['d4kn'].values
c_s_lu_sf_nm=abs(cluster_spec_starform_nm['unc_d4kn_low'].values)
c_s_uu_sf_nm=abs(cluster_spec_starform_nm['unc_d4kn_high'].values)
c_s_mass_sf_nm=cluster_spec_starform_nm['lmass(calz)-lmass(kc)'].values
c_s_sf_nm_age=cluster_spec_starform_nm['lage(calz)-lage(kc)'].values

#import quiescent cluster galaxies without mass, set point size
cluster_nospec_quiescent=pd.read_csv('cluster_uvjfastd4k_spec_q_nomass.csv')
c_ns_d4kn_q=cluster_nospec_quiescent['d4kn'].values
c_ns_lu_q=abs(cluster_nospec_quiescent['unc_d4kn_low'].values)
c_ns_uu_q=abs(cluster_nospec_quiescent['unc_d4kn_high'].values)
c_ns_mass_q=cluster_nospec_quiescent['lmass(calz)-lmass(kc)'].values
c_ns_q_age=cluster_nospec_quiescent['lage(calz)-lage(kc)'].values

#import quiescent field galaxies with spectra info, set point size
field_spec_quiescent=pd.read_csv('field_uvjfastd4k_spec_q.csv')
f_s_d4kn_q=field_spec_quiescent['d4kn'].values
f_s_lu_q=abs(field_spec_quiescent['unc_d4kn_low'].values)
f_s_uu_q=abs(field_spec_quiescent['unc_d4kn_high'].values)
f_s_mass_q=field_spec_quiescent['lmass(calz)-lmass(kc)'].values
f_s_q_age=field_spec_quiescent['lage(calz)-lage(kc)'].values

#import star forming field galaxies with spectra info, set point size
field_spec_starform=pd.read_csv('field_uvjfastd4k_spec_sf.csv')
f_s_d4kn_sf=field_spec_starform['d4kn'].values
f_s_lu_sf=abs(field_spec_starform['unc_d4kn_low'].values)
f_s_uu_sf=abs(field_spec_starform['unc_d4kn_high'].values)
f_s_mass_sf=field_spec_starform['lmass(calz)-lmass(kc)'].values
f_s_sf_age=field_spec_starform['lage(calz)-lage(kc)'].values

#import star forming field galaxies with spectra info but no mass completeness, set point size
field_spec_starform_nm=pd.read_csv('field_uvjfastd4k_spec_sf_nomass.csv')
f_s_d4kn_sf_nm=field_spec_starform_nm['d4kn'].values
f_s_lu_sf_nm=abs(field_spec_starform_nm['unc_d4kn_low'].values)
f_s_uu_sf_nm=abs(field_spec_starform_nm['unc_d4kn_high'].values)
f_s_mass_sf_nm=field_spec_starform_nm['lmass(calz)-lmass(kc)'].values
f_s_sf_nm_age=field_spec_starform_nm['lage(calz)-lage(kc)'].values

#import quiescent field galaxies without spectra info, set point size
field_nospec_quiescent=pd.read_csv('field_uvjfastd4k_spec_q_nomass.csv')
f_ns_d4kn_q=field_nospec_quiescent['d4kn'].values
f_ns_lu_q=abs(field_nospec_quiescent['unc_d4kn_low'].values)
f_ns_uu_q=abs(field_nospec_quiescent['unc_d4kn_high'].values)
f_ns_mass_q=field_nospec_quiescent['lmass(calz)-lmass(kc)'].values
f_ns_q_age=field_nospec_quiescent['lage(calz)-lage(kc)'].values

#plot the galaxy points
fig, splot = plt.subplots()

#kill the gridlines
splot.grid(False)
size=200
size2=350
alpha=0.5

splot.scatter(c_s_mass_q, c_s_q_age, c='FireBrick', s=size, alpha=1.0,linewidths=2,zorder=6)
splot.scatter(c_s_mass_sf, c_s_sf_age, c='RoyalBlue', s=size, alpha=1.0,linewidths=2,zorder=6)
#splot.scatter(c_ns_mass_q, c_ns_q_age, c='FireBrick', s=size,facecolors='White',edgecolors='FireBrick',alpha=alpha,linewidths=2,zorder=4)
splot.scatter(c_s_mass_sf_nm, c_s_sf_nm_age, c='RoyalBlue', s=size,facecolors='White',edgecolors='RoyalBlue',alpha=alpha,linewidths=2,zorder=4)

marker='*'
splot.scatter(f_s_mass_q, f_s_q_age, c='FireBrick', marker=marker, s=size2, alpha=1.0,linewidths=2,zorder=5)
splot.scatter(f_s_mass_sf, f_s_sf_age, c='RoyalBlue',marker=marker, s=size2, alpha=1.0,linewidths=2,zorder=5)
#splot.scatter(f_ns_mass_q, f_ns_q_age, c='FireBrick',marker=marker, s=size2,facecolors='White',edgecolors='FireBrick',alpha=alpha,linewidths=2,zorder=3)
splot.scatter(f_s_mass_sf_nm, f_s_sf_nm_age, c='RoyalBlue', marker=marker, s=size2,facecolors='White',edgecolors='RoyalBlue',alpha=alpha,linewidths=2,zorder=3)

#text: axes labels, title, labels
splot.set_xlabel(r'$log(M_{\odot})_{Calzetti}-log(M_{\odot})_{K+C}$', fontsize=18)
splot.set_ylabel(r'$log(Age/yr)_{Calzetti}-log(Age/yr)_{K+C}$', fontsize=18)

fig.tight_layout()

splot.set_xlim(-0.2,0.5)
splot.set_ylim(-0.8,1.2)

plt.savefig('agekc_vs_agecalz', format='pdf',bbox_inches='tight')
plt.show()