__author__ = 'donald'
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

sestito_ages = [0.005*10**9, 0.03*10**9, 0.05*10**9, 0.1*10**9, 0.15*10**9, 0.25*10**9, 0.6*10**9, 2*10**9, 5*10**9,
                8*10**9]
sestito_abunds = [3.21, 3.06, 2.96, 2.96, 2.85, 2.79, 2.58, 2.33, 2.25, 2.34]
sestito_unc = [0.17, 0.13, 0.10, 0.07, 0.11, 0.14, 0.15, 0.17, 0.12, 0.14]

randich_ages = [5*10**9]
randich_abunds = [2.47]
randich_unc = [0.16]

cummings_ages = [3.0*10**9]
cummings_abunds = [2.43]
cummings_unc = [0.15]

cummings17_ages = [0.625*10**9, 0.650*10**9]
cummings17_abunds = [2.91, 2.72]
cummings17_unc = [0.09, 0.28]

fig, splot = plt.subplots()
splot.grid(False)
richline2, = splot.plot([0.001*10**4,5*10**10],[3.5, 3.5],color='Plum', linestyle='-',linewidth=5,zorder=1, label='Metal-Rich $A(Li)_{initial}$')
richline, = splot.plot([0.001*10**4,5*10**10],[3.5, 3.5],color='Plum', linestyle='-',linewidth=30,zorder=1)

spiteline2, = splot.plot([0.001*10**4,5*10**10],[2.2,2.2],color='LightSkyBlue',linewidth=5,zorder=1, label='Spite et al. 2012')
spiteline, = splot.plot([0.001*10**4,5*10**10],[2.2,2.2],color='LightSkyBlue',linewidth=25,zorder=1)

splot.errorbar(sestito_ages, sestito_abunds, yerr=sestito_unc, linestyle='None', elinewidth=3, capthick=3, capsize=5, color='FireBrick', zorder=2)
sestito_plt, = splot.semilogx(sestito_ages, sestito_abunds, markersize=11, color='FireBrick', marker='o', markeredgecolor='FireBrick', linewidth=0, label='Sestito & Randich 2005',zorder=3)

splot.errorbar(randich_ages, randich_abunds, yerr=randich_unc,linestyle='None', elinewidth=3, capthick=3, capsize=5, color='RoyalBlue', zorder=4)
randich_plt, = splot.semilogx(randich_ages, randich_abunds, markersize=11, color='RoyalBlue', markeredgecolor='RoyalBlue', marker='^', linewidth=0, label='Randich et al. 2009', zorder=5)

splot.errorbar(cummings_ages, cummings_abunds, yerr=cummings_unc,linestyle='None', elinewidth=3, capthick=3, capsize=5, color='GoldenRod', zorder=6)
cummings_plt, = splot.semilogx(cummings_ages, cummings_abunds, markersize=11, color='GoldenRod', markeredgecolor='GoldenRod', marker='s', linewidth=0, label='Cummings et al. 2012', zorder=7)

splot.errorbar(cummings17_ages[0], cummings17_abunds[0], yerr=cummings17_unc[0],linestyle='None', elinewidth=3, capthick=3, capsize=5, color='DarkSlateGray', zorder=8)
cummings17_plt2, = splot.semilogx(cummings17_ages[0], cummings17_abunds[0], markersize=11, color='DarkSlateGray', markeredgecolor='DarkSlateGray', marker='D', linewidth=0, label='Cummings et al. 2017', zorder=9)

#splot.errorbar(cummings17_ages[1], cummings17_abunds[1], yerr=cummings17_unc[1],linestyle='None', elinewidth=5, capthick=5, capsize=7, color='White', zorder=10)
#cummings17_plt3, = splot.semilogx(cummings17_ages[1], cummings17_abunds[1], markersize=13, color='White', markeredgecolor='White', marker='D', linewidth=0,zorder=11)


splot.errorbar(cummings17_ages[1], cummings17_abunds[1], yerr=cummings17_unc[1],linestyle='None', elinewidth=3, capthick=3, capsize=5, color='DarkSlateGray', zorder=12)
cummings17_plt, = splot.semilogx(cummings17_ages[1], cummings17_abunds[1], markersize=11, color='DarkSlateGray', markeredgecolor='DarkSlateGray', marker='D', linewidth=0, zorder=13)


splot.set_xlim(0.002*10**9,2*10**10)
splot.set_ylim(1.75,3.75)
splot.set_xlabel(r'Age [$yr$]', fontsize=18)
splot.set_ylabel(r'A(Li) [$dex$]', fontsize=18)

splot.legend(handles=[sestito_plt, randich_plt, cummings_plt, cummings17_plt2, spiteline2, richline2],
             loc=3, prop={'size':14},labelspacing=0.3)

plt.minorticks_on()
plt.savefig('dlb17_noao', format='eps',bbox_inches='tight')


plt.show()