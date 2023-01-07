import numpy as np
import sys
import pandas as pd 
import h5py

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import gridspec
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams.update({'font.size': 12})
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{physics}'
params = {'xtick.top': True, 'ytick.right': True, 'xtick.direction': 'in', 'ytick.direction': 'in'}
plt.rcParams.update(params)
from cycler import cycler
custom_cycler = (cycler(color=["lightseagreen", "orange", "r", 'mediumblue', 'purple', 'mediumseagreen', 'magenta',]))





fig = plt.figure(
    figsize=(4.5, 6)
)
gs = gridspec.GridSpec(2, 1, hspace=0, height_ratios=[1.5, 1])
ax0 = plt.subplot(gs[0])

ax0.xaxis.set_ticklabels([])
ax0.set_prop_cycle(custom_cycler)
ax1 = plt.subplot(gs[1])

with h5py.File(
    f'./data/conc_emu_vs_sim_rmin0.10_z0.00.hdf5',
    'r',
) as file_pack:
    for node_id in range(1, 50):
        if (node_id == 1):
            pp = ax0.plot(
                file_pack['fR']['training'][f'node{node_id}']['log10M200c'][...],
                file_pack['fR']['training'][f'node{node_id}']['conc_sim'][...],
                lw=0,
                markersize=2,
                marker='o',
                color="gray",
                alpha=0.9,
                label=r"$\mathrm{training, simulation}$"
            )

            ax0.plot(
                file_pack['fR']['training'][f'node{node_id}']['log10M200c'][...],
                file_pack['fR']['training'][f'node{node_id}']['conc_emu'][...],
                lw=0.7,
                color=pp[0].get_color(),
                alpha=0.9,
                label=r"$\mathrm{training, emulation}$"
            )
        else:
            pp = ax0.plot(
                file_pack['fR']['training'][f'node{node_id}']['log10M200c'][...],
                file_pack['fR']['training'][f'node{node_id}']['conc_sim'][...],
                lw=0,
                markersize=2,
                marker='o',
                color="gray",
                alpha=0.5,
            )

            ax0.plot(
                file_pack['fR']['training'][f'node{node_id}']['log10M200c'][...],
                file_pack['fR']['training'][f'node{node_id}']['conc_emu'][...],
                lw=0.7,
                color=pp[0].get_color(),
                alpha=0.7,
            )


        ax1.plot(
            file_pack['fR']['training'][f'node{node_id}']['log10M200c'][...],
            file_pack['fR']['training'][f'node{node_id}']['conc_emu'][...]/file_pack['fR']['training'][f'node{node_id}']['conc_sim'][...] - 1.0,
            lw=0.7,
            color=pp[0].get_color(),
            alpha=0.7,
        )




    for kk, model in enumerate(["F5x8", "F6x8",]):
        pp = ax0.plot(
            file_pack['fR']['test'][model]['log10M200c'][...],
            file_pack['fR']['test'][model]['conc_sim'][...],
            lw=0,
            markersize=3,
            marker='s',
            alpha=0.9,
            zorder=100,
        )

        ax0.plot(
            file_pack['fR']['test'][model]['log10M200c'][...],
            file_pack['fR']['test'][model]['conc_emu'][...],
            lw=2,
            color=pp[0].get_color(),
            alpha=0.9,
            zorder=100,
        )
        ax1.plot(
            file_pack['fR']['test'][model]['log10M200c'][...],
            file_pack['fR']['test'][model]['conc_emu'][...]/file_pack['fR']['test'][model]['conc_sim'][...] - 1.0,
            lw=2,
            color=pp[0].get_color(),
            alpha=0.9,
            zorder=100,
            label=r"$\mathrm{test, " + model[:2] + "}$"
        )


    pp = ax0.plot(
        file_pack['LCDM']['test']['GRx8']['log10M200c'][...],
        file_pack['LCDM']['test']['GRx8']['conc_sim'][...],
        lw=0,
        markersize=3,
        marker='s',
        alpha=0.9,
        zorder=100,
    )
    ax0.plot(
        file_pack['LCDM']['test']['GRx8']['log10M200c'][...],
        file_pack['LCDM']['test']['GRx8']['conc_emu'][...],
        lw=2,
        color=pp[0].get_color(),
        alpha=0.9,
        zorder=100,
    )
    ax1.plot(
        file_pack['LCDM']['test']['GRx8']['log10M200c'][...],
        file_pack['LCDM']['test']['GRx8']['conc_emu'][...]/file_pack['LCDM']['test']['GRx8']['conc_sim'][...] - 1.0,
        lw=2,
        color=pp[0].get_color(),
        alpha=0.9,
        zorder=100,
        label=r"$\mathrm{test, GR}$"
    )



    gravity = 'DGP'
    for kk, model in enumerate(["N1x8", "N5x8",]):
        pp = ax0.plot(
            file_pack[gravity]['test'][model]['log10M200c'][...],
            file_pack[gravity]['test'][model]['conc_sim'][...],
            lw=0,
            markersize=3,
            marker='s',
            alpha=0.9,
            zorder=100,
        )

        ax0.plot(
            file_pack[gravity]['test'][model]['log10M200c'][...],
            file_pack[gravity]['test'][model]['conc_emu'][...],
            lw=2,
            color=pp[0].get_color(),
            alpha=0.9,
            zorder=100,
        )
        ax1.plot(
            file_pack[gravity]['test'][model]['log10M200c'][...],
            file_pack[gravity]['test'][model]['conc_emu'][...]/file_pack[gravity]['test'][model]['conc_sim'][...] - 1.0,
            lw=2,
            color=pp[0].get_color(),
            alpha=0.9,
            zorder=100,
            label=r"$\mathrm{test, " + model[:2] + "}$"
        )



ax0.set_xlim([13.0, 14.0])
ax1.set_xlim([13.0, 14.0])

ax1.set_ylim([-0.016, 0.016])

ax1.set_xlabel(
    r"$\displaystyle\log_{10}\big[M_{200\mathrm{c}} / (h^{-1}M_{\odot})\big]$",
    fontsize=13,
)
ax0.set_ylabel(
    r"$\mathrm{concentration}$",
    fontsize=15,
)
ax1.set_ylabel(
    r"$\displaystyle c^{\mathrm{emu}} / c^{\mathrm{sim}} - 1$",
    fontsize=14,
)

ax0.legend(
    frameon=False, 
    ncol=1, 
    fontsize=11,
    loc='lower left',
)
ax1.legend(
    frameon=False, 
    ncol=2, 
    fontsize=11,
    loc='upper left'
)

plt.savefig(
    "./plots/conc_emu_vs_sim.jpg",
    dpi=600,
    bbox_inches="tight",
    pad_inches=0.05,
)