import this
from math import sqrt

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


class DrawEllipseGoneWrong:
    # Theory used from: https://courses.lumenlearning.com/boundless-physics/chapter/keplers-laws/

    def __init__(self):
        print("Enter e:")
        e = input()
        print("Enter r_min (minimum radius of curvature)")
        rmin = input()
        rmax = (-rmin - (e * rmin)) / (e - 1)
        majAxis = rmin + rmax
        minAxis = 2 * sqrt(rmin * rmax)

    def draw(self):
        plt.figure()
        ax = plt.gca()
        ellipse = Ellipse(xy=(0, 0), width=self.__init__.majAxis, height=self.__init__.minAxis, edgecolor='r',
                          fc='None', lw=3)
        ax.add_patch(ellipse)