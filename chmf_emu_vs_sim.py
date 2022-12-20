import numpy as np
import sys 
import h5py

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



redshift = 0.00 
dlog10M = 0.10
file_hmf = h5py.File(
    f'./data/hmf_dlog10M{dlog10M:.2f}_redshift{redshift:.2f}.hdf5',
    'r',
)


fig = plt.figure(
    figsize=(12.9, 6.5)
)
gs = gridspec.GridSpec(
    2, 3,
    hspace=0,
    height_ratios=[3, 1],
    wspace=0,
)

ax00 = plt.subplot(gs[0, 0])
ax10 = plt.subplot(gs[1, 0])

ax01 = plt.subplot(gs[0, 1])
ax11 = plt.subplot(gs[1, 1])

ax02 = plt.subplot(gs[0, 2])
ax12 = plt.subplot(gs[1, 2])


ax00.set_xscale('log')
ax00.set_yscale('log')
ax00.xaxis.set_ticklabels([])
ax10.set_xscale('log')

ax01.set_xscale('log')
ax01.set_yscale('log')
ax01.xaxis.set_ticklabels([])
ax01.yaxis.set_ticklabels([])
ax11.set_xscale('log')
ax11.yaxis.set_ticklabels([])


ax02.set_xscale('log')
ax02.set_yscale('log')
ax02.xaxis.set_ticklabels([])
ax02.yaxis.set_ticklabels([])
ax12.set_xscale('log')
ax12.yaxis.set_ticklabels([])



gravity = 'LCDM'
# training set
for ii, node_id in enumerate(range(1, 50)):
    group_1node = file_hmf[f'{gravity}/training/node{node_id}']
    
    log10M_bin_leftedge = group_1node['log10M_bin_leftedge'][...]
    log10M_bin_centre   = group_1node['log10M_bin_centre'][...]
    if ii == 0:
        pp = ax00.plot(
            10**log10M_bin_leftedge,
            group_1node['cHMF_sim'][...],
            color="coral",
            linewidth=0,
            marker='o',
            markersize=2,
            label=r'$\mathrm{training, simulation}$',
            alpha=0.9,
        )
    else:
        ax00.plot(
            10**log10M_bin_leftedge,
            group_1node['cHMF_sim'][...],
            color="coral",
            linewidth=0,
            marker='o',
            markersize=2,
            alpha=0.22,
        )


    if ii == 0:
        ax00.plot(
            10**log10M_bin_leftedge,
            group_1node['cHMF_emu'][...],
            color=pp[0].get_color(),
            linewidth=1,
            label=r'$\mathrm{training, emulation}$',
            alpha=0.9
        )
    else:
        ax00.errorbar(
            10**log10M_bin_leftedge,
            group_1node['cHMF_emu'][...],
            color=pp[0].get_color(),
            linewidth=1,
            alpha=0.2,
        )

    ax10.plot(
        10**log10M_bin_leftedge,
        (group_1node['cHMF_emu'][...] / group_1node['cHMF_sim'][...]) - 1.0,
        color=pp[0].get_color(),
        linewidth=1.1,
        alpha=0.55,
        zorder=98,
    )

    print(f"node {node_id} done.")


group_1node = file_hmf[f'{gravity}/test/nodeGRx8']
log10M_bin_leftedge = group_1node['log10M_bin_leftedge'][...]
log10M_bin_centre   = group_1node['log10M_bin_centre'][...]

pp = ax00.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_sim'][...],
    linewidth=2.5,
    markersize=0,
    zorder=101,
    color='red',
    label=r'$\displaystyle\mathrm{test,\ GR}$',
)


ax00.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_emu'][...],
    color=pp[0].get_color(),
    linewidth=0,
    marker='s',
    markersize=3.5,
    zorder=101,
)

ax10.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_emu'][...] / group_1node['cHMF_sim'][...] - 1.0,
    color=pp[0].get_color(),
    linewidth=2.5,
    markersize=0,
    zorder=100,
)

props = dict(
    boxstyle='round', 
    facecolor='r' ,
    edgecolor='r',
    linewidth=0, 
    alpha=0.2,
)
ax00.text(
    2e13, 
    3e-3,
    r"$\displaystyle \Lambda\mathrm{CDM}$",
    color='r',
    bbox=props,
    fontsize=18,
    zorder=100,
)







gravity = 'fR'
# training set
for ii, node_id in enumerate(range(1, 50)):
    group_1node = file_hmf[f'{gravity}/training/node{node_id}']
    
    log10M_bin_leftedge = group_1node['log10M_bin_leftedge'][...]
    log10M_bin_centre   = group_1node['log10M_bin_centre'][...]
    if ii == 0:
        pp = ax01.plot(
            10**log10M_bin_leftedge,
            group_1node['cHMF_sim'][...],
            color="turquoise",
            linewidth=0,
            marker='o',
            markersize=2,
            label=r'$\mathrm{training, simulation}$',
            alpha=0.9,
        )
    else:
        ax01.plot(
            10**log10M_bin_leftedge,
            group_1node['cHMF_sim'][...],
            color="turquoise",
            linewidth=0,
            marker='o',
            markersize=2,
            alpha=0.22,
        )


    if ii == 0:
        ax01.plot(
            10**log10M_bin_leftedge,
            group_1node['cHMF_emu'][...],
            color=pp[0].get_color(),
            linewidth=1,
            label=r'$\mathrm{training, emulation}$',
            alpha=0.9
        )
    else:
        ax01.errorbar(
            10**log10M_bin_leftedge,
            group_1node['cHMF_emu'][...],
            color=pp[0].get_color(),
            linewidth=1,
            alpha=0.2,
        )

    ax11.plot(
        10**log10M_bin_leftedge,
        (group_1node['cHMF_emu'][...] / group_1node['cHMF_sim'][...]) - 1.0,
        color=pp[0].get_color(),
        linewidth=1.1,
        alpha=0.55,
        zorder=98,
    )

    print(f"node {node_id} done.")


group_1node = file_hmf[f'{gravity}/test/nodeF5x8']
log10M_bin_leftedge = group_1node['log10M_bin_leftedge'][...]
log10M_bin_centre   = group_1node['log10M_bin_centre'][...]

pp = ax01.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_sim'][...],
    linewidth=2.5,
    markersize=0,
    zorder=101,
    color='lightseagreen',
    label=r'$\displaystyle\mathrm{test,\ F5}$',
)
ax01.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_emu'][...],
    color=pp[0].get_color(),
    linewidth=0,
    marker='s',
    markersize=3.5,
    zorder=101,
)
ax11.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_emu'][...] / group_1node['cHMF_sim'][...] - 1.0,
    color=pp[0].get_color(),
    linewidth=2.5,
    markersize=0,
    zorder=100,
)


group_1node = file_hmf[f'{gravity}/test/nodeF6x8']
log10M_bin_leftedge = group_1node['log10M_bin_leftedge'][...]
log10M_bin_centre   = group_1node['log10M_bin_centre'][...]

pp = ax01.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_sim'][...],
    linewidth=2.5,
    markersize=0,
    zorder=101,
    color='teal',
    label=r'$\displaystyle\mathrm{test,\ F6}$',
)
ax01.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_emu'][...],
    color=pp[0].get_color(),
    linewidth=0,
    marker='s',
    markersize=3.5,
    zorder=101,
)
ax11.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_emu'][...] / group_1node['cHMF_sim'][...] - 1.0,
    color=pp[0].get_color(),
    linewidth=2.5,
    markersize=0,
    zorder=100,
)

props = dict(
    boxstyle='round', 
    facecolor='lightseagreen' ,
    edgecolor='lightseagreen',
    linewidth=0, 
    alpha=0.2,
)

ax01.text(
    1.2e13, 
    3e-3,
    r"$\displaystyle f(R)\,\mathrm{gravity}$",
    color='lightseagreen',
    bbox=props,
    fontsize=18,
    zorder=100,
)




gravity = 'DGP'
# training set
for ii, node_id in enumerate(range(1, 50)):
    group_1node = file_hmf[f'{gravity}/training/node{node_id}']
    
    log10M_bin_leftedge = group_1node['log10M_bin_leftedge'][...]
    log10M_bin_centre   = group_1node['log10M_bin_centre'][...]
    if ii == 0:
        pp = ax02.plot(
            10**log10M_bin_leftedge,
            group_1node['cHMF_sim'][...],
            color="sandybrown",
            linewidth=0,
            marker='o',
            markersize=2,
            label=r'$\mathrm{training, simulation}$',
            alpha=0.9,
        )
    else:
        ax02.plot(
            10**log10M_bin_leftedge,
            group_1node['cHMF_sim'][...],
            color="sandybrown",
            linewidth=0,
            marker='o',
            markersize=2,
            alpha=0.22,
        )


    if ii == 0:
        ax02.plot(
            10**log10M_bin_leftedge,
            group_1node['cHMF_emu'][...],
            color=pp[0].get_color(),
            linewidth=1,
            label=r'$\mathrm{training, emulation}$',
            alpha=0.9
        )
    else:
        ax02.errorbar(
            10**log10M_bin_leftedge,
            group_1node['cHMF_emu'][...],
            color=pp[0].get_color(),
            linewidth=1,
            alpha=0.2,
        )

    ax12.plot(
        10**log10M_bin_leftedge,
        (group_1node['cHMF_emu'][...] / group_1node['cHMF_sim'][...]) - 1.0,
        color=pp[0].get_color(),
        linewidth=1.1,
        alpha=0.55,
        zorder=98,
    )

    print(f"node {node_id} done.")


group_1node = file_hmf[f'{gravity}/test/nodeN1x8']
log10M_bin_leftedge = group_1node['log10M_bin_leftedge'][...]
log10M_bin_centre   = group_1node['log10M_bin_centre'][...]

pp = ax02.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_sim'][...],
    linewidth=2.5,
    markersize=0,
    zorder=101,
    color='orange',
    label=r'$\displaystyle\mathrm{test,\ N1}$',
)
ax02.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_emu'][...],
    color=pp[0].get_color(),
    linewidth=0,
    marker='s',
    markersize=3.5,
    zorder=101,
)
ax12.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_emu'][...] / group_1node['cHMF_sim'][...] - 1.0,
    color=pp[0].get_color(),
    linewidth=2.5,
    markersize=0,
    zorder=100,
)


group_1node = file_hmf[f'{gravity}/test/nodeN5x8']
log10M_bin_leftedge = group_1node['log10M_bin_leftedge'][...]
log10M_bin_centre   = group_1node['log10M_bin_centre'][...]

pp = ax02.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_sim'][...],
    linewidth=2.5,
    markersize=0,
    zorder=101,
    color='peru',
    label=r'$\displaystyle\mathrm{test,\ N5}$',
)
ax02.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_emu'][...],
    color=pp[0].get_color(),
    linewidth=0,
    marker='s',
    markersize=3.5,
    zorder=101,
)
ax12.plot(
    10**log10M_bin_leftedge,
    group_1node['cHMF_emu'][...] / group_1node['cHMF_sim'][...] - 1.0,
    color=pp[0].get_color(),
    linewidth=2.5,
    markersize=0,
    zorder=100,
)

props = dict(
    boxstyle='round', 
    facecolor='orange' ,
    edgecolor='orange',
    linewidth=0, 
    alpha=0.2,
)

ax02.text(
    2e13, 
    3e-3,
    r"$\displaystyle \mathrm{DGP}$",
    color='orange',
    bbox=props,
    fontsize=18,
    zorder=100,
)




fmt = True
if fmt:
    lm = np.array([11, 15])
    ax10.plot(
        10**lm,
        np.zeros_like(10**lm),
        linewidth=0.8,
        linestyle="--",
        color='white',
        zorder=101,
    )
    ax10.fill_between(
        10**lm,
        0.01 * np.ones_like(10**lm),
        -0.01 * np.ones_like(10**lm),
        color='silver',
        alpha=0.5,
    )
    ax10.fill_between(
        10**lm,
        0.02 * np.ones_like(10**lm),
        -0.02 * np.ones_like(10**lm),
        color='gray',
        alpha=0.15
    )

    ax11.plot(
        10**lm,
        np.zeros_like(10**lm),
        linewidth=0.8,
        linestyle="--",
        color='white',
        zorder=101,
    )
    ax11.fill_between(
        10**lm,
        0.01 * np.ones_like(10**lm),
        -0.01 * np.ones_like(10**lm),
        color='silver',
        alpha=0.5,
    )
    ax11.fill_between(
        10**lm,
        0.02 * np.ones_like(10**lm),
        -0.02 * np.ones_like(10**lm),
        color='gray',
        alpha=0.15
    )

    ax12.plot(
        10**lm,
        np.zeros_like(10**lm),
        linewidth=0.8,
        linestyle="--",
        color='white',
        zorder=101,
    )
    ax12.fill_between(
        10**lm,
        0.01 * np.ones_like(10**lm),
        -0.01 * np.ones_like(10**lm),
        color='silver',
        alpha=0.5,
    )
    ax12.fill_between(
        10**lm,
        0.02 * np.ones_like(10**lm),
        -0.02 * np.ones_like(10**lm),
        color='gray',
        alpha=0.15
    )


    ax00.set_xlim([6e11, 1.2e14])
    ax00.set_ylim([2e-6, 1.5e-2])
    ax10.set_xlim([6e11, 1.2e14])
    ax10.set_ylim([-0.053, 0.053])

    ax01.set_xlim([6e11, 1.2e14])
    ax01.set_ylim([2e-6, 1.5e-2])
    ax11.set_xlim([6e11, 1.2e14])
    ax11.set_ylim([-0.053, 0.053])

    ax02.set_xlim([6e11, 1.2e14])
    ax02.set_ylim([2e-6, 1.5e-2])
    ax12.set_xlim([6e11, 1.2e14])
    ax12.set_ylim([-0.053, 0.053])

    ax10.set_xlabel(
        r'$\displaystyle M_{\mathrm{200c}} / (h^{-1} M_{\odot})$',
        fontsize=18
    )
    ax11.set_xlabel(
        r'$\displaystyle M_{\mathrm{200c}} / (h^{-1} M_{\odot})$',
        fontsize=18
    )
    ax12.set_xlabel(
        r'$\displaystyle M_{\mathrm{200c}} / (h^{-1} M_{\odot})$',
        fontsize=18
    )

    ax10.set_ylabel(
        r'$\displaystyle \mathrm{rel. diff.}$',
        fontsize=18
    )
    ax00.set_ylabel(
        r'$\displaystyle n_{\mathrm{h}}(>M_{\mathrm{200c}}) / (h^{-1}\mathrm{Mpc})^{-3}$',
        fontsize=20,
    )
    ax00.legend(
        fontsize=16,
        frameon=False,
        loc="lower left"
    )
    ax01.legend(
        fontsize=15,
        frameon=False,
        loc="lower left"
    )
    ax02.legend(
        fontsize=15,
        frameon=False,
        loc="lower left"
    )

figpath = f'./plots/chmf_emu_vs_sim.jpg'
plt.savefig(
    figpath,
    dpi=600,
    bbox_inches="tight",
    pad_inches=0.05,
)
print(
    f'save plot to {figpath}'
)
plt.close(fig)

file_hmf.close()