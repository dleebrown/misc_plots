__author__ = 'donald'

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as patches
import math
import matplotlib.gridspec as gridspec

data=pd.read_csv('new_sp_complete_jrf.csv')
idcat=data['idcat'].values
jmag=data['Jmag'].values
idg102=data['ID_g102'].values

#change idg102: if present = 1, if not present 0
for entry in range(len(idg102)):
    if str(idg102[entry])!='nan':
        idg102[entry]=1.0
    else:
        idg102[entry]=0.0

#define min/max for bin ranges, number of bins
min=19.6
max=25.0
nbins=9.0
completeness=22.6

binwidth=(max-min)/nbins

#initialize array
array=np.zeros((int(nbins),4))

#fill in the bin centers, #phot, and #spec
for entry in range(int(nbins)):
    array[entry,0]=binwidth/2+entry*binwidth+min
    counterphot=0
    counterspec=0
    for entry2 in range(len(jmag)):
        if abs(jmag[entry2]-array[entry,0])<=binwidth/2:
            counterphot+=1
            counterspec+=idg102[entry2]
    array[entry,1]=counterphot
    array[entry,2]=counterspec

array[:,3]=array[:,2]/array[:,1]
print array

#make two subarrays: 1 for above sp complete, 1 below
subarray= np.split(array, np.where(array[:,0]>=completeness)[0])
subarraycomplete=subarray[0]
subarraynope=np.concatenate(subarray[1:])

fig, splot = plt.subplots()
#get some whitespace around the bars, plot the complete points
wspace=0.05
splot.bar(subarraycomplete[:,0]-binwidth/2+0.5*wspace,subarraycomplete[:,3],width=binwidth-wspace,color='FireBrick',edgecolor='White')

#plot the nope points with same whitespace
splot.bar(subarraynope[:,0]-binwidth/2+0.5*wspace,subarraynope[:,3],width=binwidth-wspace,color='LightCoral',edgecolor='White',hatch='///')

plt.ylim(0,1.08)
plt.xlim(19.6-0.5*wspace,25.0+0.5*wspace)

plt.tick_params(labelsize=24)
plt.xlabel(r'$J_{AB}$',fontsize=32)
plt.ylabel(r'$N_{sp}/N_{ph}$',fontsize=32)



plt.savefig("sp_complete",format='pdf',bbox_inches='tight')
plt.show()