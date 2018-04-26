"""plot of google search popularity of "machine learning" as well as the same term's popularity in published papers
(abstract and title) on ADS server in 6 month intervals, both from the period 2011-2018.
"""

import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(9,4.5))

ads_data = np.genfromtxt('7yr_ads_popularity.csv', delimiter=',')
ads_data = ads_data[1:, 1:]
ads_series = ads_data[:, 0]
ads_pop = ads_data[:, 2]/100.

google_data = np.genfromtxt('7yr_google_popularity.csv', delimiter=',')
google_data = google_data[1:, 1:]
google_series = google_data[:, 0]
google_pop = google_data[:, 2]/100.

x_vals = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
num_xvals = [1, 13, 25, 37, 49, 61, 73, 85]
dummy_yval = [0, 0, 0, 0, 0, 0, 0, 0]

plt.xticks(num_xvals, x_vals)
plt.scatter(num_xvals, dummy_yval, color='White')

plt.bar(ads_series, ads_pop, color='DarkCyan', width=5.5, alpha=1.0, zorder=2, label='New Refereed Articles on ADS with "Machine Learning" in Abstract')
plt.plot(google_series, google_pop, color='FireBrick', linewidth=8.0, alpha=1.0, zorder=4)
#plt.plot(google_series, google_pop, color='White', linewidth=15.0, alpha=1.0, zorder=3)

plt.fill_between(google_series[-2:-1], google_pop[-2:-1], color='IndianRed', linewidth=0.0, alpha=1.0, label='Google Search Popularity: "Machine Learning"', zorder=9)
#plt.fill_between(ads_series, ads_pop, color='SteelBlue', alpha=1.0, label='Refereed Articles Indexed by ADS with "Machine Learning" in Abstract', zorder=1)
plt.legend(bbox_to_anchor=(0.94, 1.185), frameon=False, prop={'size': 12})

plt.tick_params(labelsize=15)
plt.ylabel('Normalized Value', fontsize=15)
plt.yticks([])

plt.xlim(6.5, 77.5)
plt.ylim(0, 1.05)

plt.savefig('aas_popularity_plot', format='pdf',bbox_inches='tight')


plt.show()
