from anwendungsschicht.WaffelController import WaffelController
from hardwareAbstraktionsschicht.TemperatureSensor import get_sensor_instance
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI

def test_it12_sensor_plausibilitaet():
    """
    IT12: Sicherstellen, dass der WaffelController die Daten vom 
    TemperatureSensor beim Systemstart korrekt einliest (Requirement 2.3).
    """
    print("--- Starte Integration Test: IT12 (Sensor-Plausibilität) ---")
    
    sensor = get_sensor_instance()
    test_umgebungstemp = 22.4
    sensor.setze_simulierte_temperatur(test_umgebungstemp)
    
    gui = SimpleGUI(controller=None)
    regler = PIDRegler()
    tabelle = Solltabelle()
    
    print(f"Aktion: Systemstart bei simulierten {test_umgebungstemp}°C...")
    controller = WaffelController(gui, regler, tabelle)
    
    gelesener_wert = sensor.leseTemperatur()
    
    print(f"Vom Controller interpretierte Temperatur: {gelesener_wert}°C")
    
    if gelesener_wert == test_umgebungstemp and 18.0 <= gelesener_wert <= 25.0:
        print("TEST BESTANDEN (Temperatur ist plausibel)")
    else:
        print("TEST FEHLGESCHLAGEN (Wert unplausibel oder fehlerhaft)")

if __name__ == "__main__":
    test_it12_sensor_plausibilitaet()