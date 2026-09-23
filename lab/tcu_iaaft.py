#!/usr/bin/env python3
"""IAAFT Schreiber-Schmitz 1996 por columna + E3 TUC. No permuta AR1."""
from __future__ import annotations

from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATOS = Path("/home/workdir/artifacts/tcu-8dominios/datos")
if not DATOS.exists():
    DATOS = ROOT / "lab" / "datos"
RES = Path(__file__).resolve().parent / "resultados"


def iaaft(x, n_iter=100, seed=None):
    x = np.asarray(x, dtype=float)
    rng = np.random.default_rng(seed)
    x_sorted = np.sort(x)
    amp = np.abs(np.fft.rfft(x))
    y = rng.permutation(x)
    for _ in range(n_iter):
        Y = np.fft.rfft(y)
        y = np.fft.irfft(amp * np.exp(1j * np.angle(Y)), n=len(x)).real
        y = x_sorted[np.argsort(np.argsort(y))]
    return y


def ar1_series(X, W):
    n, p = X.shape
    out = np.full(n, np.nan)
    for t in range(W, n):
        ev = np.linalg.eigvalsh(np.cov(X[t - W : t].T))
        ev = np.maximum(ev, 1e-12)
        out[t] = ev[-1] / ev.sum()
    return out


def auc_score(y, s):
    y = y.astype(int)
    pos, neg = s[y == 1], s[y == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    gt = np.sum(pos[:, None] > neg[None, :])
    eq = np.sum(pos[:, None] == neg[None, :])
    return float((gt + 0.5 * eq) / (len(pos) * len(neg)))
