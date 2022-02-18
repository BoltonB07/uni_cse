from math import sqrt

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse


# Theory used from: https://courses.lumenlearning.com/boundless-physics/chapter/keplers-laws/

def createEllipse():
    # input:
    print("Enter e:")
    e = float(input())
    print("Enter r_min (minimum radius of curvature)")
    rmin = float(input())

    # The calculation part:
    rmax = (-rmin - (e * rmin)) / (e - 1)
    majAxis = rmin + rmax
    minAxis = 2 * sqrt(rmin * rmax)

    # The plotting part:
    ellipse = Ellipse((50, 50), majAxis, minAxis, edgecolor='black', fc='lightgray', lw=1, hatch='x')
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    ax.add_artist(ellipse)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    plt.show()
createEllipse()