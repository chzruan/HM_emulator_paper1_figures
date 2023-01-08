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





fig = plt.figure(figsize=(5, 5))
gs = gridspec.GridSpec(
    2, 1,
    hspace=0,
    height_ratios=[2, 1],
)
ax0 = plt.subplot(gs[0])
ax0.set_xscale("log")

ax1 = plt.subplot(gs[1])
ax1.set_xscale("log")

r_bins, xi_1h_fid, xi_ss_1h_fid, xi_cs_1h_fid = np.loadtxt(
    f"./data/xi_1h_gg_NFW-D19.dat",
    unpack=True,
    max_rows=30,
)
ax0.plot(
    r_bins,
    r_bins**2 * xi_1h_fid,
    lw=1.5,
    color='k',
    label=r'$\mathrm{fiducial}$',
)

r_bins, xi_1h, xi_ss_1h, xi_cs_1h = np.loadtxt(
    f"./data/xi_1h_gg_NFW-D19_cx0.9.dat",
    unpack=True,
    max_rows=30,
)
pp = ax0.plot(
    r_bins,
    r_bins**2 * xi_1h,
    lw=1.0,
    label=r'$0.9\, c(M)$',
)
ax1.plot(
    r_bins,
    xi_1h / xi_1h_fid - 1.0,
    lw=1.0,
    color=pp[0].get_color(),
)

r_bins, xi_1h, xi_ss_1h, xi_cs_1h = np.loadtxt(
    f"./data/xi_1h_gg_NFW-D19_cx1.1.dat",
    unpack=True,
    max_rows=30,
)
pp = ax0.plot(
    r_bins,
    r_bins**2 * xi_1h,
    lw=1.0,
    label=r'$1.1\, c(M)$',
)
ax1.plot(
    r_bins,
    xi_1h / xi_1h_fid - 1.0,
    lw=1.0,
    color=pp[0].get_color(),
)

ax1.hlines(
    [0.0],
    r_bins.min(),
    r_bins.max(),
    color='gray',
    lw=0.8,
    linestyle='--',
)

ax1.set_xlabel(
    r'$r / (h^{-1}\mathrm{Mpc})$',
    fontsize=15,
)
ax0.set_ylabel(
    r'$r^2 \xi_{\mathrm{gg}}^{\mathrm{1h}} (r), \mathrm{halo\ model}$',
    fontsize=15,
)
ax1.set_ylabel(
    r'$\xi / \xi_{\mathrm{fid}}$',
    fontsize=14,
)

ax0.legend(frameon=False, fontsize=15)

plt.savefig(
    "./plots/xi_gg_theory_varconc.pdf",
    bbox_inches="tight",
    pad_inches=0.05,
)

