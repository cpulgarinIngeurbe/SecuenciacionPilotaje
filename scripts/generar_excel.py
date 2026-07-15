import os
import pandas as pd

# Crear carpeta data si no existe
os.makedirs("data", exist_ok=True)

# Datos de prueba
datos = [
    {
        "Fase": "Excavación",
        "Descripción": "Pilote P01",
        "Responsable": "Equipo A",
        "Duración": 45,
        "Estado": "Ejecutado"
    },
    {
        "Fase": "Hormigonado",
        "Descripción": "Pilote P02",
        "Responsable": "Equipo B",
        "Duración": 60,
        "Estado": "Pendiente"
    }
]

# Crear DataFrame
df = pd.DataFrame(datos)

# Guardar Excel
archivo = "data/Pilotaje.xlsx"

with pd.ExcelWriter(archivo, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Pilotaje")

print(f"Excel generado correctamente: {archivo}")
