import importlib
import os
import pkgutil

# Ottiene il nome del package corrente (models)
package = __name__

# Ottiene il percorso assoluto della cartella models
models_path = os.path.join(os.path.dirname(__file__), "models")

# Scansiona tutti i moduli nella cartella models
for _, module_name, _ in pkgutil.iter_modules([models_path]):
    module_full_name = f"{package}.models.{module_name}"
    print(f"Importing {module_full_name}")  # Aggiungi questa riga per il debug
    importlib.import_module(module_full_name)
