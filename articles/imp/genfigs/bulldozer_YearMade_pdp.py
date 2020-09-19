from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.ensemble import RandomForestRegressor
from timeit import default_timer as timer
from sklearn.utils import resample

import shap
from sympy.simplify.radsimp import fraction_expand

from stratx import plot_stratpd
from support import load_dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.set_printoptions(precision=2, suppress=True, linewidth=300, threshold=2000)

n = 25_000
X, y, X_train, X_test, y_train, y_test = load_dataset("bulldozer", "SalePrice")

# Use just the training set like the top-k tests
plot_stratpd(X_train, y_train, colname='YearMade', targetname='SalePrice',
             n_trials=10,
             min_samples_leaf=20, # same as in top-k trials
             show_slope_lines=False,
             show_impact=False,
             pdp_marker_alpha=.7,
             pdp_marker_size=4,
             figsize=(3.8,2.9)
             )
plt.xlim(1965,2010)
plt.tight_layout()
plt.savefig(f"../images/bulldozer-YearMade.pdf", bbox_inches="tight",
            pad_inches=0)
plt.show()

