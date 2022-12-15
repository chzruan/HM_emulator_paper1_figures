import numpy as np
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import gridspec
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams.update({'font.size': 20})
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{physics}'
params = {'xtick.top': True, 'ytick.right': True, 'xtick.direction': 'in', 'ytick.direction': 'in'}
plt.rcParams.update(params)
#ax00.xaxis.set_ticklabels([])
from cycler import cycler
custom_cycler = (cycler(color=['mediumblue', 'orange', 'mediumseagreen', 'red', 'purple', 'magenta', 'green', 'black']))
# ax00.set_prop_cycle(custom_cycler)


import pandas as pd




fig = plt.figure(
    figsize=(12, 12),
)
gs = gridspec.GridSpec(4, 4, wspace=0, hspace=0)

ax00 = plt.subplot(gs[0, 0])
ax03 = plt.subplot(gs[0, 3])

ax10 = plt.subplot(gs[1, 0])
ax11 = plt.subplot(gs[1, 1])

ax20 = plt.subplot(gs[2, 0])
ax21 = plt.subplot(gs[2, 1])
ax22 = plt.subplot(gs[2, 2])

ax30 = plt.subplot(gs[3, 0])
ax31 = plt.subplot(gs[3, 1])
ax32 = plt.subplot(gs[3, 2])
ax33 = plt.subplot(gs[3, 3])




# test, inner 50%
foldNum = 1
for sliceIndex in range(foldNum):
    nodeParams_df = pd.read_csv(
        f'./data/testNodeParams_500nodes_1folds_slice0.csv',
    )

    ax00.plot(
        nodeParams_df["Om0"],
        nodeParams_df["Ob0"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )
    ax03.plot(
        nodeParams_df["w0"],
        nodeParams_df["wa"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )

    ax10.plot(
        nodeParams_df["Om0"],
        nodeParams_df["h"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )
    ax20.plot(
        nodeParams_df["Om0"],
        nodeParams_df["sigma8"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )
    ax30.plot(
        nodeParams_df["Om0"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )

    ax11.plot(
        nodeParams_df["Ob0"],
        nodeParams_df["h"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )
    ax21.plot(
        nodeParams_df["Ob0"],
        nodeParams_df["sigma8"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )
    ax31.plot(
        nodeParams_df["Ob0"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )

    ax22.plot(
        nodeParams_df["h"],
        nodeParams_df["sigma8"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )
    ax32.plot(
        nodeParams_df["h"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )

    ax33.plot(
        nodeParams_df["sigma8"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=1.5, alpha=0.55,
        color="lightseagreen", 
    )



# test, inner 50%
foldNum = 1
for sliceIndex in range(foldNum):
    nodeParams_df = pd.read_csv(
        f'./data/testInner50NodeParams_200nodes_1folds_slice0.csv',
    )

    ax00.plot(
        nodeParams_df["Om0"],
        nodeParams_df["Ob0"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )
    ax03.plot(
        nodeParams_df["w0"],
        nodeParams_df["wa"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )

    ax10.plot(
        nodeParams_df["Om0"],
        nodeParams_df["h"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )
    ax20.plot(
        nodeParams_df["Om0"],
        nodeParams_df["sigma8"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )
    ax30.plot(
        nodeParams_df["Om0"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )

    ax11.plot(
        nodeParams_df["Ob0"],
        nodeParams_df["h"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )
    ax21.plot(
        nodeParams_df["Ob0"],
        nodeParams_df["sigma8"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )
    ax31.plot(
        nodeParams_df["Ob0"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )

    ax22.plot(
        nodeParams_df["h"],
        nodeParams_df["sigma8"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )
    ax32.plot(
        nodeParams_df["h"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )

    ax33.plot(
        nodeParams_df["sigma8"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=3, alpha=0.4,
        color="mediumblue", 
    )




foldNum = 5
for sliceIndex in range(foldNum):
    nodeParams_df = pd.read_csv(
        f'./data/nodeParams_50nodes_{foldNum}folds_slice{sliceIndex}.csv',
    )

    ax00.plot(
        nodeParams_df["Om0"],
        nodeParams_df["Ob0"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )
    ax03.plot(
        nodeParams_df["w0"],
        nodeParams_df["wa"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )

    ax10.plot(
        nodeParams_df["Om0"],
        nodeParams_df["h"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )
    ax20.plot(
        nodeParams_df["Om0"],
        nodeParams_df["sigma8"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )
    ax30.plot(
        nodeParams_df["Om0"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )

    ax11.plot(
        nodeParams_df["Ob0"],
        nodeParams_df["h"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )
    ax21.plot(
        nodeParams_df["Ob0"],
        nodeParams_df["sigma8"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )
    ax31.plot(
        nodeParams_df["Ob0"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )

    ax22.plot(
        nodeParams_df["h"],
        nodeParams_df["sigma8"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )
    ax32.plot(
        nodeParams_df["h"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )

    ax33.plot(
        nodeParams_df["sigma8"],
        nodeParams_df["ns"],
        linewidth=0,
        marker='o',
        markersize=7, alpha=0.7,
        color="gray"
    )





ax00.xaxis.set_ticklabels([])
ax10.xaxis.set_ticklabels([])
ax20.xaxis.set_ticklabels([])

ax11.xaxis.set_ticklabels([])
ax21.xaxis.set_ticklabels([])

ax22.xaxis.set_ticklabels([])


ax11.yaxis.set_ticklabels([])
ax21.yaxis.set_ticklabels([])
ax31.yaxis.set_ticklabels([])

ax22.yaxis.set_ticklabels([])
ax32.yaxis.set_ticklabels([])
ax33.yaxis.set_ticklabels([])


ax30.set_xlabel(r'$\displaystyle\Omega_{\mathrm{m0}}$', fontsize=30)
ax32.set_xlabel(r'$h$', fontsize=30)
ax31.set_xlabel(r'$\displaystyle \Omega_{\mathrm{b0}}$', fontsize=30)
ax33.set_xlabel(r'$\displaystyle\sigma_8$', fontsize=30)

ax10.set_ylabel(r'$h$', fontsize=30)
ax00.set_ylabel(r'$\displaystyle \Omega_{\mathrm{b0}}$', fontsize=30)
ax20.set_ylabel(r'$\displaystyle\sigma_8$', fontsize=30)
ax30.set_ylabel(r'$\displaystyle n_s$', fontsize=30)

ax03.set_xlabel(r'$w_0$', fontsize=30)
ax03.set_ylabel(r'$w_a$', fontsize=30)


plt.savefig(
    f'./plots/nodes_ideal_tests.jpg',
    dpi=500,
    bbox_inches="tight",
    pad_inches=0.05,
)

