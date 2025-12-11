import json
import os

# Bestimme den absoluten Pfad zur Config-Datei relativ zu diesem Skript
base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "config", "sprache_config.json")

if os.path.exists(path):
    with open(path, 'r') as file:
        data = json.load(file)
        # print(data)
    print(f"en: {data['EN']['BEREIT']}")
else:
    print(f"FEHLER: Datei nicht gefunden unter: {path}")