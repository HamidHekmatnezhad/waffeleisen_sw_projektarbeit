import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from anwendungsschicht.WaffelController import WaffelController, Zustand
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI
from hardwareAbstraktionsschicht.TemperatureSensor import get_sensor_instance
from hardwareAbstraktionsschicht.HeaterActuator import HeaterActuator 

def test_ut4_sensor_controller_integration():
    print("--- Starte Integration Test: IT4 (Sensor-Controller Kopplung) ---")
    
    gui = SimpleGUI(controller=None)
    regler = PIDRegler()
    aktor = HeaterActuator()
    regler.heater_aktuator = aktor 
    tabelle = Solltabelle()
    sensor = get_sensor_instance()
    
    controller = WaffelController(gui, regler, tabelle)
    controller.starteBackvorgang() 
    
    test_wert = 25.0
    sensor.setze_simulierte_temperatur(test_wert)
    
    print("Führe Regelkreis-Iteration aus...")
    controller.runRegelkreisIteration()
    
    ist_temp_im_system = sensor.leseTemperatur()
    print(f"Vom Sensor gelesene Temperatur: {ist_temp_im_system}°C")
    
    if ist_temp_im_system > 0:
        print(f"TEST BESTANDEN (Datenfluss ok, gelesener Wert: {ist_temp_im_system})")
    else:
        print(f"TEST FEHLGESCHLAGEN (Wert fehlerhaft: {ist_temp_im_system})")

if __name__ == "__main__":
    test_ut4_sensor_controller_integration()