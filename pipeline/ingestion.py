"""Scarica i CSV grezzi della Serie A da football-data.co.uk in data/raw/.

Salva i byte cosi' come arrivano, senza toccarli: questo e' il layer raw.
Salta i file gia' presenti (cosi' le stagioni gia' nel repo restano quelle).
"""
import requests

from . import config


def ingest(overwrite: bool = False):
    config.RAW.mkdir(parents=True, exist_ok=True)
    for year in config.START_YEARS:
        code = config.season_code(year)
        dest = config.RAW / f"{config.LEAGUE}_{code}.csv"
        if dest.exists() and not overwrite:
            print("gia' presente:", dest.name)
            continue
        url = f"{config.BASE_URL}/{code}/{config.LEAGUE}.csv"
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            dest.write_bytes(r.content)
            print("scaricata: ", dest.name)
        except Exception as e:
            print("non scaricata:", code, "-", type(e).__name__)


if __name__ == "__main__":
    ingest()
