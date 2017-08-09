# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:29:18 2015

@author: donald
"""

from astropy.io import fits 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.gridspec as gridspec
fig=plt.figure(figsize=(4,4.5))
plt.subplots_adjust(hspace=0.001)

######################################################################################################################
#first galaxy

g33092=plt.subplot()

image=fits.open('/home/donald/Desktop/2017_backed_up/gregwork/new_g102/IRC0218A-G102_33092.new_zfit.fits')
image.info()
cont1d=image[3].data
cont1d=np.array(cont1d)
line1d=image[4].data
line1d=np.array(line1d)


image2=fits.open('/home/donald/Desktop/2017_backed_up/gregwork/new_g102/IRC0218A-G102_33092.1D.fits')
image2.info()
image2data=image2[1].data
wavelength=np.array(image2data.field(0))
#correct for redshift
wavelength=wavelength/(2.621)
flux=np.array(image2data.field(1))
contam=np.array(image2data.field(3))
sensitivity=np.array(image2data.field(6))
flux=(flux-contam)/sensitivity
totalmodel=(line1d+cont1d)/sensitivity

image4=fits.open('/home/donald/Desktop/2017_backed_up/gregwork/uds-18-G141_33092.new_zfit.fits')
image4.info()
cont1d4=image4[3].data
cont1d4=np.array(cont1d4)
line1d4=image4[4].data
line1d4=np.array(line1d4)

image3=fits.open('/home/donald/Desktop/2017_backed_up/gregwork/uds-18-G141_33092.1D.fits')
image3.info()
image3data=image3[1].data
wavelength2=np.array(image3data.field(0))
#correct for redshift
wavelength2=wavelength2/(2.621)
flux2=np.array(image3data.field(1))
contam2=np.array(image3data.field(3))
sensitivity2=np.array(image3data.field(6))
flux2=(flux2-contam2)/sensitivity2
totalmodel2=(line1d4+cont1d4)/sensitivity2

rs=Rectangle((4000,0),100,45)
bc=Rectangle((3850,0),100,45)
g33092.add_artist(bc)
g33092.add_artist(rs)

rs.set_facecolor('RoyalBlue')
bc.set_facecolor('RoyalBlue')
rs.set_alpha(0.6)
bc.set_alpha(0.6)
rs.set_edgecolor('White')
bc.set_edgecolor('White')
rs.set_hatch('//')
bc.set_hatch('//')

g33092.grid(False)
"""
g33092.plot(wavelength[np.where(wavelength>3000.0)[-1][1]:np.where(wavelength<4300.0)[-1][-1]],
           flux[np.where(wavelength>3000.0)[-1][1]:np.where(wavelength<4300.0)[-1][-1]],linewidth=2.0,color='RoyalBlue')
g33092.plot(wavelength2[np.where(wavelength2>4100.0)[-1][1]:np.where(wavelength2<6400.0)[-1][-1]],
           flux2[np.where(wavelength2>4100.0)[-1][1]:np.where(wavelength2<6400.0)[-1][-1]],linewidth=2.0,color='FireBrick')
"""
"""
#splot.plot(wavelength2[np.where(wavelength2>4100.0)[-1][1]:np.where(wavelength2<6400.0)[-1][-1]],
#           totalmodel2[np.where(wavelength2>4100.0)[-1][1]:np.where(wavelength2<6400.0)[-1][-1]],linewidth=9, color='White')
g33092.plot(wavelength2[np.where(wavelength2>4100.0)[-1][1]:np.where(wavelength2<6400.0)[-1][-1]],
           totalmodel2[np.where(wavelength2>4100.0)[-1][1]:np.where(wavelength2<6400.0)[-1][-1]],linewidth=3.0, color='Black')
"""
#splot.plot(wavelength[np.where(wavelength>3000.0)[-1][1]:np.where(wavelength<4300.0)[-1][-1]],
#           totalmodel[np.where(wavelength>3000.0)[-1][1]:np.where(wavelength<4300.0)[-1][-1]],linewidth=9,color='White')
g33092.plot(wavelength[np.where(wavelength>3000.0)[-1][1]:np.where(wavelength<4360.0)[-1][-1]],
           totalmodel[np.where(wavelength>3000.0)[-1][1]:np.where(wavelength<4360.0)[-1][-1]],linewidth=3.0,color='Black')

g33092.set_ylim([0.03,0.10])
g33092.set_ylabel(r'$F_{\lambda}$', fontsize=18)
#g33092.set_yticks(np.arange(0.02,0.15,0.03))

#####################################################################################################################
#global tweaks

plt.setp(g33092.get_yticklabels(), visible=False)


plt.xlabel(r'$\lambda_{Rest}$', fontsize=18)
plt.xlim([3550,4350])
g33092.tick_params(labelsize=12)

g33092.tick_params(axis='y', which='both', bottom='off', top='off')
g33092.axes.get_yaxis().set_ticks([])





plt.savefig("d4k_zoom",format='pdf', bbox_inches='tight')
plt.show()

'''
imagedata=image[5].data
print(imagedata)
'''
"""
wavelength=np.array(imagedata.field(0))
flux=np.array(imagedata.field(1))
error=np.array(imagedata.field(2))
contamination=np.array(imagedata.field(3))
print(contamination)
"""