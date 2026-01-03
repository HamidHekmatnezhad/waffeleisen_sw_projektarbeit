import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datenhaltungsschicht.ConfigLoader import ConfigLoader

def test_ut7_config_loading():
    """
    UT7: Verifikation, dass der ConfigLoader die Sprachdateien 
    korrekt lädt und ein valides Dictionary zurückgibt.
    """
    print("--- Starte Unit Test: UT7 (ConfigLoader / Mehrsprachigkeit) ---")
    
    loader = ConfigLoader()
    
    print("Aktion: lade_lang('DE') wird aufgerufen...")
    config = loader.laod_lang("DE")
    
    pflicht_schluessel = ["BEREIT", "AUFHEIZEN", "FEHLER"]
    
    if isinstance(config, dict):
        print("Ergebnis ist ein gültiges Dictionary.")
        
        alle_vorhanden = all(key in config for key in pflicht_schluessel)
        
        if alle_vorhanden:
            print(f"Gefundene Werte: {config}")
            print("Ergebnis: TEST BESTANDEN")
        else:
            print("TEST FEHLGESCHLAGEN (Fehlende Schlüssel in der Datei)")
    else:
        print("TEST FEHLGESCHLAGEN (Rückgabewert ist kein Dictionary)")

if __name__ == "__main__":
    test_ut7_config_loading()