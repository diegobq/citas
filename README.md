# citas

Automatización para reservar cita de NIE en la administración pública española.

## Prerrequisitos

- Python 3.10+
- Playwright (se encarga de instalar Chromium automáticamente)

## Instalación

```bash
# 1. Clonar el repositorio
git clone <repo-url> && cd citas

# 2. Crear y activar entorno virtual
#    Mac / Linux:
python3 -m venv .venv && source .venv/bin/activate
#    Windows (PowerShell):
# python -m venv .venv && .venv\Scripts\Activate.ps1
#    Windows (cmd):
# python -m venv .venv && .venv\Scripts\activate.bat

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar los navegadores de Playwright
playwright install chromium

# 5. Configurar variables de entorno
cp .env-example .env
# Editar .env con tus datos (NIE, nombre, etc.)
```

## Uso

```bash
python main.py
```
