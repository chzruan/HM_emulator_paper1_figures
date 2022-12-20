import numpy as np
import sys 
import h5py


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import gridspec
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams.update({'font.size': 14})
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
params = {'xtick.top': True, 'ytick.right': True, 'xtick.direction': 'in', 'ytick.direction': 'in'}
plt.rcParams.update(params)



redshift = 0.000



fig = plt.figure(
    figsize=(6.0, 7.0)
)
gs = gridspec.GridSpec(
    2, 1,
    hspace=0,
    height_ratios=[1.5, 1],
)

ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])

ax0.set_xscale('log')
ax0.set_yscale('log')
ax0.xaxis.set_ticklabels([])
ax1.set_xscale('log')
ax1.set_yscale('log')


with h5py.File(
    f'./data/hmf_ideal_emu.hdf5',
    'r',
) as file_hmf:
    group_dataset = file_hmf['training']
    _err_lst = []
    for slice_id in range(10):
        for ii, node_id in enumerate(range(5)):
            group_1node = group_dataset[f'slice{slice_id}/node{node_id}']
            log10M = group_1node['log10M_bin_centre'][...]         
            if ii == 1 and slice_id == 0:
                pp = ax0.plot(
                    10**log10M,
                    group_1node["cHMF_true"][...],
                    color="gray",
                    linewidth=0,
                    marker='o',
                    markersize=2,
                    label=r'$\mathrm{training, simulation}$',
                    alpha=0.9,
                )
            else:
                pp = ax0.plot(
                    10**log10M,
                    group_1node["cHMF_true"][...],
                    color="gray",
                    linewidth=0,
                    marker='o',
                    markersize=2,
                    alpha=0.2,
                )
                
            if ii == 1 and slice_id == 0:
                ax0.plot(
                    10**log10M,
                    group_1node["cHMF_emu"][...],
                color=pp[0].get_color(),
                    linewidth=1,
                    label=r'$\mathrm{training, emulation}$',
                    alpha=0.9
                )
            else:
                ax0.errorbar(
                    10**log10M,
                    group_1node["cHMF_emu"][...],
                color=pp[0].get_color(),
                    linewidth=0.8,
                    alpha=0.2
                )

            _err_lst.append(np.abs(group_1node["cHMF_emu"][...] / group_1node["cHMF_true"][...] - 1.0))


    err_all = np.array(_err_lst)
    err_mean = np.mean(err_all, axis=0,)
    err_median = np.median(err_all, axis=0,)
    err_2 = np.percentile(err_all, q=90, axis=0,)

    ax1.plot(
        10**log10M,
        err_median,
        lw=2.5,
        color=pp[0].get_color(),
        zorder=98,
        alpha=1,
        label=r'$\mathrm{training, median}$',
    )
    ax1.plot(
        10**log10M,
        err_2,
        lw=1.5,
        linestyle='--',
        color=pp[0].get_color(),
        zorder=98,
        alpha=1,
        label=r'$\mathrm{training, 90\text{-}th\ percentile}$',
    )




    group_dataset = file_hmf['test']
    _err_lst = []
    for slice_id in range(1):
        for ii, node_id in enumerate(range(500)):
            group_1node = group_dataset[f'slice{slice_id}/node{node_id}']
            log10M = group_1node['log10M_bin_centre'][...]         
            if ii == 1 and slice_id == 0:
                pp = ax0.plot(
                    10**log10M,
                    group_1node["cHMF_true"][...],
                    color="lightseagreen",
                    linewidth=0,
                    marker='o',
                    markersize=2,
                    alpha=0.9,
                )
            else:
                pp = ax0.plot(
                    10**log10M,
                    group_1node["cHMF_true"][...],
                    color="lightseagreen",
                    linewidth=0,
                    marker='o',
                    markersize=2,
                    alpha=0.2,
                )
                
            if ii == 1 and slice_id == 0:
                ax0.plot(
                    10**log10M,
                    group_1node["cHMF_emu"][...],
                    color=pp[0].get_color(),
                    linewidth=1,
                    label=r'$\mathrm{test}$',
                    alpha=0.9
                )
            else:
                ax0.errorbar(
                    10**log10M,
                    group_1node["cHMF_emu"][...],
                    color=pp[0].get_color(),
                    linewidth=0.8,
                    alpha=0.2
                )

            _err_lst.append(np.abs(group_1node["cHMF_emu"][...] / group_1node["cHMF_true"][...] - 1.0))


    err_all = np.array(_err_lst)
    err_mean = np.mean(err_all, axis=0,)
    err_median = np.median(err_all, axis=0,)
    err_2 = np.percentile(err_all, q=90, axis=0,)

    ax1.plot(
        10**log10M,
        err_median,
        lw=2.5,
        color=pp[0].get_color(),
        zorder=98,
        alpha=1,
        label=r'$\mathrm{test}$',
    )
    ax1.plot(
        10**log10M,
        err_2,
        lw=1.5,
        linestyle='--',
        color=pp[0].get_color(),
        zorder=98,
        alpha=1,
    )









    group_dataset = file_hmf['test_inner']
    _err_lst = []
    for slice_id in range(1):
        for ii, node_id in enumerate(range(500)):
            group_1node = group_dataset[f'slice{slice_id}/node{node_id}']
            log10M = group_1node['log10M_bin_centre'][...]         
            if ii == 1 and slice_id == 0:
                pp = ax0.plot(
                    10**log10M,
                    group_1node["cHMF_true"][...],
                    color="mediumblue",
                    linewidth=0,
                    marker='o',
                    markersize=2,
                    alpha=0.9,
                )
            else:
                pp = ax0.plot(
                    10**log10M,
                    group_1node["cHMF_true"][...],
                    color="mediumblue",
                    linewidth=0,
                    marker='o',
                    markersize=2,
                    alpha=0.2,
                )
                
            if ii == 1 and slice_id == 0:
                ax0.plot(
                    10**log10M,
                    group_1node["cHMF_emu"][...],
                    color=pp[0].get_color(),
                    linewidth=1,
                    label=r'$\mathrm{test, inner}\,50\%$',
                    alpha=0.9
                )
            else:
                ax0.errorbar(
                    10**log10M,
                    group_1node["cHMF_emu"][...],
                    color=pp[0].get_color(),
                    linewidth=0.8,
                    alpha=0.2
                )

            _err_lst.append(np.abs(group_1node["cHMF_emu"][...] / group_1node["cHMF_true"][...] - 1.0))


    err_all = np.array(_err_lst)
    err_mean = np.mean(err_all, axis=0,)
    err_median = np.median(err_all, axis=0,)
    err_2 = np.percentile(err_all, q=90, axis=0,)

    ax1.plot(
        10**log10M,
        err_median,
        lw=2.5,
        color=pp[0].get_color(),
        zorder=98,
        alpha=1,
        label=r'$\mathrm{test, inner}\,50\%$',
    )
    ax1.plot(
        10**log10M,
        err_2,
        lw=1.5,
        linestyle='--',
        color=pp[0].get_color(),
        zorder=98,
        alpha=1,
    )





    ax1.plot(
        10**log10M,
        np.ones_like(10**log10M) * 1e-3,
        linewidth=0.8,
        linestyle="-.",
        color='r',
    )
    ax1.plot(
        10**log10M,
        np.ones_like(10**log10M) * 1e-2,
        linewidth=0.8,
        linestyle="-.",
        color='r',
    )

    ax0.set_xlim([1e12, 1e16])
    ax1.set_xlim([1e12, 1e16])
    ax1.set_ylim([1e-4, 0.051])

    ax1.set_xlabel(
        r'$\displaystyle  M / (h^{-1}M_{\odot})$',
        fontsize=18
    )
    ax1.set_ylabel(
        r'$\displaystyle |\Delta n_{\mathrm{h}}| / n_{\mathrm{h}}^{\mathrm{true}}$',
        fontsize=20,
    )
    ax0.set_ylabel(
        r"$n_{\mathrm{h}} (>M) / (h^{-1}\mathrm{Mpc})^{-3}$",
        fontsize=22
    )

    ax0.legend(
        fontsize=19,
        frameon=False,
    )
    ax1.legend(
        fontsize=10.5,
        ncol=2,
        frameon=False,
        loc="upper left"
    )

    plt.savefig(
        f'./plots/hmf_ideal_emu.jpg',
        dpi=600,
        bbox_inches="tight",
        pad_inches=0.05,        
    )
