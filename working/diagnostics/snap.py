#!/usr/bin/env python3
"""Capture targeted screenshots of case-notifications.html embeds.

Usage:
    python3 snap.py [tag]

Saves PNGs into screenshots-2026-04-28/. Tag argument lets us label
"before" vs "after" runs.
"""
import asyncio, os, sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[2]
URL = (ROOT / "case-notifications.html").as_uri()
OUT = Path(__file__).resolve().parent / "screenshots-2026-04-28"
OUT.mkdir(exist_ok=True)
TAG = (sys.argv[1] if len(sys.argv) > 1 else "before")

# Each diagram-embed has a data-diagram attr; we'll snap the bounding box.
# Plus the section header (h3) just above so we have context.
TARGETS = [
    "not-02b",         # row 2 disconnected surfaces
    "not-02b-swipe",   # row 7 swipe actions
    "not-04b",         # row 9 unread color
    "not-10",          # row 10 three inboxes
    "not-13",          # row 13 taxonomy detail
    # also existing on-disk diagrams for context
    "not-03",          # row 1 summary
    "not-02",          # row 6 inbox row unit
]

async def shoot(page, viewport, label):
    await page.set_viewport_size(viewport)
    await page.goto(URL, wait_until="networkidle")
    # give iframe content + auto-resize JS time to settle
    await page.wait_for_timeout(2500)
    full = OUT / f"{label}-fullpage-{TAG}.png"
    await page.screenshot(path=str(full), full_page=True)
    print(f"  full page -> {full.name}")
    for d in TARGETS:
        sel = f'.diagram-embed[data-diagram="{d}"]'
        loc = page.locator(sel).first
        if await loc.count() == 0:
            print(f"  [skip] no embed {d} on page at {label}")
            continue
        # scroll into view
        await loc.scroll_into_view_if_needed()
        await page.wait_for_timeout(400)
        path = OUT / f"{label}-{d}-{TAG}.png"
        # screenshot the embed plus a little vertical context
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
        page.on("console", lambda msg: print(f"[console:{msg.type}] {msg.text}"))
        page.on("pageerror", lambda exc: print(f"[pageerror] {exc}"))
        page.on("requestfailed", lambda req: print(f"[404/fail] {req.url} -- {req.failure}"))
        await shoot(page, {"width": 1440, "height": 900}, "desktop-1440")
        await shoot(page, {"width": 375, "height": 812},  "mobile-375")
        await browser.close()

asyncio.run(main())
