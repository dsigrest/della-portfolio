#!/usr/bin/env python3
"""
Screenshot orphan diagrams (not-e1 through not-e7) at all 6 breakpoints.
Orphans are not embedded in case-notifications.html, so we render them standalone.
"""

import os
from pathlib import Path
import subprocess
import asyncio
from playwright.async_api import async_playwright

BREAKPOINTS = [1440, 1024, 768, 480, 375, 320]
ORPHAN_IDS = ["not-e1", "not-e2", "not-e3", "not-e4", "not-e5", "not-e6", "not-e7"]

async def screenshot_orphan(diagram_id: str):
    """Screenshot one orphan diagram at all breakpoints."""
    diagram_file = f"img/diagrams/diagram-{diagram_id}-*-v5.html"
    
    # Find the actual file
    matches = list(Path(".").glob(diagram_file))
    if not matches:
        print(f"  WARNING: No v5 file found for {diagram_id}")
        return
    
    diagram_path = str(matches[0].resolve())
    diagram_url = f"file://{diagram_path}"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for width in BREAKPOINTS:
            page = await browser.new_page(viewport={"width": width, "height": 900})
            await page.goto(diagram_url, wait_until="networkidle")
            
            # Create output directory
            out_dir = Path(f"working/mobile-audit/screenshots/{width}/orphans")
            out_dir.mkdir(parents=True, exist_ok=True)
            
            out_file = out_dir / f"{diagram_id}.png"
            await page.screenshot(path=str(out_file), full_page=True)
            print(f"  [{width}] {diagram_id} → working/mobile-audit/screenshots/{width}/orphans/{diagram_id}.png")
            
            await page.close()
        
        await browser.close()

async def main():
    print("=== Orphan diagrams ===")
    for orphan_id in ORPHAN_IDS:
        await screenshot_orphan(orphan_id)
    print("Done. Orphan screenshots in: working/mobile-audit/screenshots/[width]/orphans")

if __name__ == "__main__":
    asyncio.run(main())
