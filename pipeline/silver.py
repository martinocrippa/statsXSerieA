"""bronze -> silver: tiene solo le colonne utili all'analisi, una stagione per file.

silver e' l'input del notebook. Le date restano stringhe nel formato originale:
le parsa il notebook (il codice di analisi non si tocca).
"""
import pandas as pd

from . import config


def to_silver():
    config.SILVER.mkdir(parents=True, exist_ok=True)
    for src in sorted(config.BRONZE.glob(f"{config.LEAGUE}_*.csv")):
        df = pd.read_csv(src, dtype=str)  # tutto stringa: non tocco i formati
        cols = [c for c in config.ANALYSIS_COLUMNS if c in df.columns]
        out = df[cols].dropna(subset=["HomeTeam", "AwayTeam"])
        dest = config.SILVER / src.name
        out.to_csv(dest, index=False, lineterminator="\n")
        print(f"{src.name}: {len(out)} partite -> silver")


if __name__ == "__main__":
    to_silver()
