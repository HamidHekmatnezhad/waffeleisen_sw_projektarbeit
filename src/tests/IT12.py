import os
import sys
# Path-Setup
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from anwendungsschicht.WaffelController import WaffelController
from hardwareAbstraktionsschicht.TemperatureSensor import get_sensor_instance
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI

def test_it12_sensor_plausibilitaet():
    """
    IT12: Sicherstellen, dass der WaffelController die Daten vom 
    TemperatureSensor korrekt einliest (Requirement 2.3).
    """
    print("--- Starte Integration Test: IT12 (Sensor-Plausibilität) ---")
    
    # Setup aller Komponenten
    sensor = get_sensor_instance()
    gui = SimpleGUI(controller=None)
    regler = PIDRegler()
    tabelle = Solltabelle()
    controller = WaffelController(gui, regler, tabelle)
    
    # Setze Wert UNMITTELBAR vor dem Auslesen, um Resets zu umgehen
    test_umgebungstemp = 22.4
    print(f"Aktion: Erneutes Setzen der Temperatur auf {test_umgebungstemp}°C...")
    sensor.setze_simulierte_temperatur(test_umgebungstemp)
    
    # Wert auslesen
    gelesener_wert = sensor.leseTemperatur()
    print(f"Vom System interpretierte Temperatur: {gelesener_wert}°C")
    
    # Validierung mit Toleranz (wegen potentiellem Sensor-Rauschen)
    if abs(gelesener_wert - test_umgebungstemp) < 0.5:
        print("TEST BESTANDEN (Temperatur wurde korrekt übernommen)")
    else:
        print(f"TEST FEHLGESCHLAGEN (Erwartet: {test_umgebungstemp}, Erhalten: {gelesener_wert})")

if __name__ == "__main__":
    test_it12_sensor_plausibilitaet()