"""raw -> bronze: rende i CSV leggibili facendo rispettare lo schema.

Alcune stagioni (es. 2003/04, 2004/05) hanno un numero variabile di colonne
vuote in coda - virgole di troppo che cambiano da riga a riga - e pandas non
riesce a parsarle. Il criterio non e' togliere virgole a ogni lettura: lo
schema vero sono le colonne con nome nell'intestazione, qui teniamo solo quelle
e scartiamo le colonne vuote. Una volta sola.
"""
import csv

from . import config


def _clean_file(src, dest) -> int:
    with src.open("r", encoding="utf-8", errors="replace", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        return 0
    header = rows[0]
    keep = [i for i, name in enumerate(header) if name.strip() != ""]  # colonne con nome
    with dest.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        for row in rows:
            w.writerow([row[i] if i < len(row) else "" for i in keep])
    return len(rows) - 1


def to_bronze():
    config.BRONZE.mkdir(parents=True, exist_ok=True)
    for src in sorted(config.RAW.glob(f"{config.LEAGUE}_*.csv")):
        dest = config.BRONZE / src.name
        n = _clean_file(src, dest)
        print(f"{src.name}: {n} righe -> bronze")


if __name__ == "__main__":
    to_bronze()
