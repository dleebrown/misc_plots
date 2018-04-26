"""plot the relative speedups afforded by different aspects of ANNA
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('../misc_data/annaspeed.csv', delimiter=',')
data = data[1:, 1:]

speedups = data[:, 0]
speednames = ['Baseline', 'Multilayer CNN', 'Parallelization\n(CPU)', 'Adaptive\nLearning', 'GPU Gradients\nCPU Preprocess']

print(speedups)

series = np.arange(np.size(speedups))

fig = plt.figure(figsize=(13, 4.5))

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(3.0)
ax.spines['left'].set_linewidth(3.0)

plt.xticks(series, speednames, rotation=0, ha='center', fontsize=16)

plt.ylabel('Relative Training Time', fontsize=16)
plt.bar(series, speedups, color='CornFlowerBlue')
plt.yticks([])
plt.text(2.85, 0.21, '6x', fontsize=32)
plt.text(3.78, 0.07, '38x', fontsize=32)


plt.savefig('anna_speedplot', format='pdf',bbox_inches='tight')

plt.show()

