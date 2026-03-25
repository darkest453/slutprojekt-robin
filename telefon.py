import json
import os

DATAFIL = "Kontakter.json"

def ladda_kontakter():
    if os.path.exists(DATAFIL):
        with open(DATAFIL, "r", encoding="utf-8") as f:
            return json.load(f)
        
    return{}