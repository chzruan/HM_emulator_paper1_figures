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
import matplotlib.cm as cm
rainbow_colors = cm.winter(np.linspace(0, 1, 49))

from hmf import cosmo
import hmf 
from scipy.interpolate import InterpolatedUnivariateSpline as ius



fig = plt.figure(figsize=(5, 3.6))
gs = gridspec.GridSpec(1, 1,)
ax0 = plt.subplot(gs[0])
ax0.set_xscale("log")

with h5py.File(f"./data/HMF_fR_z0.00.hdf5", 'r') as hmf_file:
    for node_id in range(1, 50):
        group_1node = hmf_file[f"node{node_id}"]

        # Tinker et. al. (2008) HMF
        sigma8 = group_1node.attrs["S8"] * np.sqrt(0.3 / group_1node.attrs["Om0"])
        my_cosmo = cosmo.Cosmology(cosmo_params={
            'flat': True,
            'Om0': group_1node.attrs["Om0"],
            'Ob0': 0.049199,
            'H0': group_1node.attrs['h'] * 100.0,
            'sigma8': sigma8,
            'ns': 0.9652,
        })
        mf = hmf.MassFunction(
            z = 0.000,
            sigma_8=sigma8,
            hmf_model="Tinker08",
            Mmin=11.0,
            Mmax=16.0,
        )
        dHMF_analy = mf.dndlog10m
        NumDenInBins = dHMF_analy * mf.dlog10m
        cHMF_analy = np.cumsum(NumDenInBins[::-1])[::-1]
        log10cHMF_analy_func = ius(
            np.log10(mf.m) - mf.dlog10m/2.0, 
            np.log10(cHMF_analy),
        )

        cHMF_ratio = group_1node["cHMF"][...] / 10**log10cHMF_analy_func(group_1node["log10M_bin_leftedge"][...])

        ax0.plot(
            10.0**group_1node["log10M_bin_leftedge"][...],
            cHMF_ratio,
            lw=1.0,
            color=rainbow_colors[node_id-1],
        )

ax0.set_xlabel(
    r"$\displaystyle M_{\mathrm{200c}} / (h^{-1}M_{\odot})$",
    fontsize=15,
)
ax0.set_ylabel(
    r"$\displaystyle n_{\mathrm{h}}^{\mathrm{sim}} (>M|\boldsymbol{\mathcal{C}}) / n_{\mathrm{h}}^{\mathrm{T08}} (>M|\boldsymbol{\mathcal{C}})$",
    fontsize=15,
)

plt.savefig(
    "./plots/HMF_ratio_fR_z0.00.jpg",
    dpi=600,
    bbox_inches="tight",
    pad_inches=0.05,
)
