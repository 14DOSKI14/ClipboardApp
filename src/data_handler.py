# =============================================================================
# DATA_HANDLER.PY - Lagring og lasting av clipboard-historikk
# =============================================================================
# HVA: Håndterer JSON-fil for lagring av kopiert innhold
# HVORFOR: Bevarer historikken mellom økter
# HVORDAN: Bruker json.load() og json.dump()
#
# OPPGAVEKRAV:
#   - Lese data fra fil (load_data)
#   - Skrive data til fil (save_data)
#   - Egendefinerte funksjoner
# =============================================================================

import json
import os
from datetime import datetime

# Konstant for filnavn
DATA_FILE = "clipboard_history.json"


def load_data():
    """
    Leser lagret data fra JSON-fil.

    Returns:
        dict: Historikk-data eller tom struktur hvis fil ikke finnes
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"history": []}


def save_data(data):
    """
    Skriver data til JSON-fil.

    Args:
        data: Dictionary med historikk
    """
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_clip(data, text, category):
    """
    Legger til ny kopiering i historikken.

    Args:
        data: Eksisterende data
        text: Kopiert tekst
        category: "command", "code" eller "text"

    Returns:
        Oppdatert data
    """
    # Unngå duplikater - sjekk om siste er samme
    if data["history"] and data["history"][0]["text"] == text:
        return data

    # Lag nytt klipp-objekt
    clip = {
        "text": text,
        "category": category,
        "time": datetime.now().strftime("%H:%M:%S")
    }

    # Legg til først i listen (nyeste øverst)
    data["history"].insert(0, clip)

    # Begrens til 200 elementer
    if len(data["history"]) > 200:
        data["history"] = data["history"][:200]

    # Lagre til fil
    save_data(data)

    return data


def get_category(data, category):
    """
    Henter alle klipp i en bestemt kategori.

    Args:
        data: Historikk-data
        category: "command", "code" eller "text"

    Returns:
        Liste med klipp i kategorien
    """
    return [h for h in data["history"] if h["category"] == category]


def clear_data():
    """
    Sletter all historikk.

    Returns:
        Tom data-struktur
    """
    save_data({"history": []})
    return {"history": []}