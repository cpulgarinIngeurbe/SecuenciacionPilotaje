from datetime import datetime
import os

os.makedirs("data", exist_ok=True)

with open("data/salida.txt", "w", encoding="utf-8") as f:
    f.write("Python se ejecutó correctamente.\n\n")
    f.write(f"Fecha: {datetime.now()}\n")
    f.write("Próximo paso: generar Pilotaje.xlsx\n")

print("Proceso terminado.")
