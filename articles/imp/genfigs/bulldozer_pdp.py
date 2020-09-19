from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.ensemble import RandomForestRegressor
from timeit import default_timer as timer
from sklearn.utils import resample

import shap
from sympy.simplify.radsimp import fraction_expand

#from support import load_bulldozer
import support
from stratx import plot_stratpd, plot_catstratpd, plot_catstratpd_gridsearch
from stratx import importances

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.set_printoptions(precision=2, suppress=True, linewidth=300, threshold=2000)

#np.random.seed(1)

# n = 25_000
# X, y = support.load_bulldozer(n)
X, y, X_train, X_test, y_train, y_test = support.load_dataset("bulldozer", "SalePrice")

X['auctioneerID'] = X['auctioneerID'].astype(np.int64)

# df = pd.read_csv("../../pd/bulldozer20k.csv")
# X = df.drop('SalePrice', axis=1)
# y = df['SalePrice']


I = importances(#X, y,
                X_train, y_train,
                n_trials=1,
                normalize=False,
                drop_high_stddev=2.0,
                min_samples_leaf=20,
                cat_min_samples_leaf=20,
                catcolnames={'AC', 'ModelID', 'auctioneerID'}
                )

print(I)
exit()

fig, ax = plt.subplots(1, 1)
pdpx, pdpy, ignored = \
    plot_stratpd(X, y, colname='YearMade', targetname='SalePrice',

                 # n_trials=1,
                 # n_trees=30,
                 # bootstrap=True,
                 # min_slopes_per_x=5*30,

                 n_trials=1,
                 bootstrap=True,
                 min_slopes_per_x=5,
                 min_samples_leaf=20,#200000,

                 show_slope_lines=False,#True,
                 show_impact=True,
                 figsize=(3.8,3.2),
                 show_x_counts=True,
                 show_impact_line=False,
                 show_impact_dots=False,
                 show_all_pdp=False,
                 impact_fill_color='#FEF5DC',
                 pdp_marker_size=3,
                 ax=ax
                 # xrange=(1960,2010),
                 # yrange=(-1000,45000)
                 )
# ax.set_xlim(0, 5)
# ax.set_ylim(-15000, 50_000)

plt.tight_layout()
plt.savefig(f"/Users/parrt/Desktop/james-ProductSize.pdf", pad_inches=0)
plt.show()

#


# y_ = y_.sample(frac=1.0, replace=False)
# X_['ModelID'] = X_['ModelID'].sample(frac=1.0, replace=False)

uniq_catcodes, combined_avg_per_cat, ignored = \
    plot_catstratpd(X, y, colname='ModelID', targetname='SalePrice',
                    n_trials=1,
                    min_samples_leaf=20,
                    show_unique_cat_xticks=False,
                    show_impact=True,
                    min_y_shifted_to_zero=True,
                    figsize=(5,5),
                    # yrange=(-150_000, 150_000),
                    verbose=False)
plt.title(f"ignored = {ignored}")
print("ignored",ignored)
plt.tight_layout()
plt.savefig(f"/Users/parrt/Desktop/james-ModelID.pdf", pad_inches=0)
# plt.savefig(f"/Users/parrt/Desktop/james-ModelID-10k-shuffled-x-not-y.pdf", pad_inches=0)
# plt.savefig(f"/Users/parrt/Desktop/james-ModelID-10k-shuffled.pdf", pad_inches=0)
plt.show()


# I = importances(X_, y_,
#                 min_samples_leaf=5,
#                 # min_slopes_per_x=5,
#                 n_trials=10,
#                 sort='Rank',
#                 catcolnames={'AC', 'ModelID'})
# print(I)
# I.to_csv("/tmp/t2.csv")

#plot_catstratpd(X_, y_, colname='ProductSize', targetname='SalePrice')


# plot_stratpd(X_, y_, colname='YearMade', targetname='SalePrice',
#              show_slope_lines=False,
#              show_impact=True,
#              min_samples_leaf=5,
#              min_slopes_per_x=7,
#              pdp_marker_cmap='coolwarm',#'YlGnBu',#'tab20b',
#              figsize=(4,3)
#              )
# plt.tight_layout()
# plt.savefig(f"/Users/parrt/Desktop/james-YearMade.pdf", pad_inches=0)
# plt.show()




# col = 'YearMade'
# plot_stratpd_gridsearch(X_, y_, colname=col, targetname='SalePrice',
#                         min_samples_leaf_values=(2,3,4,5,6,7),
#                         min_slopes_per_x_values=(2,3,5,6,7,8),
#                         show_slope_lines=False,
#                         show_impact=True
#                         #,yrange=(-20000,2000)
#                         )
# plt.tight_layout()
# plt.savefig(f"/Users/parrt/Desktop/james-{col}-grid.pdf", pad_inches=0)
# plt.show()

#
# plot_stratpd(X_, y_, colname='saledayofyear', targetname='SalePrice',
#              show_impact=True,
#              show_slope_lines=False)
# plt.tight_layout()
# plt.show()
# #
# plot_stratpd(X_, y_, colname='ProductSize', targetname='SalePrice',
#              show_impact=True,
#              show_slope_lines=False)
# plt.tight_layout()
# plt.show()




# I = importances(X_, y_, catcolnames={'AC', 'ModelID', 'ProductSize'},
#                 min_samples_leaf=10,
#                 min_slopes_per_x=5)
# print(I)


col = 'ModelID'
# col = 'ProductSize'

# plot_catstratpd_gridsearch(X, y, 'ModelID', 'SalePrice',
#                            min_samples_leaf_values=(2, 5, 10, 15, 20, 30),
#                            cellwidth=4.5,
#                            n_trials=1,
#                            show_impact=True,
#                            show_xticks=False,
#                            show_all_cat_deltas=False,
#                            min_y_shifted_to_zero=False)
# plt.savefig(f"/Users/parrt/Desktop/james-ModelID-grid-shuffled.pdf", pad_inches=0)
# # plt.savefig(f"/Users/parrt/Desktop/james-ModelID-grid.pdf", pad_inches=0)
# plt.show()

# plot_catstratpd(X_, y_, 'YearMade', 'SalePrice',
#                 min_samples_leaf=10,
#                 show_mean_line=True,
#                 sort=None,
#                 show_xticks=False,
#                 min_y_shifted_to_zero=False)

