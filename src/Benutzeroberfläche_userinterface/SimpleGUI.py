import tkinter as tk

class SimpleGUI:
    """
    Klasse zur Implementierung des Display-Controllers (UI).
    """
    
    def __init__(self):
        """Initialisiert das GUI-Fenster und alle Elemente."""
        self.aktueller_zustand = "STANDBY"
        self.root = tk.Tk()
        self.zustands_text = tk.StringVar(value=self.aktueller_zustand)
        self._init_fenster()
        
        print("--- INFO: SimpleGUI erstellt")

    def _init_fenster(self):
        """Erstellt alle notwendigen Tkinter-Elemente."""
        self.root.title("Waffeleisen-Display")
        self.root.geometry("350x150")
        
        self.zustands_label = tk.Label(
            self.root, 
            textvariable=self.zustands_text, 
            font=("Arial", 18), 
            bg="#f0f0f0", 
            width=25, 
            height=3
        )
        self.zustands_label.pack(pady=20)
        
        tk.Button(self.root, text="CLOSE", command=self.root.quit).pack()

    def zeigeZustand(self, text: str) -> None:
        """
        Setzt den anzuzeigenden Text auf dem Display.
        """
        self.aktueller_zustand = text
        
        if self.root:
            self.zustands_text.set(self.aktueller_zustand)
        
        print(f"GUI_UPDATE: Anzeige wechselt zu '{self.aktueller_zustand}'")

    def getDisplayState(self) -> str:
        """
        Status von Display zurückgeben.
        """
        return self.aktueller_zustand
    
    def holeRoot(self):
        """Hilf Method"""
        return self.root