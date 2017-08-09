__author__ = 'donald'
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
import math
import matplotlib
import pylab

#import quiescent cluster galaxies with spectra info, set point size
cluster_spec_quiescent=pd.read_csv('field_uvjfastd4k_spec_q.csv')
c_s_d4kn_q=cluster_spec_quiescent['d4kn'].values
c_s_lu_q=abs(cluster_spec_quiescent['unc_d4kn_low'].values)
c_s_uu_q=abs(cluster_spec_quiescent['unc_d4kn_high'].values)
c_s_mass_q=cluster_spec_quiescent['lmass'].values
c_s_q_error=[c_s_lu_q,c_s_uu_q]

#import star forming cluster galaxies with spectra info, set point size
cluster_spec_starform=pd.read_csv('field_uvjfastd4k_spec_sf.csv')
c_s_d4kn_sf=cluster_spec_starform['d4kn'].values
c_s_lu_sf=abs(cluster_spec_starform['unc_d4kn_low'].values)
c_s_uu_sf=abs(cluster_spec_starform['unc_d4kn_high'].values)
c_s_mass_sf=cluster_spec_starform['lmass'].values
c_s_sf_error=[c_s_lu_sf,c_s_uu_sf]

#calculate arrays corresponding to mean upper and lower uncertainty in d4k
ave_err_q=(c_s_lu_q-c_s_uu_q)/2
ave_err_sf=(c_s_lu_sf-c_s_uu_sf)/2

weights_q=1/(ave_err_q)**2
weights_sf=1/(ave_err_sf)**2

wm_q=np.sum(weights_q*c_s_d4kn_q)/np.sum(weights_q)
factor_q=np.sum(weights_q)/((np.sum(weights_q))**2-np.sum(weights_q**2))
ws_q=np.sqrt(factor_q*np.sum(weights_q*(c_s_d4kn_q-wm_q)**2))
print wm_q
print ws_q
wm_sf=np.sum(weights_sf*c_s_d4kn_sf)/np.sum(weights_sf)
factor_sf=np.sum(weights_sf)/((np.sum(weights_sf))**2-np.sum(weights_sf**2))
ws_sf=np.sqrt(factor_sf*np.sum(weights_sf*(c_s_d4kn_sf-wm_sf)**2))
print wm_sf
print ws_sf