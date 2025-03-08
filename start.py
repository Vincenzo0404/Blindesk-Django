import os
import subprocess
import time
import webbrowser

# 🔹 IMPOSTA IL PERCORSO DEL TUO PROGETTO (MODIFICA QUESTO!)
PROJECT_DIR = r"C:\Users\vinci\OneDrive\Desktop\Progetti\Blindesk-Django"
FRONTEND_DIR = os.path.join(PROJECT_DIR, "frontend")

# 🔹 Comando per avviare Django in PowerShell
django_command = f'powershell -NoExit -Command "cd {PROJECT_DIR}; env\\Scripts\\Activate;cd backend ;python manage.py runserver"'

# 🔹 Comando per avviare React in PowerShell
react_command = f'powershell -NoExit -Command "cd {FRONTEND_DIR}; npm run dev"'

# 🔹 Avvia Django in una nuova finestra di PowerShell
subprocess.Popen(["powershell", "-NoExit", "-Command", django_command])

# 🔹 Avvia React in una nuova finestra di PowerShell
subprocess.Popen(["powershell", "-NoExit", "-Command", react_command])

# ⏳ Aspetta qualche secondo per far partire il server React
# time.sleep(3)

# 🔹 URL di React (modifica se necessario)
react_url = "http://localhost:5173"

# 🔹 Apri il browser predefinito su localhost di React
webbrowser.open(react_url)

print("✅ Server Django e React avviati con successo!")
print("🌍 Aprendo il browser su:", react_url)
