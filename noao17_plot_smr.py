"""the noao 17 plot except shaded to highlight SMR stars and NGC 6253"""

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

fig, splot = plt.subplots(figsize=(9,5))
splot.grid(False)

richline2, = splot.plot([0.001*10**4,5*10**10],[3.5, 3.5],color='Plum', linestyle='-',linewidth=5,zorder=1, label='Metal-Rich $A(Li)_{initial}$')
richline, = splot.plot([0.001*10**4,5*10**10],[3.5, 3.5],color='Plum', linestyle='-',linewidth=30,zorder=1)

spiteline2, = splot.plot([0.001*10**4,5*10**10],[2.2,2.2],color='LightSkyBlue',linewidth=5,zorder=1, label='Spite et al. 2012')
spiteline, = splot.plot([0.001*10**4,5*10**10],[2.2,2.2],color='LightSkyBlue',linewidth=25,zorder=1)

"""
splot.errorbar(sestito_ages, sestito_abunds, yerr=sestito_unc, linestyle='None', elinewidth=3, capthick=3, capsize=5, color='FireBrick', zorder=2)
sestito_plt, = splot.semilogx(sestito_ages, sestito_abunds, markersize=11, color='FireBrick', marker='o', markeredgecolor='FireBrick', linewidth=0, label='Sestito & Randich 2005',zorder=3)

splot.errorbar(randich_ages, randich_abunds, yerr=randich_unc,linestyle='None', elinewidth=3, capthick=3, capsize=5, color='RoyalBlue', zorder=4)
randich_plt, = splot.semilogx(randich_ages, randich_abunds, markersize=11, color='RoyalBlue', markeredgecolor='RoyalBlue', marker='^', linewidth=0, label='Randich et al. 2009', zorder=5)
"""
splot.errorbar(cummings_ages, cummings_abunds, yerr=cummings_unc,linestyle='None', elinewidth=3, capthick=3, capsize=5, color='GoldenRod', zorder=5)
cummings_plt, = splot.semilogx(cummings_ages, cummings_abunds, markersize=11, color='GoldenRod', markeredgecolor='GoldenRod', marker='s', linewidth=0, label='Cummings et al. 2012', zorder=7)
cummings_plt2, = splot.semilogx(cummings_ages, cummings_abunds, markersize=13, color='White', markeredgecolor='White', marker='s', linewidth=0, label='Cummings et al. 2012', zorder=6)


"""
splot.errorbar(cummings17_ages[0], cummings17_abunds[0], yerr=cummings17_unc[0],linestyle='None', elinewidth=3, capthick=3, capsize=5, color='DarkSlateGray', zorder=8)
cummings17_plt2, = splot.semilogx(cummings17_ages[0], cummings17_abunds[0], markersize=11, color='DarkSlateGray', markeredgecolor='DarkSlateGray', marker='D', linewidth=0, label='Cummings et al. 2017', zorder=9)
"""
#splot.errorbar(cummings17_ages[1], cummings17_abunds[1], yerr=cummings17_unc[1],linestyle='None', elinewidth=5, capthick=5, capsize=7, color='White', zorder=10)
#cummings17_plt3, = splot.semilogx(cummings17_ages[1], cummings17_abunds[1], markersize=13, color='White', markeredgecolor='White', marker='D', linewidth=0,zorder=11)

#splot.errorbar(cummings17_ages[1], cummings17_abunds[1], yerr=cummings17_unc[1],linestyle='None', elinewidth=3, capthick=3, capsize=5, color='DarkSlateGray', zorder=12)
#cummings17_plt, = splot.semilogx(cummings17_ages[1], cummings17_abunds[1], markersize=11, color='DarkSlateGray', markeredgecolor='DarkSlateGray', marker='D', linewidth=0, zorder=13)

oc_line, = splot.plot([-20, -18], [-10, 10], color='LightSlateGray', linewidth=5, zorder=1, label='OC (Sestito+2005)')

# plot a band traced by the points
all_ages = sestito_ages #+ randich_ages + cummings_ages + cummings17_ages
all_abunds = sestito_abunds #+ randich_abunds + cummings_abunds + cummings17_abunds
all_lowunc = list([sestito_abunds[i] - sestito_unc[i] for i in range(len(sestito_abunds))])
all_upunc = list([sestito_abunds[i]+sestito_unc[i] for i in range(len(sestito_abunds))])


smr_err = np.zeros((2, 1))
smr_err[0, 0] = 0.5*10**9
smr_err[1, 0] = 1.0*10**9
# plot the SMR point
splot.errorbar(3.5*10**9, 2.55, xerr=smr_err, yerr=0.21, linestyle='None', elinewidth=3, capthick=3, capsize=5, color='FireBrick', zorder=7)
smr_plot, = splot.semilogx(3.5*10**9, 2.55, markersize=18, color='FireBrick', markeredgecolor='FireBrick', marker='*', linewidth=0, label='SMR Plateau', zorder=9)
smr_plot2, = splot.semilogx(3.5*10**9, 2.55, markersize=23, color='White', markeredgecolor='White', marker='*', linewidth=0, label='SMR Plateau', zorder=8)

#splot.plot(all_ages, all_abunds, linewidth=3.5, c='FireBrick')
splot.fill_between(all_ages, all_lowunc, all_upunc, color='LightSlateGray', zorder=3)


splot.set_xlim(5.2*10**6,7.85*10**9)
splot.set_ylim(1.75,3.75)
splot.set_xlabel(r'Age [$yr$]', fontsize=18)
splot.set_ylabel(r'A(Li) [$dex$]', fontsize=18)

splot.legend(handles=[smr_plot, cummings_plt, oc_line, spiteline2, richline2],
             loc=3, prop={'size':14},labelspacing=0.3)

plt.minorticks_on()
plt.savefig('/home/donald/Desktop/PYTHON/misc_data/dlb17_noao_smr', format='pdf',bbox_inches='tight')


plt.show()