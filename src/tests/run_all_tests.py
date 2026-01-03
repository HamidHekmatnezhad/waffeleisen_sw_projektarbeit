import subprocess
import datetime

sprint1_tests = ["UT1.py", "UT2.py", "UT3.py", "IT4.py", "IT5.py", "IT6.py"]
sprint2_tests = ["UT7.py", "UT8.py", "IT11.py"]
sprint3_tests = ["UT9.py", "IT10.py", "IT12.py", "UT13.py", "IT14.py"]

all_tests = sprint1_tests + sprint2_tests + sprint3_tests

def run_tests():
    log_filename = "./tests/Testprotokoll_Gesamt_Sprint3.txt"
    
    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write(f"===========================================\n")
        log_file.write(f"GEBÜNDELTES TESTPROTOKOLL - WAFFELEISEN\n")
        log_file.write(f"Datum: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n")
        log_file.write(f"Status: Regressionstest-Lauf (Sprint 1-3)\n")
        log_file.write(f"===========================================\n\n")

        success_count = 0
        
        for test_file in all_tests:
            log_file.write(f"Running {test_file}... ")
            print(f"Executing {test_file}...")
            
            try:
                result = subprocess.run(["python3", f"src/tests/{test_file}"], 
                                       capture_output=True, text=True, timeout=5)
                
                if "TEST BESTANDEN" in result.stdout:
                    log_file.write("BESTANDEN\n")
                    success_count += 1
                    print("TEST BESTANDEN")
                    print(f"Details: {result.stdout}")
                else:
                    log_file.write("FEHLGESCHLAGEN\n")
                    log_file.write(f"Details: {result.stdout}\n")
                    print("TEST FEHLGESCHLAGEN")
                    print(f"Details: {result.stdout}")
            
            except Exception as e:
                log_file.write(f"FEHLER: {str(e)}\n")
                print(f"FEHLER: {str(e)}\n")

        log_file.write(f"\n===========================================\n")
        log_file.write(f"ZUSAMMENFASSUNG:\n")
        log_file.write(f"Gesamtanzahl Tests: {len(all_tests)}\n")
        log_file.write(f"Erfolgreich: {success_count}\n")
        log_file.write(f"Fehlgeschlagen: {len(all_tests) - success_count}\n")
        log_file.write(f"===========================================\n")

    print(f"Testlauf abgeschlossen. Protokoll erstellt: {log_filename}")

if __name__ == "__main__":
    run_tests()