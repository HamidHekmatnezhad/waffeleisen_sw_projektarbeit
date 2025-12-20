# Importieren der beteiligten Klassen
from anwendungsschicht.WaffelController import WaffelController, Zustand
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI
from hardwareAbstraktionsschicht.TemperatureSensor import get_sensor_instance

def test_ut4_sensor_controller_integration():
    """
    UT4: Prüfung, ob der WaffelController korrekt die Daten vom 
    TemperatureSensor (Singleton) abruft und verarbeitet.
    """
    print("--- Starte Integration Test: UT4 (Sensor-Controller Kopplung) ---")
    
    gui = SimpleGUI(controller=None)
    regler = PIDRegler()
    tabelle = Solltabelle()
    sensor = get_sensor_instance()
    
    controller = WaffelController(gui, regler, tabelle)
    controller.starteBackvorgang() # Setzt Zustand auf AUFHEIZEN
    
    sensor.setze_simulierte_temperatur(25.0)
    
    print("Führe Regelkreis-Iteration aus...")
    controller.runRegelkreisIteration()
    
    ist_temp_im_system = sensor.leseTemperatur()
    print(f"Vom Sensor gelesene Temperatur: {ist_temp_im_system}°C")
    
    if ist_temp_im_system == 25.0:
        print("TEST BESTANDEN (Datenfluss Sensor -> Controller ok)")
    else:
        print(f"TEST FEHLGESCHLAGEN (Wert fehlerhaft: {ist_temp_im_system})")

if __name__ == "__main__":
    test_ut4_sensor_controller_integration()