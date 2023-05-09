import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

a = 1


def x(n, d):
    theta = np.arange(0, (16*np.pi)+0.05, 0.05)
    k = n/d
    if k == 1:
        return a * np.cos(k * theta) * np.cos(theta) - 0.5  # Keeps rose centered on (0,0)
    else:
        return a*np.cos(k*theta)*np.cos(theta)


def y(n, d):
    theta = np.arange(0, (16*np.pi) + 0.05, 0.05)
    k = n/d
    return a * np.sin(k * theta) * np.cos(theta)


# Initial values
n = 1
d = 1

# Creating the figure
fig, ax = plt.subplots()
plt.xlim(-2, 2)
plt.ylim(-1.3, 1.3)
line, = ax.plot(x(n, d), y(n, d))

fig.subplots_adjust(bottom=0.30)

# n slider
ax_n = fig.add_axes([0.25, 0.1, 0.65, 0.03])
nslid = Slider(
    ax=ax_n,
    label='d',
    valmin=1,
    valmax=9,
    valinit=1,
    valstep=1,
    initcolor='none'
)

# d slider
ax_d = fig.add_axes([0.25, 0.15, 0.65, 0.03])
dslid = Slider(
    ax=ax_d,
    label='n',
    valmin=1,
    valmax=7,
    valinit=1,
    valstep=1,
    initcolor='none'
)


# Define function that updates figure whenever slider value changes
def update(val):
    line.set_xdata(x(nslid.val, dslid.val))
    line.set_ydata(y(nslid.val, dslid.val))
    fig.canvas.draw_idle()


# Register the update function with the sliders
nslid.on_changed(update)
dslid.on_changed(update)

plt.show()

