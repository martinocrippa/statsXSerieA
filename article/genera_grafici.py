"""Rigenera i grafici di docs/ a partire da data/silver/.

Stessa logica del notebook (classifica vettorializzata), stile e palette
condivisi. Uso:

    python docs/genera_grafici.py

Dipendenze: pandas, numpy, matplotlib, seaborn, statsmodels (vedi requirements.txt).
I grafici sono materiale di presentazione per README e articoli; l'analisi vera
e i test stanno nel notebook.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import seaborn as sns
from statsmodels.stats.proportion import proportion_confint

ROOT = Path(__file__).resolve().parent.parent
SILVER = ROOT / "data" / "silver"
OUT = ROOT / "article"

BLU, GRI, VIO, VER = "#2F6DB5", "#C9CCD1", "#8E6BA8", "#3A8A6E"
ROSSO = "#c0392b"
sns.set_theme(style="whitegrid")
RNG = np.random.default_rng(42)

# colori sociali e sigle per il grafico temporale; se in resources/loghi/<team>.png
# c'è lo stemma viene usato al posto della pastiglia colorata (drop-in, nessuna
# altra modifica).
LOGHI = ROOT / "resources" / "loghi"
TEAM_COLORS = {
    "Juventus": "#1c1c1c", "Inter": "#0a4595", "Milan": "#fb090b",
    "Napoli": "#12a0d7", "Roma": "#8e1f2f", "Lazio": "#5b9bd5",
    "Fiorentina": "#592c82",
}
TEAM_ABBR = {
    "Juventus": "JUV", "Inter": "INT", "Milan": "MIL", "Napoli": "NAP",
    "Roma": "ROM", "Lazio": "LAZ", "Fiorentina": "FIO",
}


# --- ricostruzione classifiche (come nel notebook) -------------------------

def prepara(df):
    m = df[["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]].copy()
    m["Date"] = pd.to_datetime(m["Date"], format="mixed", dayfirst=True)
    m["FTHG"] = pd.to_numeric(m["FTHG"], errors="coerce")
    m["FTAG"] = pd.to_numeric(m["FTAG"], errors="coerce")
    return m.dropna().sort_values("Date").reset_index(drop=True)


def classifica(p):
    casa = p[["HomeTeam", "FTHG", "FTAG"]].rename(columns={"HomeTeam": "team", "FTHG": "gf", "FTAG": "ga"})
    via = p[["AwayTeam", "FTAG", "FTHG"]].rename(columns={"AwayTeam": "team", "FTAG": "gf", "FTHG": "ga"})
    lungo = pd.concat([casa, via], ignore_index=True)
    lungo["pts"] = (lungo["gf"] > lungo["ga"]) * 3 + (lungo["gf"] == lungo["ga"]) * 1
    tab = lungo.groupby("team").agg(GP=("pts", "size"), GF=("gf", "sum"), GA=("ga", "sum"), Pts=("pts", "sum"))
    tab["GD"] = tab["GF"] - tab["GA"]
    return tab.sort_values(["Pts", "GD", "GF"], ascending=False)


def istantanee(df):
    m = prepara(df)
    n = pd.concat([m["HomeTeam"], m["AwayTeam"]]).nunique()
    app = pd.concat([pd.DataFrame({"team": m["HomeTeam"].values, "g": m.index}),
                     pd.DataFrame({"team": m["AwayTeam"].values, "g": m.index})]).sort_values("g")
    app["giocate"] = app.groupby("team").cumcount() + 1
    fine = app.loc[app["giocate"] == n - 1, "g"].max()
    return classifica(m[m.index <= fine]), classifica(m), n


def anno(stem):
    yy = int(stem.split("_")[1][:2])
    return 1900 + yy if yy >= 90 else 2000 + yy


def carica():
    righe = []
    for f in sorted(SILVER.glob("I1_*.csv")):
        inv, fin, n = istantanee(pd.read_csv(f))
        wc, fc = inv.index[0], fin.index[0]
        gp = inv["GP"].iloc[0]
        righe.append({
            "anno": anno(f.stem), "n": n, "winter": wc, "final": fc, "same": wc == fc,
            "pti_inverno": inv["Pts"].iloc[0],
            "pti_campione": fin["Pts"].iloc[0],
            "pti_campione_inverno": inv.loc[fc, "Pts"],
            "distacco": inv["Pts"].iloc[0] - inv["Pts"].iloc[1],
            "gap_4": inv["Pts"].iloc[0] - inv["Pts"].iloc[3],
            "pack_2_5": inv["Pts"].iloc[1] - inv["Pts"].iloc[4],
            "entro_10": int((inv["Pts"].to_numpy() >= inv["Pts"].iloc[0] - 10).sum()),
            "diff_reti": inv["GD"].iloc[0], "forza": inv["Pts"].iloc[0] / gp,
            "attacco": inv["GF"].iloc[0] / gp, "difesa": -inv["GA"].iloc[0] / gp,
        })
    d = pd.DataFrame(righe).sort_values("anno").reset_index(drop=True)
    d["delta"] = d["pti_campione"] - d["pti_campione_inverno"]
    return d


# --- i sei grafici ----------------------------------------------------------

def g_risultati(d):
    per_team = d.groupby("winter").agg(tot=("same", "size"), won=("same", "sum"))
    per_team = per_team.sort_values("tot", ascending=True)
    k, tot = int(d["same"].sum()), len(d)
    p_si = d["same"].mean() * 100
    p_no = (tot - k) / (d["n"].sum() - tot) * 100

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))
    y = np.arange(len(per_team))
    ax1.barh(y, per_team["won"], color=BLU, label="poi campione")
    ax1.barh(y, per_team["tot"] - per_team["won"], left=per_team["won"], color=GRI, label="non campione")
    for i, (_, r) in enumerate(per_team.iterrows()):
        ax1.text(r["tot"] + 0.2, i, f"{int(r['won'])}/{int(r['tot'])}", va="center", fontsize=9, color="#444")
    ax1.set_yticks(y)
    ax1.set_yticklabels(per_team.index)
    ax1.set_xlim(0, per_team["tot"].max() + 2)
    ax1.set_title("Campione d'inverno -> scudetto, per squadra", fontsize=12, weight="bold")
    ax1.legend(loc="lower right", frameon=False, fontsize=9)

    ax2.bar(["campione\nd'inverno", "non camp.\nd'inverno"], [p_si, p_no], color=[BLU, GRI], width=0.6)
    for x, v in enumerate([p_si, p_no]):
        ax2.text(x, v + 2, f"{v:.1f}%", ha="center", fontsize=11, weight="bold")
    ax2.set_ylim(0, 100)
    ax2.set_ylabel("% che vince lo scudetto")
    ax2.set_title("Vincere lo scudetto: con o senza primato", fontsize=12, weight="bold")

    fig.suptitle(f"Serie A 1993/94-2025/26: il campione d'inverno vince il {p_si:.0f}% delle volte ({k}/{tot})",
                 fontsize=13)
    sns.despine(fig)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT / "risultati.png", dpi=150)
    plt.close(fig)


def g_distribuzioni(d):
    serie = [("Punti del campione d'inverno", d["pti_inverno"], BLU),
             ("Punti del campione d'Italia", d["pti_campione"], VIO),
             ("Punti aggiunti dopo l'inverno", d["delta"], VER)]
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.4))
    for ax, (titolo, dati, col) in zip(axes, serie):
        lo = int(np.floor(dati.min() / 5) * 5)
        hi = int(np.ceil(dati.max() / 5) * 5)
        bins = list(range(lo, hi + 5, 5))
        counts, edges = np.histogram(dati, bins=bins)
        probs = counts / counts.sum()
        centri = [(a + b) / 2 for a, b in zip(edges[:-1], edges[1:])]
        ax.bar(centri, probs, width=4.6, color=col, alpha=0.8, edgecolor="white")
        for p, c in zip(probs, centri):
            if p > 0:
                ax.text(c, p + 0.012, f"{p * 100:.0f}%", ha="center", fontsize=8, color="#555")
        ax.axvline(dati.mean(), color="black", ls="--", lw=1.3, label=f"media {dati.mean():.0f}")
        ax.axvline(dati.median(), color=ROSSO, ls=":", lw=1.7, label=f"mediana {dati.median():.0f}")
        ax.set_title(titolo, fontsize=12, weight="bold")
        ax.set_xlabel("punti (intervalli da 5)")
        ax.set_ylabel("quota di stagioni")
        ax.set_xticks(bins)
        ax.yaxis.set_major_formatter(PercentFormatter(1.0))
        ax.set_ylim(0, probs.max() * 1.3)
        ax.legend(frameon=False, fontsize=9)
    fig.suptitle("Distribuzione dei punti (33 stagioni): quota di stagioni per intervallo di 5 punti",
                 fontsize=13)
    sns.despine(fig)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT / "distribuzioni.png", dpi=150)
    plt.close(fig)


def g_modello(d):
    fasce = pd.cut(d["distacco"], [-1, 2, 5, np.inf], labels=["<=2 punti", "3-5 punti", ">=6 punti"])
    agg = d.groupby(fasce, observed=True)["same"].agg(["mean", "size"])
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(agg.index.astype(str), agg["mean"] * 100, color=BLU, width=0.6)
    for x, (_, r) in enumerate(agg.iterrows()):
        ax.text(x, r["mean"] * 100 + 1.5, f"{r['mean'] * 100:.0f}%\n(n={int(r['size'])})", ha="center", fontsize=10)
    ax.set_ylim(0, 108)
    ax.set_ylabel("% poi campione d'Italia")
    ax.set_xlabel("distacco sul secondo a fine andata")
    ax.set_title("Piu' netto e' il vantaggio, piu' si vince", fontsize=13, weight="bold")
    sns.despine(fig)
    fig.tight_layout()
    fig.savefig(OUT / "modello.png", dpi=150)
    plt.close(fig)


def g_era(d):
    d = d.assign(era=d["n"].map({18: "18 squadre (<=2003/04)", 20: "20 squadre (2004/05+)"}))
    tab = d.groupby("era")["same"].agg(["sum", "size", "mean"])
    fig, ax = plt.subplots(figsize=(8, 4.6))
    x = np.arange(len(tab))
    ax.bar(x, tab["mean"] * 100, color=BLU, width=0.55)
    for i, (_, r) in enumerate(tab.iterrows()):
        ax.text(i, r["mean"] * 100 + 1.5, f"{r['mean'] * 100:.0f}%\n({int(r['sum'])}/{int(r['size'])})",
                ha="center", fontsize=10)
    ax.axhline(d["same"].mean() * 100, color=VIO, ls="--", lw=1.3, label=f"media complessiva {d['same'].mean() * 100:.0f}%")
    ax.set_xticks(x)
    ax.set_xticklabels(tab.index)
    ax.set_ylim(0, 100)
    ax.set_ylabel("% poi campione d'Italia")
    ax.set_title("Il primato d'inverno conta di piu' nell'era moderna", fontsize=13, weight="bold")
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    sns.despine(fig)
    fig.tight_layout()
    fig.savefig(OUT / "era.png", dpi=150)
    plt.close(fig)


def g_cumulata(d):
    k = d["same"].cumsum()
    n = np.arange(1, len(d) + 1)
    lo, hi = proportion_confint(k, n, method="wilson")
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.fill_between(d["anno"], lo * 100, hi * 100, color=BLU, alpha=0.15, label="intervallo di Wilson 95%")
    ax.plot(d["anno"], k / n * 100, color=BLU, lw=2.2, marker="o", ms=3.5, label="stima cumulata")
    cum = (k / n * 100).values
    annos = d["anno"].values
    rev = np.isin(annos, [2004, 2005])  # scudetti poi revocati alla Juventus
    ax.scatter(annos[rev], cum[rev], s=120, facecolors="none", edgecolors="#d4a017",
               linewidths=2.4, zorder=6, label="stagioni poi revocate alla Juventus")
    ax.axhline(d["same"].mean() * 100, color=VIO, ls="--", lw=1.3, label=f"valore finale {d['same'].mean() * 100:.0f}%")
    eventi = [
        (2004, 9, "dal 2004/05:\n20 squadre"),
        (2006, 30, "2006:\nCalciopoli"),
    ]
    for x, y, etichetta in eventi:
        ax.axvline(x, color="#9aa0a6", ls="--", lw=1.4)
        ax.text(x + 0.3, y, etichetta, color="#555", fontsize=9, va="bottom")
    ax.set_xlabel("stagione (anno d'inizio)")
    ax.set_ylabel("P(scudetto | campione d'inverno)  %")
    ax.set_ylim(0, 100)
    ax.set_title("La stima si assesta col tempo (e dipende dall'era)", loc="left", fontsize=13, weight="bold")
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    sns.despine(fig)
    fig.tight_layout()
    fig.savefig(OUT / "cumulata.png", dpi=150)
    plt.close(fig)


def _marker(ax, x, y, team, zoom=0.16):
    path = LOGHI / f"{team}.png"
    if path.exists():
        from matplotlib.offsetbox import OffsetImage, AnnotationBbox
        im = OffsetImage(plt.imread(path), zoom=zoom)
        ax.add_artist(AnnotationBbox(im, (x, y), frameon=False, zorder=4))
    else:
        col = TEAM_COLORS.get(team, GRI)
        ax.scatter([x], [y], s=300, color=col, zorder=3, edgecolor="white", linewidth=1.2)
        ax.text(x, y, TEAM_ABBR.get(team, team[:3].upper()), ha="center", va="center",
                color="white", fontsize=6.5, weight="bold", zorder=4)


def g_timeline(d):
    revocati = {2004, 2005}  # scudetti poi revocati alla Juventus (Calciopoli)
    fig, ax = plt.subplots(figsize=(16, 4.2))
    for _, r in d.iterrows():
        x = r["anno"]
        if r["anno"] in revocati:                 # scudetto poi revocato: tratteggio oro
            stile = dict(color="#d4a017", ls=(0, (5, 3)), lw=2.4)
        elif r["same"]:                           # vince il campione d'inverno: linea piena grossa
            stile = dict(color="#5b6168", ls="-", lw=3.4)
        else:                                     # vince un'altra (rimonta): puntini rossi
            stile = dict(color=ROSSO, ls=(0, (1, 2)), lw=2.6)
        ax.plot([x, x], [0, 1], zorder=1, solid_capstyle="round", **stile)
        _marker(ax, x, 1, r["winter"])
        _marker(ax, x, 0, r["final"])
    from matplotlib.lines import Line2D
    handles = [
        Line2D([0], [0], color="#5b6168", lw=3.4, label="vince il campione d'inverno"),
        Line2D([0], [0], color=ROSSO, lw=2.6, ls=(0, (1, 2)), label="vince un'altra (rimonta)"),
        Line2D([0], [0], color="#d4a017", lw=2.4, ls=(0, (5, 3)),
               label="scudetto poi revocato alla Juventus"),
    ]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.42),
              ncol=3, frameon=False, fontsize=9)
    annos = d["anno"].tolist()
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["campione\nd'Italia", "campione\nd'inverno"], fontsize=10)
    ax.set_ylim(-0.5, 1.5)
    ax.set_xticks(annos[::2])
    ax.set_xticklabels([f"{a % 100:02d}/{(a + 1) % 100:02d}" for a in annos[::2]],
                       rotation=45, fontsize=8)
    ax.set_xlabel("stagione")
    ax.set_title("Campione d'inverno e campione d'Italia, stagione per stagione",
                 loc="left", fontsize=13, weight="bold")
    ax.grid(False)
    sns.despine(fig, left=True)
    fig.tight_layout()
    fig.savefig(OUT / "timeline.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


def _forma_per_era():
    rows = []
    for f in sorted(SILVER.glob("I1_*.csv")):
        inv, _, n = istantanee(pd.read_csv(f))
        pts = inv["Pts"].to_numpy()
        p1 = pts[0]
        rows.append({"n": n, "gap_2": p1 - pts[1], "gap_4": p1 - pts[3],
                     "pack_2_5": pts[1] - pts[4], "entro_10": int((pts >= p1 - 10).sum())})
    f = pd.DataFrame(rows)
    f["era"] = f["n"].map({18: "18 squadre", 20: "20 squadre"})
    return f.groupby("era").median(numeric_only=True)


def g_forma(d):
    med = _forma_per_era()
    eras = ["18 squadre", "20 squadre"]
    colE = {"18 squadre": "#C0504D", "20 squadre": BLU}
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.6),
                                   gridspec_kw={"width_ratios": [3, 1]})
    misure = [("gap_2", "distacco\nsulla 2ª"), ("gap_4", "distacco\nsulla 4ª"),
              ("pack_2_5", "gruppo\n2ª-5ª")]
    x = np.arange(len(misure))
    w = 0.38
    for i, e in enumerate(eras):
        vals = [med.loc[e, k] for k, _ in misure]
        ax1.bar(x + (i - 0.5) * w, vals, w, color=colE[e], label=f"era a {e}")
        for xi, v in zip(x + (i - 0.5) * w, vals):
            ax1.text(xi, v + 0.2, f"{v:.1f}".replace(".", ","), ha="center", fontsize=9)
    ax1.set_xticks(x)
    ax1.set_xticklabels([t for _, t in misure])
    ax1.set_ylabel("punti (mediana)")
    ax1.set_ylim(0, max(med[["gap_2", "gap_4", "pack_2_5"]].max()) * 1.2)
    ax1.set_title("Distacchi e compattezza al giro di boa", fontsize=12, weight="bold")
    ax1.legend(frameon=False, fontsize=9)
    for i, e in enumerate(eras):
        v = med.loc[e, "entro_10"]
        ax2.bar(i, v, 0.6, color=colE[e])
        ax2.text(i, v + 0.1, f"{v:.0f}", ha="center", fontsize=9)
    ax2.set_xticks([0, 1])
    ax2.set_xticklabels(["18 sq.", "20 sq."])
    ax2.set_ylabel("squadre (mediana)")
    ax2.set_ylim(0, med["entro_10"].max() * 1.3)
    ax2.set_title("Squadre entro 10 punti", fontsize=12, weight="bold")
    fig.suptitle("La forma della classifica: il distacco sulla 2ª non cambia, "
                 "l'isolamento dal gruppo sì", fontsize=13)
    sns.despine(fig)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT / "forma.png", dpi=150)
    plt.close(fig)


def g_regressori(d):
    regs = ["gap_4", "distacco", "pack_2_5", "entro_10", "diff_reti", "forza", "attacco", "difesa"]
    etich = {"gap_4": "distacco sul 4º (dal gruppo)", "distacco": "distacco sul 2º",
             "pack_2_5": "compattezza inseguitori (2ª-5ª)", "entro_10": "squadre entro 10 punti",
             "diff_reti": "differenza reti", "forza": "forza (punti/gara)",
             "attacco": "attacco (gol fatti/gara)", "difesa": "difesa (gol subiti/gara)"}
    res = []
    for r in regs:
        x1, x0 = d.loc[d["same"], r].values, d.loc[~d["same"], r].values
        sd = d[r].std(ddof=1)
        dm = (x1.mean() - x0.mean()) / sd
        boot = [(x1[RNG.integers(0, len(x1), len(x1))].mean() -
                 x0[RNG.integers(0, len(x0), len(x0))].mean()) / sd for _ in range(2000)]
        lo, hi = np.percentile(boot, [2.5, 97.5])
        res.append({"reg": r, "d": dm, "lo": lo, "hi": hi})
    rd = pd.DataFrame(res).iloc[::-1].reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.axvline(0, color="#9aa0a6", lw=1)
    for i, row in rd.iterrows():
        col = BLU if (row["lo"] > 0 or row["hi"] < 0) else GRI
        ax.plot([row["lo"], row["hi"]], [i, i], color=col, lw=2.6, solid_capstyle="round")
        ax.plot(row["d"], i, "o", color=col, ms=8)
    ax.set_yticks(range(len(rd)))
    ax.set_yticklabels([etich[r] for r in rd["reg"]])
    ax.set_ylim(-0.6, len(rd) - 0.4)
    ax.set_xlabel("differenza standardizzata fra chi converte e chi si fa rimontare\n"
                  "(0 = nessuna differenza; in blu gli effetti distinguibili da zero)")
    ax.set_title("Cosa distingue chi converte (e cosa no)", loc="left", fontsize=13, weight="bold")
    sns.despine(fig)
    fig.tight_layout()
    fig.savefig(OUT / "regressori.png", dpi=150)
    plt.close(fig)


def main():
    d = carica()
    g_risultati(d)
    g_distribuzioni(d)
    g_modello(d)
    g_era(d)
    g_cumulata(d)
    g_timeline(d)
    g_forma(d)
    g_regressori(d)
    print(f"Rigenerati 8 grafici in {OUT} ({len(d)} stagioni).")


if __name__ == "__main__":
    main()
