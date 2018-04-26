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
import pylab
print(matplotlib.__version__)

matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)

field_sample=pd.read_csv('allcat.uvj.trim.FINAL.csv')
field_uv=field_sample['U-V']
field_vj=field_sample['V-J']
field_mass=field_sample['lmass']

# lzfield_sample=pd.read_csv('allcat.uvj.Z1FIELD.csv') original
lzfield_sample=pd.read_csv('CHECK_joined_z1_mass_3dhst.csv')
lzfield_uv=lzfield_sample['U-V']
lzfield_vj=lzfield_sample['V-J']
lzfield_mass=lzfield_sample['lmass']

# u1field_sample=pd.read_csv('UVISTA.trim.Z1FIELD.csv') original
u1field_sample=pd.read_csv('UVISTA_wider_lowz.csv')
u1field_uv=u1field_sample['U-V']
u1field_vj=u1field_sample['V-J']
u1field_mass=u1field_sample['lmass']

u16field_sample=pd.read_csv('UVISTA.trim.Z16FIELD.csv')
u16field_uv=u16field_sample['U-V']
u16field_vj=u16field_sample['V-J']
u16field_mass=u16field_sample['lmass']

wuyts={'uvcut':1.3,'vjcut':1.6,'slope':0.88,'intercept':0.49}
whitaker={'uvcut':1.3,'vjcut':1.5,'slope':0.8,'intercept':0.7}
muzzinlz={'uvcut':1.3,'vjcut':1.5,'slope':0.88,'intercept':0.69}
muzzinhz={'uvcut':1.3,'vjcut':1.5,'slope':0.88,'intercept':0.59}
nantais={'uvcut':1.3, 'vjcut': 1.6, 'slope':0.7/0.8, 'intercept': 1.3 - 0.8*0.7/0.8}
#change the uvj cuts applied to the FIELD SAMPLE ONLY
definitionary='whitaker'
if definitionary=='wuyts':
    active=wuyts
elif definitionary=='whitaker':
    active=whitaker
elif definitionary=='nantais':
    active=nantais

#the 3dhst selection needs to be whitaker 2012
field_quiescent=field_mass[(field_uv>active['uvcut']) & (field_vj<active['vjcut']) & (field_uv>active['slope']*field_vj+active['intercept'])]
field_sf=field_mass[(field_uv<[active['uvcut']]) | (field_vj>active['vjcut']) | ((field_uv>active['uvcut']) & (field_vj<active['vjcut']) & (field_uv<active['slope']*field_vj+active['intercept']))]

lzfield_quiescent=lzfield_mass[(lzfield_uv>active['uvcut']) & (lzfield_vj<active['vjcut']) & (lzfield_uv>active['slope']*lzfield_vj+active['intercept'])]
lzfield_sf=lzfield_mass[(lzfield_uv<[active['uvcut']]) | (lzfield_vj>active['vjcut']) | ((lzfield_uv>active['uvcut']) & (lzfield_vj<active['vjcut']) & (lzfield_uv<active['slope']*lzfield_vj+active['intercept']))]

#change the ultravista selection to be muzzin
active=muzzinlz
u1field_quiescent=u1field_mass[(u1field_uv>active['uvcut']) & (u1field_vj<active['vjcut']) & (u1field_uv>active['slope']*u1field_vj+active['intercept'])]
u1field_sf=u1field_mass[(u1field_uv<[active['uvcut']]) | (u1field_vj>active['vjcut']) | ((u1field_uv>active['uvcut']) & (u1field_vj<active['vjcut']) & (u1field_uv<active['slope']*u1field_vj+active['intercept']))]

active=muzzinhz
u16field_quiescent=u16field_mass[(u16field_uv>active['uvcut']) & (u16field_vj<active['vjcut']) & (u16field_uv>active['slope']*u16field_vj+active['intercept'])]
u16field_sf=u16field_mass[(u16field_uv<[active['uvcut']]) | (u16field_vj>active['vjcut']) | ((u16field_uv>active['uvcut']) & (u16field_vj<active['vjcut']) & (u16field_uv<active['slope']*u16field_vj+active['intercept']))]


cooke_data=pd.read_csv('cooke_data.csv')
cooke_mass=cooke_data['mass'].values
cooke_fq=cooke_data['fq'].values
cooke_uppere=cooke_data['perror'].values
cooke_uppere[2]=0.0
cooke_lowere=cooke_data['merror'].values


gclass_data=pd.read_csv('balogh_gclass.csv')
gclass_mass=gclass_data['mass'].values
gclass_fq=gclass_data['fq'].values
gclass_uppere=gclass_data['perror'].values
gclass_lowere=gclass_data['merror'].values


geec2_data=pd.read_csv('balogh_geec2.csv')
geec2_mass=geec2_data['mass'].values[2:]
geec2_fq=geec2_data['fq'].values[2:]
geec2_uppere=geec2_data['perror'].values[2:]
geec2_lowere=geec2_data['merror'].values[2:]


newman_data=pd.read_csv('newman_data.csv')
newman_mass=newman_data['mass'].values
newman_fq=newman_data['fq'].values
newman_uppere=newman_data['perror'].values
newman_lowere=newman_data['merror'].values
newman_lowerm=newman_data['merror_mass'].values
newman_upperm=newman_data['perror_mass'].values

lowzdata=pd.read_csv('vdb13.csv')
lowzmass=lowzdata['lmass'].values
lowzfq=lowzdata['fq'].values
lowzfqlu=lowzfq-lowzdata['fqlu'].values
lowzfquu=lowzdata['fquu'].values-lowzfq

balogh_sdss=pd.read_csv('balogh_sdss.csv')
sdss_mass=balogh_sdss['mass'].values
sdss_fq=balogh_sdss['fq'].values

#double check to make sure sifting was okay - plot uvj diagram for photometric sample
#double check to make sure the sifting did what it was supposed to: plot uvj
active=whitaker
field_quiescent_uv=field_uv[(field_uv>active['uvcut']) & (field_vj<active['vjcut']) & (field_uv>active['slope']*field_vj+active['intercept'])]
field_sf_uv=field_uv[(field_uv<active['uvcut']) | (field_vj>active['vjcut']) | ((field_uv>active['uvcut']) & (field_vj<active['vjcut']) & (field_uv<active['slope']*field_vj+active['intercept']))]

field_quiescent_vj=field_vj[(field_uv>active['uvcut']) & (field_vj<active['vjcut']) & (field_uv>active['slope']*field_vj+active['intercept'])]
field_sf_vj=field_vj[(field_uv<active['uvcut']) | (field_vj>active['vjcut']) | ((field_uv>active['uvcut']) & (field_vj<active['vjcut']) & (field_uv<active['slope']*field_vj+active['intercept']))]

fig, splot = plt.subplots()
splot.grid(False)
splot.set_xlabel(r'$(V-J)_{AB}$', fontsize=18)
splot.set_ylabel(r'$(U-V)_{AB}$', fontsize=18)
splot.text(0.22,2.2,'Quiescent',fontsize=18,color='k')
splot.text(1.45,0.22,'Star Forming',fontsize=18,color='k')


#plot the UVJ SF/Q cut lines for the whitaker selection
splot.plot([0.0,(active['uvcut']-active['intercept'])/active['slope']],[active['uvcut'],active['uvcut']],color='White',linestyle='-',linewidth=5,zorder=6)
splot.plot([(active['uvcut']-active['intercept'])/active['slope'],active['vjcut']],[active['uvcut'],active['slope']*active['vjcut']+active['intercept']],color='White',linestyle='-',linewidth=5,zorder=6)
splot.plot([active['vjcut'],active['vjcut']],[active['slope']*active['vjcut']+active['intercept'],2.5],color='White',linestyle='-',linewidth=5,zorder=6)

splot.plot([0.0,(active['uvcut']-active['intercept'])/active['slope']],[active['uvcut'],active['uvcut']],color='k',linestyle='-',linewidth=4,zorder=7)
DHSTUVJ, = splot.plot([(active['uvcut']-active['intercept'])/active['slope'],active['vjcut']],[active['uvcut'],active['slope']*active['vjcut']+active['intercept']],color='k',label='3D-HST',linestyle='-',linewidth=4,zorder=7)
splot.plot([active['vjcut'],active['vjcut']],[active['slope']*active['vjcut']+active['intercept'],2.5],color='k',linestyle='-',linewidth=4,zorder=7)


#plot the UVJ SF/Q cut lines for the muzzin selection
active=muzzinlz

splot.plot([0.0,(active['uvcut']-active['intercept'])/active['slope']],[active['uvcut'],active['uvcut']],color='White',linestyle='--',linewidth=5,zorder=6)
splot.plot([(active['uvcut']-active['intercept'])/active['slope'],active['vjcut']],[active['uvcut'],active['slope']*active['vjcut']+active['intercept']],color='White',linestyle='--',linewidth=5,zorder=6)
splot.plot([active['vjcut'],active['vjcut']],[active['slope']*active['vjcut']+active['intercept'],2.5],color='White',linestyle='--',linewidth=5,zorder=6)

splot.plot([0.0,(active['uvcut']-active['intercept'])/active['slope']],[active['uvcut'],active['uvcut']],color='Red',linestyle='--',linewidth=4,zorder=7)
UVISTUVJ, = splot.plot([(active['uvcut']-active['intercept'])/active['slope'],active['vjcut']],[active['uvcut'],active['slope']*active['vjcut']+active['intercept']],color='Red', label='UltraVISTA', linestyle='--',linewidth=4,zorder=7)
splot.plot([active['vjcut'],active['vjcut']],[active['slope']*active['vjcut']+active['intercept'],2.5],color='Red',linestyle='--',linewidth=4,zorder=7)

active=whitaker
splot.scatter(field_vj, field_uv, c='k', s=10, alpha=1.0,linewidths=0,zorder=5)
splot.scatter(u16field_vj, u16field_uv, c='DimGray', s=2, alpha=1.0,linewidths=0,zorder=4)
splot.text(1.93,0.06,'z=1.6',weight='ultralight',fontsize=16, color='k')
#splot.scatter(field_sf_vj, field_sf_uv, c='RoyalBlue', s=100, alpha=1.0,linewidths=2,zorder=5)

fig.tight_layout()
splot.set_aspect('equal')

#set plot limits
splot.set_xticks(np.arange(0.0,3.0,0.5))
splot.set_yticks(np.arange(0.5,3.0,0.5))

splot.set_xlim(0.0,2.5)
splot.set_ylim(0.0,2.5)

splot.legend(handles=[DHSTUVJ, UVISTUVJ],
             loc=3, prop={'size':14},labelspacing=0.3)

plt.savefig('test', format='pdf',bbox_inches='tight')
plt.show()

# checks out - now bin by mass - field goes from 10.2 to 11.4 in steps of 0.2 (6 bins)
#columns are central mass in bin, number sf, number q, fraction q
field_stats=np.zeros((6,6))
field_stats[:,0]=[10.3,10.5,10.7,10.9,11.1,11.3]
for i in range(6):
    centralmass=10.3+0.2*i
    if i == 5:
        addition = 0.1
    else:
        addition = 0.0
    field_stats[i,1]=len(field_sf[(field_sf>=centralmass-0.101) & (field_sf<centralmass+0.099+addition)].values)
    field_stats[i,2]=len(field_quiescent[(field_quiescent>=centralmass-0.101) & (field_quiescent<centralmass+0.099+addition)].values)
field_stats[:,3]=field_stats[:,2]/(field_stats[:,2]+field_stats[:,1])
field_stats[:,4]=field_stats[:,3]-[0.149981,0.262107,0.365454,0.417666,0.367495,0.358661] #lower fraction 68
field_stats[:,5]=abs(field_stats[:,3]-[0.194681,0.318744,0.430677,0.507036,0.48813,0.512062]) #upper fraction 68
print "high z 3dhst field"
print field_stats[:,0:3]
#now do the same thing for the cluster data:
cluster_q=pd.read_csv('cluster_uvjfastd4k_spec_q.csv')
cluster_sf=pd.read_csv('cluster_uvjfastd4k_spec_sf.csv')
c_q_mass=cluster_q['lmass']
c_sf_mass=cluster_sf['lmass']

#lowzfield
lzfield_stats=np.zeros((6,6))
lzfield_stats[:,0]=[10.3,10.5,10.7,10.9,11.1,11.3]
for i in range(6):
    centralmass=10.3+0.2*i
    if i == 5:
        addition = 0.1
    else:
        addition = 0.0
    lzfield_stats[i,1]=len(lzfield_sf[(lzfield_sf>=centralmass-0.1) & (lzfield_sf<centralmass+0.1+addition)].values)
    lzfield_stats[i,2]=len(lzfield_quiescent[(lzfield_quiescent>=centralmass-0.1) & (lzfield_quiescent<centralmass+0.1+addition)].values)
lzfield_stats[:,3]=lzfield_stats[:,2]/(lzfield_stats[:,2]+lzfield_stats[:,1])
lzfield_stats[:,4]=lzfield_stats[:,3]-[0.24288,0.307124,0.285773,0.358857,0.329674,0.460727] #lower fraction 68
lzfield_stats[:,5]=abs(lzfield_stats[:,3]-[0.303068,0.37198,0.360796,0.451881,0.467631,0.697817]) #upper fraction 68

print "low z 3dhst field stats"
print lzfield_stats[:,0:3]

#u1 field
u1field_stats=np.zeros((6,6))
u1field_stats[:,0]=[10.3,10.5,10.7,10.9,11.1,11.3]
for i in range(6):
    centralmass=10.3+0.2*i
    if i == 5:
        addition = 0.1
    else:
        addition = 0.0
    u1field_stats[i,1]=len(u1field_sf[(u1field_sf>=centralmass-0.1) & (u1field_sf<centralmass+0.1+addition)].values)
    u1field_stats[i,2]=len(u1field_quiescent[(u1field_quiescent>=centralmass-0.1) & (u1field_quiescent<centralmass+0.1+addition)].values)
u1field_stats[:,3]=u1field_stats[:,2]/(u1field_stats[:,2]+u1field_stats[:,1])
u1field_stats[:,4]=u1field_stats[:,3]-[0.302109,0.36868,0.450865,0.555961,0.671523,0.770278] #lower fraction 68
u1field_stats[:,5]=abs(u1field_stats[:,3]-[0.318531,0.386384,0.472046,0.582363,0.707244,0.821761]) #upper fraction 68

print "low z uvista field"
print u1field_stats[:,0:3]


#u16 field
u16field_stats=np.zeros((6,6))
u16field_stats[:,0]=[10.3,10.5,10.7,10.9,11.1,11.3]
for i in range(6):
    centralmass=10.3+0.2*i
    if i == 5:
        addition = 0.1
    else:
        addition = 0.0
    u16field_stats[i,1]=len(u16field_sf[(u16field_sf>=centralmass-0.1) & (u16field_sf<centralmass+0.1+addition)].values)
    u16field_stats[i,2]=len(u16field_quiescent[(u16field_quiescent>=centralmass-0.1) & (u16field_quiescent<centralmass+0.1+addition)].values)
u16field_stats[:,3]=u16field_stats[:,2]/(u16field_stats[:,2]+u16field_stats[:,1])
u16field_stats[:,4]=u16field_stats[:,3]-[0.190069,0.253444,0.371834,0.444419,0.521764,0.543415] #lower fraction 68
u16field_stats[:,5]=abs(u16field_stats[:,3]-[0.21034,0.277136,0.403148,0.483061,0.582945,0.663602]) #upper fraction 68
print("high z uvista field")
print u16field_stats[:,0:3]
print 'END U16 FIELD STATS'

cluster_stats=np.zeros((2,6))
cluster_stats[:,0]=[10.525,11.175]
for i in range(2):
    centralmass=10.525+0.650*i
    cluster_stats[i,1]=len(c_sf_mass[(c_sf_mass>=centralmass-0.325) & (c_sf_mass<centralmass+0.325)].values)
    cluster_stats[i,2]=len(c_q_mass[(c_q_mass>=centralmass-0.325) & (c_q_mass<centralmass+0.325)].values)
cluster_stats[:,3]=cluster_stats[:,2]/(cluster_stats[:,2]+cluster_stats[:,1])
cluster_stats[:,4]= cluster_stats[:,3]-[0.21983,0.632]
cluster_stats[:,5]= abs(cluster_stats[:,3]-[0.60469,0])
#print(field_stats)
print(cluster_stats)
#plot the galaxy points
fig, splot = plt.subplots()

aa=1.0
#kill the gridlines
splot.grid(False)
#plot a line at fraction=1
splot.plot([8,12.0],[1,1],color='Grey',linestyle='--',linewidth=3,zorder=1)
#now get the plot down:
"""
cluster_errorbar=[[cluster_stats[0,4],cluster_stats[1,4]],[cluster_stats[0,5],0]]
splot.errorbar(cluster_stats[:,0], cluster_stats[:,3],yerr=cluster_errorbar,xerr=0.325,c='Red',marker='*',markersize=25,markeredgewidth=2.0,markeredgecolor='k',capsize=5,label='IRC 0218, z=1.62',zorder=3)
cluster_points, = splot.plot(cluster_stats[:,0], cluster_stats[:,3],c='Red',marker='*',markersize=16,markeredgewidth=2.0,linewidth=0, markeredgecolor='k',label='IRC 0218, z = 1.62',zorder=1)

splot.errorbar(cooke_mass,cooke_fq,yerr=(cooke_lowere,cooke_uppere),markersize=13,marker='o',c='DarkOrange',markeredgewidth=1.5,markeredgecolor='DarkOrange',capsize=5,label='Cooke+ 2016, z=1.58',zorder=2,alpha=aa)
cooke_points, = splot.plot(cooke_mass,cooke_fq,markersize=11,marker='o',c='DarkOrange',markeredgewidth=1.5,linewidth=0, markeredgecolor='DarkOrange',label='Cooke+ 2016, z = 1.58',zorder=1,alpha=aa)


splot.errorbar(newman_mass,newman_fq,yerr=(newman_lowere,newman_uppere),xerr=(newman_lowerm,newman_upperm),c='Violet',marker='^',markersize=13,markeredgewidth=1.5,markeredgecolor='Violet',capsize=5,label='JKCS 041, z=1.80',zorder=2,alpha=aa)
newman_points, = splot.plot(newman_mass,newman_fq,c='Violet',marker='^',markersize=11,markeredgewidth=1.5,linewidth=0, markeredgecolor='Violet',label='JKCS 041, z = 1.80',zorder=1,alpha=aa)
"""

#errorbars on the balogh stuff are backwards, so fixed in the plotting command

#plot lowz cluster stuff
splot.errorbar(gclass_mass,gclass_fq,yerr=(gclass_uppere,gclass_lowere),markersize=13,marker='o',markeredgewidth=1.5,c='RoyalBlue',markeredgecolor='RoyalBlue',capsize=5,alpha=aa,zorder=5)
blue_circles, = splot.plot(gclass_mass,gclass_fq,markersize=9,marker='o',markeredgewidth=1.5,c='RoyalBlue',markeredgecolor='RoyalBlue', linewidth=0, label='GCLASS Clusters',alpha=aa,zorder=5)

splot.errorbar(geec2_mass,geec2_fq,yerr=(geec2_uppere,geec2_lowere),markersize=13,marker='^',markeredgewidth=1.5,c='Green',markeredgecolor='Green',capsize=5,alpha=aa,zorder=4)
green_triangles, = splot.plot(geec2_mass,geec2_fq, markersize=9,marker='^',markeredgewidth=1.5,c='Green',markeredgecolor='Green', linewidth=0,label='GEEC2 Groups',alpha=aa,zorder=4)


"""
#plot high z 3dhst field
field_stats[5,0]=11.35
splot.errorbar(field_stats[:,0], field_stats[:,3],yerr=(field_stats[:,4],field_stats[:,5]),xerr=(0.1,0.1,0.1,0.1,0.1,0.15),c='DimGrey',markeredgecolor='DimGrey',marker='s',markersize=13,linestyle='None',markeredgewidth=1.5,capsize=5,label='z$\sim$1.6 Field',zorder=0,alpha=aa)
gray_squares, = splot.plot(field_stats[:,0], field_stats[:,3],c='DimGrey',markeredgecolor='DimGrey',marker='s',markersize=11,linestyle='None',markeredgewidth=1.5,label='3D-HST z = 1.6 Field',zorder=0,alpha=aa)
"""


#plot 3dhst lowz field
lzfield_stats[5,0] = 11.35
splot.errorbar(lzfield_stats[:,0], lzfield_stats[:,3],yerr=(lzfield_stats[:,4],lzfield_stats[:,5]),xerr=(0.1,0.1,0.1,0.1,0.1,0.15),c='DimGrey',markeredgecolor='DimGrey',marker='s',markersize=13,linestyle='None',markeredgewidth=1.5,capsize=5,label='3D-HST z$\sim$1 Field',zorder=4,alpha=aa)
filled_squares, = splot.plot(lzfield_stats[:,0], lzfield_stats[:,3], c='DimGrey',markeredgecolor='DimGrey',marker='s',markersize=9,linestyle='None',markeredgewidth=1.5,label='3D-HST z$\sim$1 Field',zorder=4,alpha=aa)

#plot u1 field
u1field_stats[5,0] = 11.35
splot.errorbar(u1field_stats[:,0], u1field_stats[:,3],yerr=(u1field_stats[:,4],u1field_stats[:,5]),xerr=(0.1,0.1,0.1,0.1,0.1,0.15),c='Gray',markerfacecolor='White',markeredgecolor='Gray',marker='s',markersize=13,linestyle='None',markeredgewidth=3.0,capsize=5,zorder=3,alpha=aa)
hollow_squares, = splot.plot(u1field_stats[:,0], u1field_stats[:,3],c='Gray',markerfacecolor='none',markeredgecolor='Gray',marker='s',markersize=9,linestyle='None',markeredgewidth=3.0,label='UltraVISTA z$\sim$1 Field',zorder=2,alpha=aa)

#plot lowz field
#splot.errorbar(lowzmass, lowzfq,yerr=(lowzfqlu,lowzfquu),xerr=0.1,c='DimGrey',markeredgecolor='DimGray',marker='s',markersize=13,linestyle='None',markeredgewidth=1.5,capsize=5,label='z$\sim$1 Field',zorder=2,alpha=aa)
#splot.plot(sdss_mass,sdss_fq)

#adds in filled between area corresponding to upper and lower 68% bounds of high redshift cluster f_q
#add a filled polygon corresponding to f_q envelope, then add a line corresponding to the region where f_q = 1.0
poly=np.zeros((10,2))
poly[:,0]=[11.54,11.10,10.65,10.525,10.2,10.2,10.525,10.75,11.185,11.54]
poly[:,1]=[1.0,1.0,0.95,0.60469,0.50,0.16,0.21983,0.55485,0.632,0.632]
envelope=patches.Polygon(poly,closed=False, label='hello')
envelope.set_label('hello')
splot.add_artist(envelope)
envelope.set_facecolor('LightPink')
envelope.set_edgecolor('None')
#splot.plot([11.15,11.50],[0.94,0.94],color='LightPink',linewidth=3,zorder=2,label='High z Clusters')

#do the same for the high-z field so I can plot that on the low-z plot, use the upper and lower 68% confidence intervals
#as the bounds for the fillbetween
poly2=np.zeros((len(field_stats[:,0])*2,2))
field_stats[5,0] = 11.35
poly2[:len(field_stats[:,0]),0]=field_stats[:,0]
poly2[:len(field_stats[:,0]),1]=field_stats[:,3]-field_stats[:,4]

revmass=field_stats[:,0]
revmass=revmass[::-1]
upperbounds=field_stats[:,3]+field_stats[:,5]
upperbounds=upperbounds[::-1]
poly2[len(field_stats[:,0]):,0]=revmass
poly2[len(field_stats[:,0]):,1]=upperbounds
envelope2=patches.Polygon(poly2,closed=False,zorder=1)
splot.add_artist(envelope2)
envelope2.set_facecolor('LightGray')
envelope2.set_edgecolor('None')
#make a legend entry
#splot.plot([11.10,11.11],[0.25,0.25],color='LightGray',linewidth=3,zorder=1,label='High z Field')

u16field_stats[5,0]=11.35
#do the same for the u16 field so I can plot that on the low-z plot, use the upper and lower 68% confidence intervals
#as the bounds for the fillbetween
u16poly2=np.zeros((len(u16field_stats[:,0])*2,2))
u16poly2[:len(u16field_stats[:,0]),0]=u16field_stats[:,0]
u16poly2[:len(u16field_stats[:,0]),1]=u16field_stats[:,3]-u16field_stats[:,4]

u16poly2s=np.zeros((len(u16field_stats[:,0])*2,2))
u16poly2s[:len(u16field_stats[:,0]),0]=u16field_stats[:,0]
u16poly2s[:len(u16field_stats[:,0]),1]=u16field_stats[:,3]-u16field_stats[:,4]

u16revmasss=u16field_stats[:,0]
u16revmasss=u16revmasss[::-1]
u16upperboundss=u16field_stats[:,3]+u16field_stats[:,5]
u16upperboundss=u16upperboundss[::-1]
u16poly2s[len(u16field_stats[:,0]):,0]=u16revmasss
u16poly2s[len(u16field_stats[:,0]):,1]=u16upperboundss
u16envelope2s=patches.Polygon(u16poly2s,closed=False,zorder=1)
splot.add_artist(u16envelope2s)
u16envelope2s.set_facecolor('Gray')
u16envelope2s.set_alpha(0.5)
u16envelope2s.set_linewidth(0)

u16revmass=u16field_stats[:,0]
u16revmass=u16revmass[::-1]
u16upperbounds=u16field_stats[:,3]+u16field_stats[:,5]
u16upperbounds=u16upperbounds[::-1]
u16poly2[len(u16field_stats[:,0]):,0]=u16revmass
u16poly2[len(u16field_stats[:,0]):,1]=u16upperbounds
u16envelope2=patches.Polygon(u16poly2,closed=False,zorder=1, hatch='\/\/\/')
splot.add_artist(u16envelope2)
u16envelope2.set_facecolor('None')
u16envelope2.set_edgecolor('k')
u16envelope2.set_alpha(0.5)
u16envelope2.set_linewidth(0)

#dummyentry = matplotlib.patches.Rectangle((0,0),1,1,fc='White',fill='False', edgecolor='None', linewidth=0, label=r'z $\sim$ 1.6 results:')
pink_blob = matplotlib.patches.Patch(color='LightPink', label=r'z $\sim$ 1.6 Clusters')
gray_blob = matplotlib.patches.Patch(color='LightGray', label=r'3D-HST z $\sim$ 1.6 Field')
hatch_blob = matplotlib.patches.Patch(facecolor='LightGray',edgecolor='k', hatch='\/\/\/', label=r'UltraVISTA z $\sim$ 1.6 Field')

#these are now fancy arrows
opt = {'head_width': 0.07, 'head_length': 0.025, 'width': 0.035,
        'length_includes_head': True,'zorder':2}
# arrow to show how field fq would change under whitaker adoption
splot.add_patch(pylab.arrow(11.84,0.46,0,abs(0.46-0.52),color='Crimson',alpha=1.0,**opt))


splot.legend(handles=[blue_circles, green_triangles, filled_squares, hollow_squares, pink_blob, gray_blob, hatch_blob],
             bbox_to_anchor=(0., 1.01, 1., 0.101), loc=3, mode='expand', borderaxespad=0, prop={'size':14},labelspacing=0.2, ncol=2)

"""
splot.legend(handles=[cluster_points, cooke_points, newman_points, gray_squares],
             loc=4, prop={'size':14},labelspacing=0.3, ncol=1)
"""
#axes labels
splot.set_xlabel(r'$log(M/M_\odot)$', fontsize=18)
splot.set_ylabel(r'Quiescent Fraction', fontsize=18)

#fig.tight_layout()

plt.ylim(0,1.1)
plt.xlim(9.9,11.9)
plt.savefig('fq_lowz_final_select', format='pdf',bbox_inches='tight')
plt.show()