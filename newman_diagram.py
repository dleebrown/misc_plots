__author__ = 'donald'

"""calculates the quenched fraction of galaxies as a function of mass for the cluster and field,
assuming binomial errors on the counts and mass errors = width of mass bin. right now:
field sample is binned in increments of 0.2 in mass, cluster sample has 2 mass bins.
the uvj quiescent cuts are the same in both plots. the field sample criteria are in my notes.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
import math
import matplotlib
matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)

field_sample=pd.read_csv('allcat.uvj.z1.GRIZONLY.csv')
field_uv=field_sample['U-V']
field_vj=field_sample['V-J']
field_mass=field_sample['lmass']
vjcut=1.6
uvcut=1.3
field_quiescent=field_mass[(field_uv>uvcut) & (field_vj<vjcut) & (field_uv>(0.88*field_vj+0.49))]
field_sf=field_mass[(field_uv<uvcut) | (field_vj>vjcut) | ((field_uv>uvcut) & (field_vj<vjcut) & (field_uv<(0.88*field_vj+0.49)))]

#double check to make sure sifting was okay - plot uvj diagram for photometric sample

#double check to make sure the sifting did what it was supposed to: plot uvj
field_quiescent_uv=field_uv[(field_uv>1.3) & (field_vj<1.6) & (field_uv>0.88*field_vj+0.49)]
field_sf_uv=field_uv[(field_uv<1.3) | (field_vj>1.6) | ((field_uv>1.3) & (field_vj<1.6) & (field_uv<0.88*field_vj+0.49))]

field_quiescent_vj=field_vj[(field_uv>1.3) & (field_vj<1.6) & (field_uv>0.88*field_vj+0.49)]
field_sf_vj=field_vj[(field_uv<1.3) | (field_vj>1.6) | ((field_uv>1.3) & (field_vj<1.6) & (field_uv<0.88*field_vj+0.49))]

fig, splot = plt.subplots()
splot.grid(False)
splot.set_xlabel(r'$(V-J)_{AB}$', fontsize=18)
splot.set_ylabel(r'$(U-V)_{AB}$', fontsize=18)
splot.text(0.22,2.2,'Quiescent',fontsize=18,color='k')
splot.text(1.45,0.22,'Star Forming',fontsize=18,color='k')

#plot the UVJ SF/Q cut lines
splot.plot([0.0,0.92],[1.3,1.3],color='k',linestyle='-',linewidth=2,zorder=7)
splot.plot([0.92,1.6],[1.3,1.898],color='k',linestyle='-',linewidth=2,zorder=7)
splot.plot([1.6,1.6],[1.898,2.5],color='k',linestyle='-',linewidth=2,zorder=7)

splot.scatter(field_quiescent_vj, field_quiescent_uv, c='FireBrick', s=100, alpha=1.0,linewidths=2,zorder=6)
splot.scatter(field_sf_vj, field_sf_uv, c='RoyalBlue', s=100, alpha=1.0,linewidths=2,zorder=5)

fig.tight_layout()
splot.set_aspect('equal')

#set plot limits
splot.set_xticks(np.arange(0.0,3.0,0.5))
splot.set_yticks(np.arange(0.5,3.0,0.5))

splot.set_xlim(0.0,2.5)
splot.set_ylim(0.0,2.5)

plt.savefig('photometric_uvj', format='pdf',bbox_inches='tight')
plt.show()


# checks out - now bin by mass - field goes from 10.2 to 11.4 in steps of 0.2 (6 bins)
#columns are central mass in bin, number sf, number q, fraction q
field_stats=np.zeros((6,6))
field_stats[:,0]=[10.3,10.5,10.7,10.9,11.1,11.3]
for i in range(6):
    centralmass=10.3+0.2*i
    field_stats[i,1]=len(field_sf[(field_sf>=centralmass-0.1) & (field_sf<centralmass+0.1)].values)
    field_stats[i,2]=len(field_quiescent[(field_quiescent>=centralmass-0.1) & (field_quiescent<centralmass+0.1)].values)
field_stats[:,3]=field_stats[:,2]/(field_stats[:,2]+field_stats[:,1])
#field_stats[:,4]=field_stats[:,3]-[0.156,0.217,0.183,0.285,0.209,0.128]
#field_stats[:,5]=abs(field_stats[:,3]-[0.274,0.358,0.319,0.445,0.479,0.469])
print(np.sum(field_stats[:,1]))
print(np.sum(field_stats[:,2]))

#now do the same thing for the cluster data:
cluster_q=pd.read_csv('cluster_uvjfastd4k_spec_q.csv')
cluster_sf=pd.read_csv('cluster_uvjfastd4k_spec_sf.csv')
c_q_mass=cluster_q['lmass']
c_sf_mass=cluster_sf['lmass']

cluster_stats=np.zeros((2,6))
cluster_stats[:,0]=[10.525,11.175]
for i in range(2):
    centralmass=10.525+0.65*i
    cluster_stats[i,1]=len(c_sf_mass[(c_sf_mass>=centralmass-0.325) & (c_sf_mass<centralmass+0.325)].values)
    cluster_stats[i,2]=len(c_q_mass[(c_q_mass>=centralmass-0.325) & (c_q_mass<centralmass+0.325)].values)
cluster_stats[:,3]=cluster_stats[:,2]/(cluster_stats[:,2]+cluster_stats[:,1])
cluster_stats[:,4]= cluster_stats[:,3]-[0.219,0.632]
cluster_stats[:,5]= abs(cluster_stats[:,3]-[0.605,0])
print(field_stats)
#plot the galaxy points
fig, splot = plt.subplots()

#kill the gridlines
splot.grid(False)
#plot a line at fraction=1
splot.plot([10.15,11.55],[1,1],color='Grey',linestyle='--',linewidth=3,zorder=1)
#now get the plot down:
cluster_errorbar=[[cluster_stats[0,4],cluster_stats[1,4]],[cluster_stats[0,5],0]]
splot.errorbar(cluster_stats[:,0], cluster_stats[:,3],yerr=cluster_errorbar,xerr=0.325,c='Red',marker='*',markersize=25,markeredgewidth=2.0,markeredgecolor='k',linestyle='None',capsize=5,label='IRC 0218',zorder=3)
splot.errorbar(field_stats[:,0], field_stats[:,3],yerr=(field_stats[:,4],field_stats[:,5]),xerr=0.1,c='DimGrey',markeredgecolor='DimGrey',marker='s',markersize=13,linestyle='None',markeredgewidth=1.5,capsize=5,label='z$\sim$1.6 Field',zorder=4)

splot.legend(loc=2, prop={'size':18})

#axes labels
splot.set_xlabel(r'$log(M/M_\odot)$', fontsize=18)
splot.set_ylabel(r'Quiescent Fraction', fontsize=18)

splot.text(10.56,0.43,'4/10',fontsize=18,color='k')
splot.text(11.2,0.925,'4/4',fontsize=18,color='k')

#fig.tight_layout()

plt.ylim(0,1.1)
plt.xlim(10.15,11.55)
plt.savefig('newman_diagram_justus', format='pdf',bbox_inches='tight')
plt.show()