import matplotlib.pyplot as plt
import scipy.ndimage
import numpy as np

class FloodGrid:
    def __init__(self, shape, n_colors, clumpiness, distribution):
        self.shape = shape
        self.n_colors = n_colors
        self.clumpiness = clumpiness
        self.distribution = distribution

        self.grid = np.random.randint(1, self.n_colors + 1, size=self.shape)
        self.iterations = 0

    def show(self, cmap='hsv'):
        fig, ax = plt.subplots()
        ax.imshow(self.grid, cmap=cmap, vmin=1, vmax=self.n_colors + 1)
        fig.show()

    def fill(self, color):
        assert color >= 1
        assert color <= self.n_colors

        labels = scipy.ndimage.label(self.grid == self.grid[0, 0])[0]
        mask = (labels == labels[0, 0])
        self.grid[mask] = color
        self.iterations += 1

    def won(self):
        return np.all(self.grid == self.grid[0, 0])

    def colors_remaining(self):
        return len(np.unique(self.grid))