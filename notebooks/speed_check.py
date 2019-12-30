from timeit import default_timer as timer

from support import load_rent, load_bulldozer
from stratx.featimp import *
from stratx.partdep import *

np.random.seed(999)

n = 2_000
min_samples_leaf = 5
min_slopes_per_x = 15

X, y = load_rent(n=n)

# X, y = load_bulldozer()

X = X.iloc[-n:]
y = y.iloc[-n:]


for i in range(1):
    start = timer()

    I = importances(X, y)

    # I = impact_importances(X, y, catcolnames={'ModelID'}, n_jobs=1,
    #                        min_samples_leaf=20, min_slopes_per_x=15)
    plot_importances(I)
    I.reset_index().to_feather("/tmp/t.feather")
    # print(I)

    # leaf_xranges, leaf_slopes, slope_counts_at_x, dx, dydx, pdpx, pdpy, ignored = \
    #     partial_dependence(X=X, y=y, colname="Wvillage",
    #                        min_samples_leaf=min_samples_leaf,
    #                        min_slopes_per_x=min_slopes_per_x)

    # leaf_histos, avg_per_cat, ignored = \
    #     cat_partial_dependence(X, y, colname="ModelID",
    #                            min_samples_leaf=10)

    stop = timer()
    print(f"Time {i+1}: {stop-start:.1f}s")


# plot_catstratpd(X, y, "ModelID", "SalePrice", ntrees=2, min_y_shifted_to_zero=False,
#                 max_features=3)
# plt.show()

# plot_stratpd(X, y, "latitude", "price")
plt.show()


