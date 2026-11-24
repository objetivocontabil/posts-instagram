"""Uso: python3 ferramentas/render.py PASTA_SAIDA arquivo1.html arquivo2.html ...
Gera slide-1.png, slide-2.png... (1080x1350) na PASTA_SAIDA, na ordem dos arquivos."""
import sys, os, asyncio
ALT = int(os.environ.get('ALTURA', 1350))  # use ALTURA=1920 para stories
from playwright.async_api import async_playwright
async def main(saida, arquivos):
    os.makedirs(saida, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for i, f in enumerate(arquivos, 1):
            pg = await b.new_page(viewport={"width": 1080, "height": ALT})
            await pg.goto("file://" + os.path.abspath(f))
            await pg.wait_for_timeout(1200)
            h = await pg.evaluate("document.body.scrollHeight")
            print(f, "altura", h, "(deve ser igual a ALTURA)")
            await pg.screenshot(path=f"{saida}/slide-{i}.png", clip={"x": 0, "y": 0, "width": 1080, "height": ALT})
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2:]))
