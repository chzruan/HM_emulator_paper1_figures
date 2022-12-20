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
from cycler import cycler
custom_cycler = (cycler(color=['mediumblue', 'orange', 'green', 'red', 'purple', 'mediumseagreen', 'magenta', 'black']))

import pandas as pd 
from scipy.interpolate import InterpolatedUnivariateSpline as ius


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


k_sim, Pk_gm_sim_mean, Pk_gm_sim_stddev = np.loadtxt(
    f'./data/HM_HOD_Pk_gm_sim.dat',
    unpack=True,
)
p_gm = ax0.errorbar(
    k_sim,
    Pk_gm_sim_mean,
    yerr=Pk_gm_sim_stddev,
    color='k',
    label=r"$P_{\mathrm{gm}}^{\mathrm{simulation}}$",
    lw=0.0,
    elinewidth=1.0,
    markersize=3.5,
    marker='s',
    zorder=100,
)
Pk_gm_func = ius(
    k_sim,
    Pk_gm_sim_mean,
)




k_sim, Pk_cm_sim_mean, Pk_cm_sim_stddev = np.loadtxt(
    f'./data/HM_HOD_Pk_cm_sim.dat',
    unpack=True,
)
p_cm = ax0.errorbar(
    k_sim,
    Pk_cm_sim_mean * n_c / n_g,
    yerr=Pk_cm_sim_stddev * n_c / n_g,
    label=r"$P_{\mathrm{cm}}^{\mathrm{simulation}}$",
    lw=0.0,
    elinewidth=1.0,
    markersize=3,
    marker='o',
    color="red",
)
Pk_cm_func = ius(
    k_sim,
    Pk_cm_sim_mean * n_c / n_g
)



k_sim, Pk_sm_sim_mean, Pk_sm_sim_stddev = np.loadtxt(
    f'./data/HM_HOD_Pk_sm_sim.dat',
    unpack=True,
)
p_sm = ax0.errorbar(
    k_sim,
    Pk_sm_sim_mean * n_s / n_g,
    yerr=Pk_sm_sim_stddev * n_s / n_g,
    label=r"$P_{\mathrm{sm}}^{\mathrm{simulation}}$",
    lw=0.0,
    elinewidth=1.0,
    linestyle="--",
    markersize=3.5,
    marker='X',
    alpha=0.9,
    color="lightseagreen",
)
Pk_sm_func = ius(
    k_sim,
    Pk_sm_sim_mean * n_s / n_g,
)






# kk, Pk_cm_theory, Pk_sm_theory = np.loadtxt(f"./data/Pk_gm_NFW-D19.dat", unpack=True,)
# # rr = rr[::2]
# # Pk_cm_theory = Pk_cm_theory[::2]
# Pk_gm_theory = Pk_cm_theory + Pk_sm_theory
# ax0.plot(
#     kk,
#     kk * Pk_cm_theory,
#     lw=1.5,
#     color=p_cm[0].get_color(),
# )
# ax1.plot(
#     kk,
#     Pk_cm_theory / Pk_cm_func(kk) - 1.0,
#     lw=1.5,
#     color=p_cm[0].get_color(),
#     label=r"$\mathrm{theory}, P_{\mathrm{cm}}$",
# )

# ax0.plot(
#     kk,
#     kk * Pk_sm_theory,
#     lw=1.5,
#     color=p_sm[0].get_color(),
# )
# ax1.plot(
#     kk,
#     Pk_sm_theory / Pk_sm_func(kk) - 1.0,
#     lw=1.5,
#     color=p_sm[0].get_color(),
#     label=r"$\mathrm{theory}, P_{\mathrm{sm}}$",
# )

# ax0.plot(
#     kk,
#     kk * Pk_gm_theory,
#     lw=2,
#     color=p_gm[0].get_color(),
# )
# ax1.plot(
#     kk,
#     Pk_gm_theory / (Pk_cm_func(kk) + Pk_sm_func(kk)) - 1.0,
#     lw=2,
#     color=p_gm[0].get_color(),
#     label=r"$\mathrm{theory}, P_{\mathrm{gm}}$",
# )




ax1.hlines(
    [-0.01, 0.00, 0.01],
    1e-1, 10,
    lw=0.7,
    linestyle="--",
    color="gray",
    alpha=0.5,
)

ax0.xaxis.set_ticklabels([])

# ax0.set_xlim([0.2, 6])
# ax1.set_xlim([0.2, 6])

# ax0.set_ylim([0, 900])
# ax1.set_ylim([-0.015, 0.015])

ax1.set_xlabel(r"$\displaystyle k / (h\,\mathrm{Mpc}^{-1})$", fontsize=16,)
ax0.set_ylabel(r"$\displaystyle k P_{\mathrm{gm}}(k)$", fontsize=18,)
ax1.set_ylabel(r"$\displaystyle \mathrm{rel.\ diff.}$", fontsize=12,)

ax0.legend(frameon=False, fontsize=10, ncol=1,)
ax1.legend(frameon=False, fontsize=9, ncol=2,)

plt.savefig(
    "Pk_gm.pdf",
    bbox_inches="tight",
    pad_inches=0.05,
)
