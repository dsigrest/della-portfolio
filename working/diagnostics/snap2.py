#!/usr/bin/env python3
"""Capture screenshots of batch-2 diagrams (rows 17, 19, 22, 24, 27)."""
import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[2]
URL  = (ROOT / "case-notifications.html").as_uri()
OUT  = Path(__file__).resolve().parent / "screenshots-2026-04-28"
TAG  = (sys.argv[1] if len(sys.argv) > 1 else "batch2")

TARGETS = ["not-17", "not-19", "not-22", "not-24", "not-14-v2"]

async def shoot(page, viewport, label):
    await page.set_viewport_size(viewport)
    await page.goto(URL, wait_until="networkidle")
    await page.wait_for_timeout(2500)
    full = OUT / f"{label}-fullpage-{TAG}.png"
    await page.screenshot(path=str(full), full_page=True)
    print(f"  full -> {full.name}")
    for d in TARGETS:
        loc = page.locator(f'.diagram-embed[data-diagram="{d}"]').first
        if await loc.count() == 0:
            print(f"  [skip] {d}"); continue
        await loc.scroll_into_view_if_needed()
        await page.wait_for_timeout(400)
        path = OUT / f"{label}-{d}-{TAG}.png"
        try:
            await loc.screenshot(path=str(path))
            print(f"  {d} -> {path.name}")
        except Exception as e:
            print(f"  [err] {d}: {e}")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context()
        page = await ctx.new_page()
        page.on("console",       lambda msg: print(f"[console:{msg.type}] {msg.text}"))
        page.on("pageerror",     lambda exc: print(f"[pageerror] {exc}"))
        page.on("requestfailed", lambda req: print(f"[404/fail] {req.url} -- {req.failure}"))
        await shoot(page, {"width": 1440, "height": 900}, "desktop-1440")
        await shoot(page, {"width": 375,  "height": 812}, "mobile-375")
        await browser.close()

asyncio.run(main())
