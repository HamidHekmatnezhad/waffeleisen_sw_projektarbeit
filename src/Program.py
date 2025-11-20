from anwendungsschicht.WaffelController import WaffelController, Zustand
from steuerungsschicht_regelungsschicht.PIDRegler import PIDRegler
from steuerungsschicht_regelungsschicht.Solltabelle import Solltabelle
from Benutzeroberfläche_userinterface.SimpleGUI import SimpleGUI
from Benutzeroberfläche_userinterface.ButtonInput import ButtonInput
from hardwareAbstraktionsschicht.HeaterActuator import HeaterActuator
from hardwareAbstraktionsschicht.TemperatureSensor import get_sensor_instance
import time # für thread und Timer, aber nicht zu benutzen

# Zeitintervall zwischen zwei Regelzyklen in Millisekunden (100ms = 10 Zyklen/Sekunde)
REGELKREIS_INTERVALL_MS = 100 
controller_instance = None # Globale Variable für den Zugriff durch den Scheduler

def run_scheduler():
    """
    Zeitgesteuerte, wiederkehrende Ausführung des Regelkreises.
    """
    global controller_instance
    
    if controller_instance:
        
        # 1. Führe eine Iteration des Regelkreises aus
        controller_instance.runRegelkreisIteration()
        
        # 2. Überprüfe den Zustand und plane den nächsten Aufruf
        if controller_instance._aktuellerZustand not in (Zustand.FEHLER, Zustand.BEREIT):
            root = controller_instance._gui.holeRoot()
            root.after(REGELKREIS_INTERVALL_MS, run_scheduler)
        else:
             print("*** SYSTEM-INFO: Endzustand erreicht. Zeitplanung gestoppt. ***")
             
def main():
    """
    Hauptfunktion des Programms. Initialisiert alle Komponenten.
    """
    global controller_instance
    print("--- SYSTEM START: Initialisierung der Komponenten ---")
    
    # 1. Singleton 
    sensor = get_sensor_instance() 
    aktor = HeaterActuator()

    # 2. Kern-Logik
    solltabelle = Solltabelle()
    regler = PIDRegler() 
    regler.heater_aktuator = aktor 
    
    # 3. GUI
    gui = SimpleGUI()
    
    # 4. WaffelControllers
    controller = WaffelController(gui=gui, regler=regler, tabelle=solltabelle)
    controller_instance = controller 
    
    # 5. Eingabe 
    input_handler = ButtonInput(controller=controller)

    print("\n--- PROGRAMM BEREIT ---")




    # --- SIMULATION: Benutzerinteraktion ---
    
    print("SIMULATION: Benutzer wählt Grad 5 (durch zwei Klicks).")
    input_handler.simuliereTaste('+') 
    input_handler.simuliereTaste('+') 
    
    # Benutzer startet den Backvorgang
    controller.starteBackvorgang()
    
    # --- START DER HAUPTSCHLEIFE ---
    
    print("\n--- START REGELKREIS-SIMULATION ---")
    
    gui.holeRoot().after(REGELKREIS_INTERVALL_MS, run_scheduler) 
    
    gui.holeRoot().mainloop() 


if __name__ == '__main__':
    main()

# noch nicht getestet.