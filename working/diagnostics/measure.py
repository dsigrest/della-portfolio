#!/usr/bin/env python3
"""Read the actual rendered iframe heights vs their inner content heights."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[2]
URL = (ROOT / "case-notifications.html").as_uri()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await ctx.new_page()
        await page.goto(URL, wait_until="networkidle")
        await page.wait_for_timeout(3000)
        rows = await page.evaluate("""
() => {
  const out = [];
  document.querySelectorAll('.diagram-embed iframe').forEach(f => {
    const wrap = f.closest('.diagram-embed');
    const wrapName = wrap ? wrap.getAttribute('data-diagram') : '?';
    const cs = getComputedStyle(f);
    const inner = f.contentDocument;
    const innerDiagram = inner ? inner.querySelector('.diagram') : null;
    out.push({
      d: wrapName,
      iframeStyleHeight: f.style.height,
      iframeOffsetHeight: f.offsetHeight,
      iframeRectHeight: f.getBoundingClientRect().height,
      iframeMaxHeightCSS: cs.maxHeight,
      iframeOverflowCSS: cs.overflow,
      docHTMLscrollH: inner && inner.documentElement ? inner.documentElement.scrollHeight : null,
      docBodyScrollH: inner && inner.body ? inner.body.scrollHeight : null,
      diagramOffsetH: innerDiagram ? innerDiagram.offsetHeight : null,
      diagramScrollH: innerDiagram ? innerDiagram.scrollHeight : null,
      diagramComputedHeight: innerDiagram ? getComputedStyle(innerDiagram).height : null,
      diagramOverflow: innerDiagram ? getComputedStyle(innerDiagram).overflow : null,
    });
  });
  return out;
}
""")
        for r in rows:
            print(r)
        await browser.close()

asyncio.run(main())
