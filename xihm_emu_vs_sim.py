import numpy as np
import sys
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
custom_cycler = (cycler(color=["lightseagreen", "orange", "red", 'mediumblue', 'purple', 'mediumseagreen', 'magenta',]))


log10nh_all = [-3.50,]

fig = plt.figure(figsize=(5, 6))
gs = gridspec.GridSpec(
    2, 1,
    hspace=0,
    height_ratios=[2, 1],
)
ax0 = plt.subplot(gs[0])
ax0.xaxis.set_ticklabels([])
ax0.set_prop_cycle(custom_cycler)
ax1 = plt.subplot(gs[1])

ax0.set_xscale('log')
ax1.set_xscale('log')

with h5py.File(
    f'./data/xihm_emu_vs_sim_redshift0.00.hdf5',
    'r',
) as file_pack:
    gravity = 'LCDM'
    dataflag = 'training'

    for node_id in range(1, 49+1):
        log10rr = file_pack[f'{gravity}/{dataflag}/node{node_id}']['log10r'][...]
        rr = 10**log10rr
        xihm_sim_all = file_pack[f'{gravity}/{dataflag}/node{node_id}']['xihm_sim'][...]
        xihm_emu_all = file_pack[f'{gravity}/{dataflag}/node{node_id}']['xihm_emu'][...]

        for jj in range(len(log10nh_all)):
            if (jj == 0) and (node_id == 1):
                pp = ax0.plot(
                    rr,
                    rr**2 * xihm_sim_all[jj, :],
                    lw=0,
                    markersize=2,
                    marker='o',
                    color="gray",
                    alpha=0.9,
                    label=r"$\mathrm{training, simulation}$"
                )

                ax0.plot(
                    10**log10rr,
                    rr**2 * xihm_emu_all[jj, :],
                    lw=0.7,
                    color=pp[0].get_color(),
                    alpha=0.9,
                    label=r"$\mathrm{training, emulation}$"
                )
            else:
                pp = ax0.plot(
                    10**log10rr,
                    rr**2 * xihm_sim_all[jj, :],
                    lw=0,
                    markersize=2,
                    marker='o',
                    color="gray",
                    alpha=0.5,
                )

                ax0.plot(
                    10**log10rr,
                    rr**2 * xihm_emu_all[jj, :],
                    lw=0.7,
                    color=pp[0].get_color(),
                    alpha=0.5,
                )

            ax1.plot(
                10**log10rr,
                xihm_emu_all[jj, :] / xihm_sim_all[jj, :] - 1.0,
                lw=0.7,
                color=pp[0].get_color(),
                alpha=0.7,
            )




    gravity = 'LCDM'
    dataflag = 'test'

    for node_id in ['GRx8']:
        log10rr = file_pack[f'{gravity}/{dataflag}/node{node_id}']['log10r'][...]
        rr = 10**log10rr
        xihm_sim_all = file_pack[f'{gravity}/{dataflag}/node{node_id}']['xihm_sim'][...]
        xihm_emu_all = file_pack[f'{gravity}/{dataflag}/node{node_id}']['xihm_emu'][...]

        for jj in range(len(log10nh_all)):
            pp = ax0.plot(
                rr,
                rr**2 * xihm_sim_all[jj, :],
                lw=0,
                markersize=3,
                marker='s',
                zorder=100,
            )
            ax0.plot(
                10**log10rr,
                rr**2 * xihm_emu_all[jj, :],
                lw=1.5,
                color=pp[0].get_color(),
                label=r'$\mathrm{test, ' + node_id[0:2] + '}$',
                zorder=100,
            )
            ax1.plot(
                10**log10rr,
                xihm_emu_all[jj, :] / xihm_sim_all[jj, :] - 1.0,
                lw=1.5,
                color=pp[0].get_color(),
                zorder=100,
            )



    gravity = 'fR'
    dataflag = 'test'

    for node_id in ['F5x8', 'F6x8']:
        xihm_sim_all = file_pack[f'{gravity}/{dataflag}/node{node_id}']['xihm_sim'][...]
        xihm_emu_all = file_pack[f'{gravity}/{dataflag}/node{node_id}']['xihm_emu'][...]

        for jj in range(len(log10nh_all)):
            pp = ax0.plot(
                rr,
                rr**2 * xihm_sim_all[jj, :],
                lw=0,
                markersize=3,
                marker='s',
                zorder=100,
            )
            ax0.plot(
                10**log10rr,
                rr**2 * xihm_emu_all[jj, :],
                lw=1.5,
                color=pp[0].get_color(),
                zorder=100,
            )
            ax1.plot(
                10**log10rr,
                xihm_emu_all[jj, :] / xihm_sim_all[jj, :] - 1.0,
                lw=1.5,
                color=pp[0].get_color(),
                zorder=100,
                label=r'$\mathrm{test, ' + node_id[0:2] + '}$',
            )




    gravity = 'DGP'
    dataflag = 'test'

    for node_id in ['N1x8', 'N5x8']:
        log10rr = file_pack[f'{gravity}/{dataflag}/node{node_id}']['log10rr'][...]
        rr = 10**log10rr
        xihm_sim_all = file_pack[f'{gravity}/{dataflag}/node{node_id}']['xihm_sim'][...]
        xihm_emu_all = file_pack[f'{gravity}/{dataflag}/node{node_id}']['xihm_emu'][...]

        for jj in range(len(log10nh_all)):
            pp = ax0.plot(
                rr,
                rr**2 * xihm_sim_all[jj, :],
                lw=0,
                markersize=3,
                marker='s',
                zorder=100,
            )
            ax0.plot(
                10**log10rr,
                rr**2 * xihm_emu_all[jj, :],
                lw=1.5,
                color=pp[0].get_color(),
                zorder=100,
            )
            ax1.plot(
                10**log10rr,
                xihm_emu_all[jj, :] / xihm_sim_all[jj, :] - 1.0,
                lw=1.5,
                color=pp[0].get_color(),
                zorder=100,
                label=r'$\mathrm{test, ' + node_id[0:2] + '}$',
            )


ax1.set_ylim([-0.024, 0.024])

ax1.set_xlabel(
    r"$\displaystyle r / (h^{-1}\mathrm{Mpc})$",
    fontsize=13,
)
ax0.set_ylabel(
    r"$r^2 \xi_{\mathrm{hm}} (r | n_{\mathrm{h}} = 10^{-3.5})$",
    fontsize=15,
)
ax1.set_ylabel(
    r"$\displaystyle \xi_{\mathrm{hm}}^{\mathrm{emu}} / \xi_{\mathrm{hm}}^{\mathrm{sim}} - 1$",
    fontsize=14,
)

ax0.legend(
    frameon=False, 
    ncol=1, 
    fontsize=12,
)
ax1.legend(
    frameon=False, 
    ncol=2, 
    fontsize=11,
    loc='upper right'
)

plt.savefig(
    "./plots/xihm_emu_vs_sim.jpg",
    dpi=600,
    bbox_inches="tight",
    pad_inches=0.05,
)