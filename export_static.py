# ============================================================
# Exporta el portafolio Django como sitio estatico en docs/
# (para GitHub Pages). Genera ES (/) y EN (/en/).
# Requiere el runserver corriendo en 8025.
# Uso:  python export_static.py
# ============================================================
import shutil
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent
DOCS = BASE / "docs"
SERVER = "http://localhost:8025"

# 1. HTML renderizado por Django (ambos idiomas)
html_es = urllib.request.urlopen(SERVER + "/", timeout=20).read().decode("utf-8")
html_en = urllib.request.urlopen(SERVER + "/en/", timeout=20).read().decode("utf-8")

# 2. Carpeta docs/ limpia
if DOCS.exists():
    shutil.rmtree(DOCS)
DOCS.mkdir()
(DOCS / ".nojekyll").write_text("")

(DOCS / "index.html").write_text(html_es, encoding="utf-8")
(DOCS / "en").mkdir()
(DOCS / "en" / "index.html").write_text(html_en, encoding="utf-8")

# 3. Copiar archivos estaticos (fuente original, sin hash)
shutil.copytree(BASE / "web" / "static" / "web", DOCS / "static" / "web")

print("OK: sitio estatico ES + EN generado en", DOCS)
