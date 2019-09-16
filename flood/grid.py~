import matplotlib.pyplot as plt
import scipy.ndimage
import numpy as np
from typing import Tuple, Union
from matplotlib.colors import Colormap


class FloodGrid:
    """
    A game where a grid is filled with many colors and your objective is to change the upper left contiguous
    region to a different color iteratively until the board is all one color.
    """
    def __init__(self, shape: Tuple[int, int], n_colors: int) -> None:
        """
        Initialize a board randomly
        :param shape: the size of the board in numpy shape form (10, 10) is a 10, 10 board
        :param n_colors: the number of colors in the game
        """
        self.shape = shape
        self.n_colors = n_colors

        self.grid = np.random.randint(1, self.n_colors + 1, size=self.shape)
        self.iterations = 0

    def show(self, cmap: Union[str, Colormap] = 'hsv') -> None:
        """
        Visualize the grid with Matplotlib
        :param cmap: a color map, either specified by a known name or custom designed colormap
        """
        fig, ax = plt.subplots()
        ax.imshow(self.grid, cmap=cmap, vmin=1, vmax=self.n_colors + 1)
        fig.show()

    def fill(self, color: int) -> None:
        """
        Set the upper left contiguous region as the specified color
        :param color: the integer color to set
        """
        assert color >= 1
        assert color <= self.n_colors

        # Find the upper left contiguous region and mask it
        labels = scipy.ndimage.label(self.grid == self.grid[0, 0])[0]
        mask = (labels == labels[0, 0])

        # Update the color
        self.grid[mask] = color
        self.iterations += 1

    def won(self) -> bool:
        """
        :return: whether the game has been won, i.e. the grid is all one color
        """
        return np.all(self.grid == self.grid[0, 0])

    def colors_remaining(self) -> int:
        """
        :return: the number of unique colors remaining in the game
        """
        return len(np.unique(self.grid))
