import numpy as np
import sys
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import gridspec
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams.update({'font.size': 18})
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{physics}'
params = {'xtick.top': True, 'ytick.right': True, 'xtick.direction': 'in', 'ytick.direction': 'in'}
plt.rcParams.update(params)


valid_set_nodes = [11, 34, 13, 22, 36]

fig = plt.figure(figsize=(9, 12))
gs = gridspec.GridSpec(
    4, 3,
    hspace=0,
    wspace=0,
)

ax00 = plt.subplot(gs[0,0])
ax10 = plt.subplot(gs[1,0])
ax20 = plt.subplot(gs[2,0])
ax11 = plt.subplot(gs[1,1])
ax21 = plt.subplot(gs[2,1])
ax22 = plt.subplot(gs[2,2])
ax30 = plt.subplot(gs[3,0])
ax31 = plt.subplot(gs[3,1])
ax32 = plt.subplot(gs[3,2])

ax_legend = plt.subplot(gs[0, 2])

for nodeID in range(0, 50):
    print(f"node{nodeID} start")

    nodeParams = np.loadtxt(
        './data/BRIDGE_Nodes_Omm-S8-h-H0rc-sigma8-As-B0.dat',
        skiprows=1,
        usecols=(0,1,2,3,4),
        dtype=str
    )
    h       = float(nodeParams[nodeID][2]) # H0/100
    Om0     = float(nodeParams[nodeID][0])
    H0rc    = float(nodeParams[nodeID][3])
    S8      = float(nodeParams[nodeID][1])
    sigma8  = float(nodeParams[nodeID][4])

    nodeParams = np.loadtxt(
        './data/FORGE_Nodes_Omm-S8-h-fR0-sigma8-As-B0.dat',
        skiprows=1,
        usecols=(0,1,2,3,4),
        dtype=str
    )
    fR0     = float(nodeParams[nodeID][3])

    cosmo = {
        'Om0'   : Om0,
        'S8'    : S8,
        'h'     : h,
        'sigma8': sigma8,
        'H0rc'  : H0rc,
        'log10fR0abs': np.log10(np.abs(fR0)),
    }

    if (nodeID == 0):
        ax00.plot(
            cosmo["Om0"],
            cosmo["h"],
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,
        )
        ax10.plot(
            cosmo["Om0"],
            cosmo["S8"],
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,
        )
        ax11.plot(
            cosmo["h"],
            cosmo["S8"],
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)

        ax20.plot(
            cosmo["Om0"],
            -5.0,
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)
        ax20.plot(
            cosmo["Om0"],
            -6.0,
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)

        ax21.plot(
            cosmo["h"],
            -5.0,
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)
        ax21.plot(
            cosmo["h"],
            -6.0,
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)

        ax22.plot(
            cosmo["S8"],
            -5.0,
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)
        ax22.plot(
            cosmo["S8"],
            -6.0,
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)

        ax30.plot(
            cosmo["Om0"],
            np.log10(1.0),
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)
        ax31.plot(
            cosmo["h"],
            np.log10(1.0),
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)
        ax32.plot(
            cosmo["S8"],
            np.log10(1.0),
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)
        ax30.plot(
            cosmo["Om0"],
            np.log10(5.0),
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)
        ax31.plot(
            cosmo["h"],
            np.log10(5.0),
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)
        ax32.plot(
            cosmo["S8"],
            np.log10(5.0),
            marker='*',
            markersize=14,
            linewidth=0,
            color="red",   zorder=100,)
    elif (nodeID in valid_set_nodes):
        ax00.plot(
            cosmo["Om0"],
            cosmo["h"],
            marker="v",
            markersize=8,
            linewidth=0,
            color="darkviolet", 
        )
        ax10.plot(
            cosmo["Om0"],
            cosmo["S8"],
            marker="v",
            markersize=8,
            linewidth=0,
            color="darkviolet", 
        )
        ax11.plot(
            cosmo["h"],
            cosmo["S8"],
            marker="v",
            markersize=8,
            linewidth=0,
            color="darkviolet", 
        )
        
        ax30.plot(
            cosmo["Om0"],
            np.log10(cosmo["H0rc"]),
            marker="v",
            markersize=8,
            linewidth=0,
            color="darkviolet", 
        )
        ax31.plot(
            cosmo["h"],
            np.log10(cosmo["H0rc"]),
            marker="v",
            markersize=8,
            linewidth=0,
            color="darkviolet", 
        )
        ax32.plot(
            cosmo["S8"],
            np.log10(cosmo["H0rc"]),
            marker="v",
            markersize=8,
            linewidth=0,
            color="darkviolet", 
        )

        ax20.plot(
            cosmo["Om0"],
            cosmo["log10fR0abs"],
            marker="v",
            markersize=8,
            linewidth=0,
            color="darkviolet", 
        )
        ax21.plot(
            cosmo["h"],
            cosmo["log10fR0abs"],
            marker="v",
            markersize=8,
            linewidth=0,
            color="darkviolet", 
        )
        ax22.plot(
            cosmo["S8"],
            cosmo["log10fR0abs"],
            marker="v",
            markersize=8,
            linewidth=0,
            color="darkviolet", 
        )
    else:
        ax00.plot(
            cosmo["Om0"],
            cosmo["h"],
            marker='o',
            markersize=3,
            linewidth=0,
            color="k",  alpha=0.5,
        )
        ax10.plot(
            cosmo["Om0"],
            cosmo["S8"],
            marker='o',
            markersize=3,
            linewidth=0,
            color="k",  alpha=0.5,
        )
        ax11.plot(
            cosmo["h"],
            cosmo["S8"],
            marker='o',
            markersize=3,
            linewidth=0,
            color="k",  alpha=0.5,
        )
        
        ax30.plot(
            cosmo["Om0"],
            np.log10(cosmo["H0rc"]),
            marker='o',
            markersize=3,
            linewidth=0,
            color="k",  alpha=0.5,
        )
        ax31.plot(
            cosmo["h"],
            np.log10(cosmo["H0rc"]),
            marker='o',
            markersize=3,
            linewidth=0,
            color="k",  alpha=0.5,
        )
        ax32.plot(
            cosmo["S8"],
            np.log10(cosmo["H0rc"]),
            marker='o',
            markersize=3,
            linewidth=0,
            color="k",  alpha=0.5,
        )


        ax20.plot(
            cosmo["Om0"],
            cosmo["log10fR0abs"],
            marker='o',
            markersize=3,
            linewidth=0,
            color="k",  alpha=0.5,
        )
        ax21.plot(
            cosmo["h"],
            cosmo["log10fR0abs"],
            marker='o',
            markersize=3,
            linewidth=0,
            color="k",  alpha=0.5,
        )
        ax22.plot(
            cosmo["S8"],
            cosmo["log10fR0abs"],
            marker='o',
            markersize=3,
            linewidth=0,
            color="k",  alpha=0.5,
        )

    print(f"node{nodeID} done")



ax_legend.set_xlim([-0.2, 1.5])
ax_legend.set_ylim([-0.2, 1.5])
ax_legend.xaxis.set_ticklabels([])
ax_legend.yaxis.set_ticklabels([])
ax_legend.axis("off")

ax_legend.plot(
    0, 1.06, 
    marker='o',
    markersize=3,
    linewidth=0,
    color="k",  alpha=0.5,
)
ax_legend.text(
    0.2, 1, 
    r"$\displaystyle \mathrm{training}$",
    fontsize=26,
)

ax_legend.plot(
    0, 0.76, 
    marker="v",
    markersize=8,
    linewidth=0,
    color="darkviolet", 
)
ax_legend.text(
    0.2, 0.7, 
    r"$\displaystyle \mathrm{validation}$",
    fontsize=26,
)

ax_legend.plot(
    0, 0.46, 
    marker='*',
    markersize=14,
    linewidth=0,
    color="red",
)
ax_legend.text(
    0.2, 0.4, 
    r"$\displaystyle \mathrm{test}$",
    fontsize=26,
)




ax00.xaxis.set_ticklabels([])
ax10.xaxis.set_ticklabels([])
ax11.xaxis.set_ticklabels([])

ax11.yaxis.set_ticklabels([])
ax21.yaxis.set_ticklabels([])
ax22.yaxis.set_ticklabels([])

ax31.yaxis.set_ticklabels([])
ax32.yaxis.set_ticklabels([])


ax00.set_ylabel(r"$\displaystyle h$", fontsize=24)
ax10.set_ylabel(r"$\displaystyle S_8$", fontsize=24)

ax20.set_ylabel(r"$\displaystyle \log_{10} |\bar{f}_{R0}|$", fontsize=22.5)

ax30.set_ylabel(r"$\displaystyle \log_{10} (H_0 r_{\mathrm{c}})$", fontsize=22.5)

ax30.set_xlabel(r"$\displaystyle \Omega_{\mathrm{m0}}$", fontsize=24)
ax31.set_xlabel(r"$\displaystyle h$", fontsize=24)
ax32.set_xlabel(r"$\displaystyle S_8$", fontsize=24)



plt.savefig(
    "./plots/params_FORGE_BRIDGE.jpg",
    dpi=600,
    bbox_inches="tight",
    pad_inches=0.05,
)

