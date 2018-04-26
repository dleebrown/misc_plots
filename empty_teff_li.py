"""plot empty A(li) vs Teff frame to work on in powerpoint for thesis presentation"""

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(11, 6))


plt.xticks(np.arange(4750, 7400, 250))
plt.yticks(np.arange(0.0, 4.1, 0.5))


plt.xlim((4600, 7400))
plt.ylim((0, 4.25))
plt.tick_params(labelsize=14)

plt.ylabel('A(Li) (dex)', fontsize=14)
plt.xlabel('Surface Temperature (K)', fontsize=14)
plt.gca().invert_xaxis()

plt.savefig('empty_teff_ali_plot', format='pdf',bbox_inches='tight')

plt.show()