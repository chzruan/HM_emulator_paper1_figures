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
custom_cycler = (cycler(color=['lightseagreen', 'orange', 'red', 'darkviolet', 'mediumblue', 'green',  'magenta', 'black']))
from matplotlib.ticker import ScalarFormatter
from matplotlib import ticker



do_linear_regression = True # False if sklearn not installed

fig = plt.figure(figsize=(4.8, 6.0))
gs = gridspec.GridSpec(1, 1,)
ax0 = plt.subplot(gs[0])
ax0.set_prop_cycle(custom_cycler)

with h5py.File(f"./data/conc_Rmin.hdf5", 'r') as cr_file:
    group_1box = cr_file["L200"]
    r_min_all = group_1box["r_min"][...]
    c200_median_all = group_1box["c200_median_all"][...]
    log10M200 = group_1box["log10M200"][...]

    for jj, r_min in enumerate(r_min_all):
        if (r_min < 0.05) or (r_min > 0.15):
            continue
        if jj % 2 != 0:
            continue
        pp = ax0.plot(
            log10M200,
            np.log10(c200_median_all[jj, :]),
            linewidth=1.6,
            linestyle="solid",
            label=r"$\displaystyle r_{\mathrm{min}} = " + f"{r_min:.2f}" + r'R_{\mathrm{200c}}$',
        )

        # linear regression
        if (do_linear_regression):
            from sklearn.linear_model import LinearRegression
            mask = (log10M200 > 12.0)
            lm = log10M200[mask].reshape((-1, 1))
            lc = np.log10(c200_median_all[jj, mask])
            model = LinearRegression()
            model.fit(lm, lc)

            lm = np.linspace(11.5, 14.8, 50).reshape(-1, 1)
            log10c_pred = model.predict(lm)
            power_law_idx = model.coef_[0]
            amp = model.intercept_

            ax0.plot(
                lm,
                log10c_pred,
                linewidth=5.5,
                linestyle="solid",
                color=pp[0].get_color(),
                alpha=0.18,
            )

            props = dict(
                boxstyle='round', 
                facecolor=pp[0].get_color(), 
                edgecolor=pp[0].get_color(),
                linewidth=0, 
                alpha=0.2,
            )
            ax0.text(
                12.0 + jj/40, 
                model.predict(np.array([12.0 + jj/40 + 0.70]).reshape(-1, 1)),
                r"$\displaystyle \mathrm{fit}: c = " + f"{amp:.2f}" + " M^{" + f"{power_law_idx:.3f}" + "}$",
                color='k',
                bbox=props,
                rotation=360-48,
                fontsize=9,
                zorder=100,
            )



    MassResolution = group_1box.attrs["mass_resolution"]
    ax0.vlines(
        np.log10(MassResolution * 800),
        0, 16,
        linestyle="solid",
        linewidth=2,
        color="gray",
        alpha=0.7,
        zorder=1,
    )
    ax0.text(
        np.log10(MassResolution * 800) - 0.30,
        0.55,
        r"$\displaystyle 800 \times m_{\mathrm{particle}}^{L200}$",
    )


    plt.gca().set_prop_cycle(custom_cycler)
    group_1box = cr_file["L500"]
    r_min_all = group_1box["r_min"][...]
    c200_median_all = group_1box["c200_median_all"][...]
    log10M200 = group_1box["log10M200"][...]

    for jj, r_min in enumerate(r_min_all):
        if (r_min < 0.05) or (r_min > 0.15):
            continue
        if jj % 2 != 0:
            continue
        pp = ax0.plot(
            log10M200,
            np.log10(c200_median_all[jj, :]),
            linewidth=1.2,
            linestyle="dashed",
        )

    MassResolution = group_1box.attrs["mass_resolution"]
    ax0.vlines(
        np.log10(MassResolution * 800),
        0, 16,
        linestyle="dashed",
        linewidth=1,
        color="gray",
        alpha=0.7,
    )
    ax0.text(
        np.log10(MassResolution * 800) - 0.30,
        0.55,
        r"$\displaystyle 800 \times m_{\mathrm{particle}}^{L500}$",
    )




    plt.gca().set_prop_cycle(custom_cycler)
    group_1box = cr_file["L1000"]
    r_min_all = group_1box["r_min"][...]
    c200_median_all = group_1box["c200_median_all"][...]
    log10M200 = group_1box["log10M200"][...]

    for jj, r_min in enumerate(r_min_all):
        if (r_min < 0.05) or (r_min > 0.15):
            continue
        if jj % 2 != 0:
            continue
        pp = ax0.plot(
            log10M200,
            np.log10(c200_median_all[jj, :]),
            linewidth=1.1,
            linestyle="solid",
        )

    MassResolution = group_1box.attrs["mass_resolution"]
    ax0.vlines(
        np.log10(MassResolution * 800),
        0, 16,
        linestyle="solid",
        linewidth=1,
        color="gray",
        alpha=0.7,
        zorder=1,
    )
    ax0.text(
        np.log10(MassResolution * 800) - 0.30,
        0.55,
        r"$\displaystyle 800 \times m_{\mathrm{particle}}^{L1000}$",
    )



ax0.set_xlim([11.5, 14.7])
ax0.set_ylim([0.54,  0.9])
ax0.get_yaxis().set_major_formatter(ScalarFormatter())

ax0.set_ylabel(
    r"$\displaystyle \log_{10}c^{\mathrm{median}}_{200c}$",
    fontsize=18,
)
ax0.set_xlabel(
    r"$\displaystyle \log_{10} \big[M_{200c} / (h^{-1} M_{\odot} )\big]$",
    fontsize=16,
)

ax0.legend(
    frameon=True,
    fontsize=13,
    ncol=1,
    edgecolor="white",
)
    

plt.savefig(
    "./plots/conc_Rmin.pdf",
    bbox_inches="tight",
    pad_inches=0.05,
)



















