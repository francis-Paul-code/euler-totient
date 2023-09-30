import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.backend_bases import MouseEvent

matplotlib.use('TkAgg')

class Cursor:
    def __init__(self, ax):
        self.ax = ax
        self.horizontal_line = ax.axhline(color='k', lw=0.8, ls='--')
        self.vertical_line = ax.axvline(color='k', lw=0.8, ls='--')
        # text location in axes coordinates
        self.text = ax.text(0.72, 0.9, '', transform=ax.transAxes)

    def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(visible)
        self.vertical_line.set_visible(visible)
        self.text.set_visible(visible)
        return need_redraw

    def on_mouse_move(self, event):
        if not event.inaxes:
            need_redraw = self.set_cross_hair_visible(False)
            if need_redraw:
                self.ax.figure.canvas.draw()
        else:
            self.set_cross_hair_visible(True)
            x, y = event.xdata, event.ydata
            # update the line positions
            self.horizontal_line.set_ydata([y])
            self.vertical_line.set_xdata([x])
            self.text.set_text(f'x={x:1.2f}, y={y:1.2f}')
            self.ax.figure.canvas.draw()


def plot_graph(x: list[int], y: list[int]):
    fig, ax = plt.subplots()
    cursor = Cursor(ax)
    fig.canvas.mpl_connect('motion_notify_event', cursor.on_mouse_move)
    t = ax.transData
    MouseEvent(
        "motion_notify_event", ax.figure.canvas, *t.transform((0.5, 0.5))
    )._process()
    xpoints = np.array(x)
    ypoints = np.array(y)
    ax.scatter(xpoints, ypoints, s=3)
    plt.title("Euler's Totient Function")
    plt.xlabel("n")
    plt.ylabel("φ(n)")
    plt.show()
