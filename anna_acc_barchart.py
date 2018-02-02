"""plot the relative accuracy improvements afforded by different aspects of ANNA
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('../misc_data/annaacc.csv', delimiter=',')
data = data[1:, 1:]

speedups = data[:, 2]
speednames = ['Baseline', 'Noise\nApproximation', 'Cross-Validation', 'Dropout\nRegularization', 'Multistage\nTraining']

print(speedups)

series = np.arange(np.size(speedups))

fig = plt.figure(figsize=(13, 4.5))

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(3.0)
ax.spines['left'].set_linewidth(3.0)

plt.xticks(series, speednames, rotation=0, ha='center', fontsize=16)

plt.ylabel('Relative Uncertainty', fontsize=16)
plt.bar(series, speedups, color='DarkRed')
plt.yticks([])
plt.text(3.685, 0.52, '2.05x', fontsize=32)


plt.savefig('anna_accplot', format='pdf',bbox_inches='tight')

plt.show()

