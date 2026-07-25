import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from playwright.async_api import async_playwright

if not Path(".env").exists():
    print("ERROR: .env file not found.")
    print("Run the following command to create it from the template:")
    print()
    print("  cp .env-example .env")
    print()
    print("Then edit .env with your personal data (NIE, nombre, etc.).")
    exit(1)

load_dotenv()

SEDE = os.getenv("SEDE", "17")
TRAMITE_GRUPO = os.getenv("TRAMITE_GRUPO", "4038")
NUMERO_DOCUMENTO = os.getenv("NUMERO_DOCUMENTO")
NOMBRE = os.getenv("NOMBRE")
URL = os.getenv(
    "URL",
    "https://icp.administracionelectronica.gob.es/icpplustieb/citar?p=8&locale=es",
)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL, wait_until="networkidle")

        await page.select_option("#sede", SEDE)
        await page.wait_for_selector('[id="tramiteGrupo[0]"]')
        await page.select_option('[id="tramiteGrupo[0]"]', TRAMITE_GRUPO)
        await page.click("#btnAceptar")
        await page.wait_for_selector("#btnEntrar")
        await page.click("#btnEntrar")
        await page.wait_for_selector("#txtIdCitado")
        await page.click("#rdbTipoDocPas")
        await page.fill("#txtIdCitado", NUMERO_DOCUMENTO)
        await page.fill("#txtDesCitado", NOMBRE)
        await page.click("#btnEnviar")
        print("Done. Browser stays open.")
        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
