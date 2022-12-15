import numpy as np
import sys

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
#ax0.xaxis.set_ticklabels([])
from cycler import cycler
custom_cycler = (cycler(color=['mediumblue', 'mediumblue', 'green', 'red', 'purple', 'mediumseagreen', 'magenta', 'black']))

import h5py



fig = plt.figure(
    figsize=(5.0, 6.0)
)
gs = gridspec.GridSpec(
    2, 1,
    hspace=0,
    height_ratios=[1.5, 1]
)

ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])

ax0.set_xscale('log')
ax0.xaxis.set_ticklabels([])
ax1.set_xscale('log')
ax1.set_yscale('log')


with h5py.File(
    f'./data/conc_idea_emu.hdf5', 
    'r',
) as file_conc:
    datagroup = file_conc['train']

    _err_lst = []
    for slice_index in range(6):
        datagroup_slice = datagroup[f'slice{slice_index}']

        for node in range(10):
            datagroup_slice_node = datagroup_slice[f'node{node}']

            if (node == 0) and (slice_index == 0):
                ax0.plot(
                    10**datagroup_slice_node['log10M_bin_centre'][...],
                    datagroup_slice_node['conc_true'][...],
                    linewidth=1,
                    alpha=0.7,
                    color="gray",
                    label=r"$\displaystyle\mathrm{training, true}$",
                )
            else:
                ax0.plot(
                    10**datagroup_slice_node['log10M_bin_centre'][...],
                    datagroup_slice_node['conc_true'][...],
                    linewidth=1,
                    alpha=0.5,
                    color="gray",
                )


            log10M = datagroup_slice_node['log10M_bin_centre'][...]
            if (node == 0) and (slice_index == 0):
                ax0.plot(
                    10**log10M,
                    datagroup_slice_node['conc_emulation'][...],
                    linewidth=0,
                    marker='o',
                    markersize=2.5,
                    alpha=0.8,
                    color="gray",
                    label=r"$\displaystyle\mathrm{training, emulation}$",
                    markeredgecolor='gray',
                    markerfacecolor='gray',
                )
            else:
                ax0.plot(
                    10**log10M,
                    datagroup_slice_node['conc_emulation'][...],
                    linewidth=0,
                    marker='o',
                    markersize=2.5,
                    alpha=0.3,
                    color="gray",
                    markeredgecolor='gray',
                    markerfacecolor='gray',
                )

            _err_lst.append(np.abs(datagroup_slice_node['conc_emulation'][...] / datagroup_slice_node['conc_true'][...] - 1.0))

    err_all = np.array(_err_lst)
    err_mean = np.mean(err_all, axis=0,)
    err_median = np.median(err_all, axis=0,)
    err_2 = np.percentile(err_all, q=90, axis=0,)

    ax1.plot(
        10**log10M,
        err_median,
        lw=2.5,
        color='k',
        zorder=100,
        alpha=1,
        label=r'$\mathrm{training, median}$',
    )
    ax1.plot(
        10**log10M,
        err_2,
        lw=1.5,
        linestyle='--',
        color='k',
        zorder=100,
        alpha=1,
        label=r'$\mathrm{training, 90\text{-}th\ percentile}$',
    )







    datagroup = file_conc['test']

    _err_lst = []
    for slice_index in range(1):
        datagroup_slice = datagroup[f'slice{slice_index}']

        for node in range(500):
            datagroup_slice_node = datagroup_slice[f'node{node}']

            if (node == 0) and (slice_index == 0):
                ax0.plot(
                    10**datagroup_slice_node['log10M_bin_centre'][...],
                    datagroup_slice_node['conc_true'][...],
                    linewidth=1,
                    alpha=0.7,
                    color="lightseagreen",
                    label=r"$\displaystyle\mathrm{test}$",
                )
            elif (node % 5 == 0):
                ax0.plot(
                    10**datagroup_slice_node['log10M_bin_centre'][...],
                    datagroup_slice_node['conc_true'][...],
                    linewidth=0.7,
                    alpha=0.3,
                    color="lightseagreen",
                )
            else:
                pass


            log10M = datagroup_slice_node['log10M_bin_centre'][...]

            if (node % 5 == 0):
                ax0.plot(
                    10**log10M,
                    datagroup_slice_node['conc_emulation'][...],
                    linewidth=0,
                    marker='s',
                    markersize=2,
                    alpha=0.3,
                    color="lightseagreen",
                    markeredgecolor='lightseagreen',
                    markerfacecolor='lightseagreen',
                )

            _err_lst.append(np.abs(datagroup_slice_node['conc_emulation'][...] / datagroup_slice_node['conc_true'][...] - 1.0))

    err_all = np.array(_err_lst)
    err_mean = np.mean(err_all, axis=0,)
    err_median = np.median(err_all, axis=0,)
    err_2 = np.percentile(err_all, q=90, axis=0,)

    # ax1.errorbar(
    #     10**log10M,
    #     err_median,
    #     yerr=(err_2 - err_median),
    #     marker='s',
    #     markersize=3,
    #     lw=2.0,
    #     capsize=2.5,
    #     color='lightseagreen',
    #     zorder=98,
    #     alpha=0.7,
    #     label=r'$\mathrm{test}$',
    # )
    ax1.plot(
        10**log10M,
        err_median,
        lw=2.5,
        color='lightseagreen',
        zorder=98,
        alpha=1,
        label=r'$\mathrm{test}$',
    )
    ax1.plot(
        10**log10M,
        err_2,
        lw=1.5,
        linestyle='--',
        color='lightseagreen',
        zorder=98,
        alpha=1,
    )








    datagroup = file_conc['test_inner50']


    _err_lst = []
    for slice_index in range(1):
        datagroup_slice = datagroup[f'slice{slice_index}']

        for node in range(500):
            datagroup_slice_node = datagroup_slice[f'node{node}']

            if (node == 0) and (slice_index == 0):
                ax0.plot(
                    10**datagroup_slice_node['log10M_bin_centre'][...],
                    datagroup_slice_node['conc_true'][...],
                    linewidth=1,
                    alpha=0.7,
                    color="mediumblue",
                    label=r"$\displaystyle\mathrm{test, inner}\,50\%$",
                )
            elif (node % 5 == 0):
                ax0.plot(
                    10**datagroup_slice_node['log10M_bin_centre'][...],
                    datagroup_slice_node['conc_true'][...],
                    linewidth=0.7,
                    alpha=0.3,
                    color="mediumblue",
                )
            else:
                pass

            log10M = datagroup_slice_node['log10M_bin_centre'][...]

            if (node % 5 == 0):
                ax0.plot(
                    10**log10M,
                    datagroup_slice_node['conc_emulation'][...],
                    linewidth=0,
                    marker='s',
                    markersize=2,
                    alpha=0.3,
                    color="mediumblue",
                    markeredgecolor='mediumblue',
                    markerfacecolor='mediumblue',
                )

            _err_lst.append(np.abs(datagroup_slice_node['conc_emulation'][...] / datagroup_slice_node['conc_true'][...] - 1.0))

    err_all = np.array(_err_lst)
    err_mean = np.mean(err_all, axis=0,)
    err_median = np.median(err_all, axis=0,)
    err_2 = np.percentile(err_all, q=90, axis=0,)

    # ax1.errorbar(
    #     10**log10M,
    #     err_median,
    #     yerr=(err_2 - err_median),
    #     marker='s',
    #     markersize=3,
    #     lw=2.0,
    #     elinewidth=3.5,
    #     capsize=3.5,
    #     color='mediumblue',
    #     zorder=100,
    #     alpha=0.6,
    #     label=r'$\mathrm{test, inner}\,50\%$',
    # )

    ax1.plot(
        10**log10M,
        err_median,
        lw=2.5,
        color='mediumblue',
        zorder=98,
        alpha=1,
        label=r'$\mathrm{test, inner}\,50\%$',
    )
    ax1.plot(
        10**log10M,
        err_2,
        lw=1.5,
        linestyle='--',
        color='mediumblue',
        zorder=98,
        alpha=1,
    )





    ax1.hlines(
        [1e-2, 1e-3],
        1e12,
        1e16,
        color='r',
        linewidth=0.7,
        linestyle="-.",
    )

    ax0.set_xlim([1e12, 1e16])
    ax1.set_xlim([1e12, 1e16])

    ax0.set_ylim([3.9, 24])
    ax1.set_ylim([7e-4, 0.051])

    ax0.xaxis.set_ticklabels([])
    ax1.set_xlabel(
        r'$\displaystyle M / (h^{-1} M_\odot)$',
        fontsize=16
    )
    ax1.set_ylabel(
        r'$\displaystyle |\Delta c| / c_{\mathrm{true}}$',
        fontsize=18
    )
    ax0.set_ylabel(
        r'$\displaystyle c (M)$',
        fontsize=18
    )

    ax0.legend(
        fontsize=15.5,
        frameon=False,
        loc="upper left"
    )
    ax1.legend(
        fontsize=10.5,
        ncol=2,
        frameon=False,
        loc="upper left"
    )


    figpath = f'./plots/conc_ideal_emulation.jpg'
    plt.savefig(
        figpath,
        dpi=600,
        bbox_inches='tight',
        pad_inches=0.05,
    )



