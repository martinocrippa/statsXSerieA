"""Configurazione condivisa della pipeline: percorsi, stagioni, sorgente dati."""
from pathlib import Path

# Radice del progetto (questo file sta in pipeline/)
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RAW = DATA / "raw"
BRONZE = DATA / "bronze"
SILVER = DATA / "silver"

# football-data.co.uk, Serie A = I1
LEAGUE = "I1"
BASE_URL = "https://www.football-data.co.uk/mmz4281"

# Stagioni: anno di inizio, dal 1993/94 al 2025/26
START_YEARS = range(1993, 2026)

# Le uniche colonne che servono all'analisi
ANALYSIS_COLUMNS = ["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]


def season_code(start_year: int) -> str:
    """1993 -> '9394', 2003 -> '0304', 2024 -> '2425'."""
    return f"{start_year % 100:02d}{(start_year + 1) % 100:02d}"
