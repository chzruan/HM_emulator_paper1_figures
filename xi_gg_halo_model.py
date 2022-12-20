import numpy as np
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import gridspec
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams.update({'font.size': 10})
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{physics}'
params = {'xtick.top': True, 'ytick.right': True, 'xtick.direction': 'in', 'ytick.direction': 'in'}
plt.rcParams.update(params)

import pandas as pd 


box_size = 500.0

nn = np.loadtxt(f"./data/HM_HOD_ng.txt")
n_g = nn[0]
n_c = nn[1]
n_s = nn[2]




fig = plt.figure(figsize=(4, 5.4))
gs = gridspec.GridSpec(
    2, 1, 
    hspace=0, 
    height_ratios=[2, 1],
)
ax0 = plt.subplot(gs[0])
ax0.set_xscale("log")
ax0.set_yscale("log")

ax1 = plt.subplot(gs[1])
ax1.set_xscale("log")

r_sim, xi_gg_sim_mean, xi_gg_sim_stddev = np.loadtxt(
    f'./data/HM_HOD_xi_gg_sim.dat',
    unpack=True,
)
idx_r2xi_min = np.argmin(r_sim**2 * xi_gg_sim_mean)

p_gg = ax0.errorbar(
    r_sim[:idx_r2xi_min],
    r_sim[:idx_r2xi_min]**2 * xi_gg_sim_mean[:idx_r2xi_min],
    yerr=r_sim[:idx_r2xi_min]**2 * xi_gg_sim_stddev[:idx_r2xi_min],
    color='k',
    label=r"$\xi_{\mathrm{gg}}^{\mathrm{simulation}}$",
    lw=0.0,
    linestyle="--",
    markersize=3.5,
    marker='s',
    zorder=100,
)
ax0.errorbar(
    r_sim[idx_r2xi_min:],
    r_sim[idx_r2xi_min:]**2 * xi_gg_sim_mean[idx_r2xi_min:],
    yerr=r_sim[idx_r2xi_min:]**2 * xi_gg_sim_stddev[idx_r2xi_min:],
    color='k',
    lw=0.0,
    linestyle="--",
    markersize=3.5,
    marker='s',
    zorder=100,
    alpha=0.4,
)

r_sim, xi_cc_sim_mean, xi_cc_sim_stddev = np.loadtxt(
    f'./data/HM_HOD_xi_cc_sim.dat',
    unpack=True,
)
p_cc = ax0.errorbar(
    r_sim[:idx_r2xi_min],
    r_sim[:idx_r2xi_min]**2 * (xi_cc_sim_mean[:idx_r2xi_min] * n_c**2/n_g**2),
    yerr=r_sim[:idx_r2xi_min]**2 * (xi_cc_sim_stddev[:idx_r2xi_min] * n_c**2/n_g**2),
    label=r"$\xi_{\mathrm{cc}}^{\mathrm{simulation}}$",
    lw=0.0,
    linestyle="--",
    markersize=3,
    marker='o',
    color="red",
)
ax0.errorbar(
    r_sim[idx_r2xi_min:],
    r_sim[idx_r2xi_min:]**2 * (xi_cc_sim_mean[idx_r2xi_min:] * n_c**2/n_g**2),
    yerr=r_sim[idx_r2xi_min:]**2 * (xi_cc_sim_stddev[idx_r2xi_min:] * n_c**2/n_g**2),
    lw=0.0,
    linestyle="--",
    markersize=3,
    marker='o',
    color="red",
    alpha=0.4,
)

r_sim, xi_cs_sim_mean, xi_cs_sim_stddev = np.loadtxt(
    f'./data/HM_HOD_xi_cs_sim.dat',
    unpack=True,
)
p_cs = ax0.errorbar(
    r_sim[:idx_r2xi_min],
    r_sim[:idx_r2xi_min]**2 * (xi_cs_sim_mean[:idx_r2xi_min] * n_c*n_s/n_g**2),
    yerr=r_sim[:idx_r2xi_min]**2 * (xi_cs_sim_stddev[:idx_r2xi_min] * n_c*n_s/n_g**2),
    label=r"$\xi_{\mathrm{cs}}^{\mathrm{simulation}}$",
    lw=0.0,
    linestyle="--",
    markersize=3,
    marker='v',
    color="orange",
)
ax0.errorbar(
    r_sim[idx_r2xi_min:],
    r_sim[idx_r2xi_min:]**2 * (xi_cs_sim_mean[idx_r2xi_min:] * n_c*n_s/n_g**2),
    yerr=r_sim[idx_r2xi_min:]**2 * (xi_cs_sim_stddev[idx_r2xi_min:] * n_c*n_s/n_g**2),
    lw=0.0,
    linestyle="--",
    markersize=3,
    marker='v',
    color="orange",
    alpha=0.4,
)


r_sim, xi_ss_sim_mean, xi_ss_sim_stddev = np.loadtxt(
    f'./data/HM_HOD_xi_ss_sim.dat',
    unpack=True,
)
p_ss = ax0.errorbar(
    r_sim[:idx_r2xi_min],
    r_sim[:idx_r2xi_min]**2 * (xi_ss_sim_mean[:idx_r2xi_min] * n_s**2/n_g**2),
    yerr=r_sim[:idx_r2xi_min]**2 * (xi_ss_sim_stddev[:idx_r2xi_min] * n_s**2/n_g**2),
    label=r"$\xi_{\mathrm{ss}}^{\mathrm{simulation}}$",
    lw=0.0,
    linestyle="--",
    markersize=3.5,
    marker='X',
    color="lightseagreen",
)
ax0.errorbar(
    r_sim[idx_r2xi_min:],
    r_sim[idx_r2xi_min:]**2 * (xi_ss_sim_mean[idx_r2xi_min:] * n_s**2/n_g**2),
    yerr=r_sim[idx_r2xi_min:]**2 * (xi_ss_sim_stddev[idx_r2xi_min:] * n_s**2/n_g**2),
    label=r"$\xi_{\mathrm{ss}}^{\mathrm{simulation}}$",
    lw=0.0,
    linestyle="--",
    markersize=3.5,
    marker='X',
    alpha=0.4,
    color="lightseagreen",
)





rr, xi_gg_1h_theory, xi_ss_1h_theory, xi_cs_1h_theory = np.loadtxt(
    f"./data/HM_HOD_xi_1h_theory.dat", 
    unpack=True,
)
ax0.plot(
    rr,
    rr**2 * xi_gg_1h_theory,
    lw=2.0,
    color=p_gg[0].get_color(),
)

mask = (rr < 1.5)
ax1.plot(
    rr[mask],
    xi_gg_1h_theory[mask] / xi_gg_sim_mean[mask] - 1.0,
    lw=2.0,
    color=p_gg[0].get_color(),
    label=r"$\mathrm{theory}, \xi_{\mathrm{gg}}^{\mathrm{1h}}$",
)


ax0.plot(
    rr,
    rr**2 * xi_ss_1h_theory,
    lw=1.5,
    color=p_ss[0].get_color(),
)
ax1.plot(
    rr[mask],
    xi_ss_1h_theory[mask] / (xi_ss_sim_mean[mask] * n_s**2/n_g**2) - 1.0,
    lw=1.5,
    color=p_ss[0].get_color(),
    label=r"$\mathrm{theory}, \xi_{\mathrm{ss}}^{\mathrm{1h}}$",
)


ax0.plot(
    rr,
    rr**2 * xi_cs_1h_theory,
    lw=1.5,
    color=p_cs[0].get_color(),
)
ax1.plot(
    rr[mask],
    xi_cs_1h_theory[mask] / (xi_cs_sim_mean[mask] * n_c*n_s/n_g**2) - 1.0,
    lw=2.0,
    color=p_cs[0].get_color(),
    label=r"$\mathrm{theory}, \xi_{\mathrm{cs}}^{\mathrm{1h}}$",
)



ax0.fill_betweenx(
    [1e-2, 1e3],
    x1=r_sim[idx_r2xi_min] * 0.9, 
    x2=500,
    color='gray',
    alpha=0.3,
)
ax1.fill_betweenx(
    [-1, 1],
    x1=r_sim[idx_r2xi_min] * 0.9, 
    x2=500,
    color='gray',
    alpha=0.3,
)

ax1.hlines(
    [-0.01, 0.00, 0.01],
    1e-1, 10,
    lw=0.7,
    linestyle="--",
    color="gray",
    alpha=0.7,
    zorder=1,
)

ax0.text(
    r_sim[idx_r2xi_min] * 0.9, 
    55,
    r'$\rightarrow\mathrm{2\text{-}halo \ term}$',
    color='k',
    fontsize=15,
    zorder=100,
)
ax0.text(
    0.165, 
    55,
    r'$\mathrm{1\text{-}halo \ term}\leftarrow$',
    color='k',
    fontsize=15,
    zorder=100,
)

ax0.xaxis.set_ticklabels([])

ax0.set_xlim([1e-1, 10])
ax1.set_xlim([1e-1, 10])
ax0.set_ylim([0.9, 400])
ax1.set_ylim([-0.035, 0.035])

ax1.set_xlabel(r"$\displaystyle r / (h^{-1}\mathrm{Mpc})$", fontsize=16,)
ax0.set_ylabel(r"$\displaystyle r^2 \xi_{\mathrm{gg}}(r)$", fontsize=18,)
ax1.set_ylabel(r"$\displaystyle \Delta\xi / \xi^{\mathrm{sim}}$", fontsize=12,)

ax0.legend(frameon=False, fontsize=10, ncol=1, loc="lower left",)
ax1.legend(frameon=False, fontsize=12, ncol=1,)

plt.savefig(
    "./plots/xi_gg_halo_model.pdf",
    bbox_inches="tight",
    pad_inches=0.05,
)