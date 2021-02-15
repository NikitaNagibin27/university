import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

x = np.linspace(0, 4, 100)
y = x**0.5

fig, ax = plt.subplots()

ax.plot(x, y, color = 'cadetblue', linewidth = 2)
ax.vlines(0, y.min(), y.max(), color = 'deepskyblue', linewidth = 2)
ax.hlines(0, x.min(), x.max(), color = 'deepskyblue', linewidth = 2)

fig.set_figwidth(10); fig.set_figheight(15)

plt.show()
