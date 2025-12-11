import json
import os

class ConfigLoader:
    """
    Klasse zum Laden von Konfigurationen (Persistence Layer).
    Lädt Texte und Parameter aus einer JSON-Datei.
    """
    
    def __init__(self):
        # Pfad zur Config-Datei (simuliert)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_lang_path = os.path.join(base_dir, "config", "sprache_config.json")
        
        self.default_lang_config = {
            "EN": {
                "STANDBY": "STANDBY (from Config)",
                "BEREIT": "READY (from Config)",
                "AUFHEIZEN": "HEATING (from Config)",
                "FEHLER": "ERROR! (from Config)"
            },
        }
        self.default_lang = "EN"

    def laod_lang(self, lang: str = "EN") -> dict:
        """
        Lädt die Konfiguration. Wenn Datei nicht existiert, werden Defaults genutzt.

        return: 1D dict 
        """

        if not os.path.exists(self.config_lang_path):
            print("--- INFO: Keine Config-Datei gefunden. Nutze Defaults.")
            return self.default_lang_config[self.default_lang]
        
        try:
            with open(self.config_lang_path, 'r') as f:
                data = json.load(f)
                print("--- INFO: Konfiguration erfolgreich geladen.")
                return data[lang]
            
        except Exception as e:
            print(f"--- FEHLER: Konfiguration konnte nicht geladen werden: {e}")
            return self.default_lang_config[self.default_lang]