#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scarica i loghi (stemmi) delle squadre di Serie A da Wikipedia (it.wikipedia.org)
e li salva come PNG in  ..\\resources\\loghi  (rispetto a questo script in utils\\).

Contesto:
  L'ambiente Cowork che ha generato il set iniziale ha la rete verso Wikipedia/
  Wikimedia bloccata, quindi 27 loghi (Serie A recente) sono gia' stati copiati da
  un repo open-source in resources\\loghi. Le 26 squadre storiche mancanti vanno
  scaricate da qui, dal tuo PC dove la rete e' aperta.

Come funziona:
  - per ogni squadra fa una ricerca su it.wikipedia (generator=search)
  - prende la "page image" (lo stemma in cima all'articolo) come thumbnail PNG
    (cosi' anche i loghi in SVG vengono rasterizzati in PNG dai server Wikimedia)
  - salva <Nome>.png nella cartella di destinazione

Uso (da VS Code o terminale, dentro utils\\):
  python scarica_loghi.py                 # scarica SOLO i mancanti (non sovrascrive)
  python scarica_loghi.py --all           # (ri)scarica TUTTE le 53 (set omogeneo)
  python scarica_loghi.py --force         # sovrascrive anche i file gia' presenti
  python scarica_loghi.py --size 1024     # lato lungo del PNG (default 512)
  python scarica_loghi.py --dest "C:/percorso/loghi"   # cartella di destinazione custom

Requisiti:  pip install requests
"""
import argparse
import os
import sys
import time

try:
    import requests
except ImportError:
    sys.exit("Manca 'requests'. Installa con:  pip install requests")

API = "https://it.wikipedia.org/w/api.php"
# Wikimedia richiede uno User-Agent identificabile
HEADERS = {"User-Agent": "statsXSerieA-logo-fetcher/1.0 (contatto: martino.crippa@vantyx.ai)"}

# Cartella di destinazione di default:  <questo_file>/../resources/loghi
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DEST = os.path.normpath(os.path.join(HERE, "..", "resources", "loghi"))

# Squadra (nome file finale) -> query di ricerca su it.wikipedia
CLUBS = {
    # --- 26 storiche mancanti nel set iniziale ---
    "Ancona":      "Ancona Calcio",
    "Ascoli":      "Ascoli Calcio 1898 FC",
    "Bari":        "SSC Bari società calcistica",
    "Benevento":   "Benevento Calcio",
    "Brescia":     "Brescia Calcio",
    "Carpi":       "Carpi Football Club 1909",
    "Catania":     "Catania Football Club società 2022",
    "Cesena":      "Cesena Football Club società 2022",
    "Chievo":      "Associazione Calcio ChievoVerona",
    "Crotone":     "Football Club Crotone",
    "Foggia":      "Calcio Foggia 1920",
    "Livorno":     "Unione Sportiva Livorno 1915",
    "Messina":     "Atletico Calcio Messina società 2023",
    "Modena":      "Modena Football Club 2018",
    "Novara":      "Novara Football Club",
    "Padova":      "Calcio Padova",
    "Palermo":     "Palermo Football Club",
    "Perugia":     "Associazione Calcistica Perugia Calcio",
    "Pescara":     "Delfino Pescara 1936",
    "Piacenza":    "Piacenza Calcio 1919",
    "Reggiana":    "Associazione Calcistica Reggiana 1919",
    "Reggina":     "Reggina 1914",
    "Siena":       "Società Sportiva Robur Siena",
    "Spal":        "SPAL società calcistica Ferrara",
    "Treviso":     "Treviso Football Club 1993",
    "Vicenza":     "Lanerossi Vicenza Virtus",
    # --- 27 gia' presenti (servono solo con --all) ---
    "Atalanta":    "Atalanta Bergamasca Calcio",
    "Bologna":     "Bologna Football Club 1909",
    "Cagliari":    "Cagliari Calcio",
    "Como":        "Como 1907",
    "Cremonese":   "Unione Sportiva Cremonese",
    "Empoli":      "Empoli Football Club",
    "Fiorentina":  "ACF Fiorentina",
    "Frosinone":   "Frosinone Calcio",
    "Genoa":       "Genoa Cricket and Football Club",
    "Inter":       "Football Club Internazionale Milano",
    "Juventus":    "Juventus Football Club",
    "Lazio":       "Società Sportiva Lazio",
    "Lecce":       "Unione Sportiva Lecce",
    "Milan":       "Associazione Calcio Milan",
    "Monza":       "Associazione Calcio Monza",
    "Napoli":      "Società Sportiva Calcio Napoli",
    "Parma":       "Parma Calcio 1913",
    "Pisa":        "Pisa Sporting Club",
    "Roma":        "Associazione Sportiva Roma",
    "Salernitana": "Unione Sportiva Salernitana 1919",
    "Sampdoria":   "Unione Calcio Sampdoria",
    "Sassuolo":    "Unione Sportiva Sassuolo Calcio",
    "Spezia":      "Spezia Calcio",
    "Torino":      "Torino Football Club",
    "Udinese":     "Udinese Calcio",
    "Venezia":     "Venezia Football Club",
    "Verona":      "Hellas Verona Football Club",
}

# Le 27 da NON toccare di default (gia' presenti dal set iniziale)
ALREADY_PRESENT = {
    "Atalanta", "Bologna", "Cagliari", "Como", "Cremonese", "Empoli", "Fiorentina",
    "Frosinone", "Genoa", "Inter", "Juventus", "Lazio", "Lecce", "Milan", "Monza",
    "Napoli", "Parma", "Pisa", "Roma", "Salernitana", "Sampdoria", "Sassuolo",
    "Spezia", "Torino", "Udinese", "Venezia", "Verona",
}


def _get(params):
    params = {"format": "json", "formatversion": "2", **params}
    r = requests.get(API, params=params, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()


def search_title(query):
    """Restituisce il titolo dell'articolo piu' pertinente alla query."""
    data = _get({"action": "query", "list": "search",
                 "srsearch": query, "srlimit": 1, "srnamespace": 0})
    hits = data.get("query", {}).get("search", [])
    return hits[0]["title"] if hits else None


def pageimage_thumb(title, size):
    """Thumbnail PNG della 'page image' (stemma in infobox), anche se non libera."""
    data = _get({"action": "query", "titles": title, "redirects": 1,
                 "prop": "pageimages", "piprop": "thumbnail",
                 "pithumbsize": size, "pilicense": "any"})
    pages = data.get("query", {}).get("pages", [])
    if pages:
        return pages[0].get("thumbnail", {}).get("source")
    return None

# token che indicano che NON e' lo stemma del club
_BAD = ("pictogram", "soccerball", "soccer_ball", "stadium", "stadio", "mappa",
        "map", "italy", "italia", "flag", "bandiera", "commons-logo", "wikimedia",
        "edit-clear", "crystal", "nuvola", "ambox", "question", "disambig",
        "kit_", "kit body", "kit shorts", "kit socks", "kit_left", "kit_right",
        "scudetto", "coppa", "supercoppa", ".ogg", ".oga", ".mid", ".webm")
_GOOD = ("logo", "stemma", "crest", "badge", "scudo", "emblem")


def crest_from_images(title, size):
    """Fallback: elenca i file della pagina e sceglie quello che sembra lo stemma."""
    data = _get({"action": "query", "titles": title, "redirects": 1,
                 "prop": "images", "imlimit": 100})
    pages = data.get("query", {}).get("pages", [])
    if not pages:
        return None
    files = [im["title"] for im in pages[0].get("images", [])]
    cand = []
    for f in files:
        low = f.lower()
        if not (low.endswith(".png") or low.endswith(".svg") or low.endswith(".jpg")):
            continue
        if any(b in low for b in _BAD):
            continue
        cand.append(f)
    if not cand:
        return None

    # priorita': file con parola-chiave da stemma, poi che contiene un pezzo del titolo
    tokens = [t.lower() for t in title.replace("'", " ").split() if len(t) > 3]

    def score(f):
        low = f.lower()
        s = 0
        if any(g in low for g in _GOOD):
            s += 10
        s += sum(1 for t in tokens if t in low)
        return s

    cand.sort(key=score, reverse=True)
    best = cand[0]

    info = _get({"action": "query", "titles": best, "prop": "imageinfo",
                 "iiprop": "url", "iiurlwidth": size})
    ipages = info.get("query", {}).get("pages", [])
    if ipages and ipages[0].get("imageinfo"):
        ii = ipages[0]["imageinfo"][0]
        return ii.get("thumburl") or ii.get("url")
    return None


def page_image_url(query, size):
    """Risolve (url_immagine_png, titolo_articolo) con catena di fallback."""
    title = search_title(query) or query
    url = pageimage_thumb(title, size)
    if not url:
        url = crest_from_images(title, size)
    return url, title


def download(url, dest):
    r = requests.get(url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    ctype = r.headers.get("Content-Type", "")
    if "image" not in ctype:
        raise ValueError(f"contenuto non immagine ({ctype})")
    with open(dest, "wb") as f:
        f.write(r.content)
    return len(r.content)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true",
                    help="scarica tutte le 53 squadre (set omogeneo da Wikipedia)")
    ap.add_argument("--force", action="store_true",
                    help="sovrascrive i file gia' presenti")
    ap.add_argument("--size", type=int, default=512,
                    help="lato lungo del PNG in px (default 512)")
    ap.add_argument("--dest", default=DEFAULT_DEST,
                    help=f"cartella di destinazione (default: {DEFAULT_DEST})")
    args = ap.parse_args()

    dest_dir = os.path.abspath(args.dest)
    os.makedirs(dest_dir, exist_ok=True)
    print(f"Destinazione: {dest_dir}\n")

    if args.all:
        targets = list(CLUBS.keys())
    else:
        targets = [c for c in CLUBS if c not in ALREADY_PRESENT]

    ok, skip, fail = 0, 0, 0
    failed = []
    for name in sorted(targets):
        dest = os.path.join(dest_dir, f"{name}.png")
        if os.path.exists(dest) and not args.force:
            print(f"[skip ] {name} (gia' presente)")
            skip += 1
            continue
        try:
            url, title = page_image_url(CLUBS[name], args.size)
            if not url:
                raise ValueError("nessuna immagine trovata")
            size = download(url, dest)
            print(f"[ ok  ] {name:12s} <- {title}  ({size // 1024} KB)")
            ok += 1
        except Exception as e:
            print(f"[FAIL ] {name:12s} -> {e}")
            failed.append(name)
            fail += 1
        time.sleep(0.4)  # gentile con i server Wikimedia

    print(f"\nFatto. ok={ok} skip={skip} fail={fail}")
    if failed:
        print("Da controllare a mano:", ", ".join(failed))


if __name__ == "__main__":
    main()
