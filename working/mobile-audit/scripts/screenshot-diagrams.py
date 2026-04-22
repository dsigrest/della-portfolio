"""
Capture screenshots of diagrams + case study pages at 6 breakpoints using Playwright.

Usage:
    python3 working/mobile-audit/scripts/screenshot-diagrams.py [case-study-slug]

If no slug provided, captures all case studies.

Output: working/mobile-audit/screenshots/{width}/{case-study}/{diagram-id}.png
        working/mobile-audit/screenshots/{width}/pages/{case-study}.png

Requirements:
    pip install playwright --break-system-packages
    python3 -m playwright install chromium
"""
import asyncio
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Missing dependency. Install with: pip install playwright --break-system-packages")
    print("Then: python3 -m playwright install chromium")
    sys.exit(1)

BREAKPOINTS = [1440, 1024, 768, 480, 375, 320]

CASES = {
    "case-ai.html": "case-ai",
    "case-notifications.html": "case-notifications",
    "case-sharing.html": "case-sharing",
    "case-subreddit.html": "case-subreddit",
    "case-building-portfolio.html": "case-building-portfolio",
}

async def capture_url(page, url, path, width):
    """Render page at given width and save screenshot."""
    await page.set_viewport_size({"width": width, "height": 900})
    await page.goto(url, wait_until="networkidle", timeout=30_000)
    # give CSS a moment to settle
    await page.wait_for_timeout(400)
    path.parent.mkdir(parents=True, exist_ok=True)
    await page.screenshot(path=str(path), full_page=True)

async def process_case(browser, root, case_file, case_slug, screenshots_dir):
    html = (root / case_file).read_text()
    srcs = re.findall(r'src="(img/diagrams/[^"]+\.html)"', html)

    for width in BREAKPOINTS:
        context = await browser.new_context(viewport={"width": width, "height": 900})
        page = await context.new_page()

        # case study page itself
        page_out = screenshots_dir / str(width) / "pages" / f"{case_slug}.png"
        page_url = f"file://{(root / case_file).resolve()}"
        try:
            await capture_url(page, page_url, page_out, width)
            print(f"  [{width}] page → {page_out.relative_to(root)}")
        except Exception as e:
            print(f"  [{width}] page FAILED: {e}")

        # each embedded diagram standalone
        for src in srcs:
            diagram_id = Path(src).stem.replace("diagram-", "")
            diagram_out = screenshots_dir / str(width) / case_slug / f"{diagram_id}.png"
            diagram_url = f"file://{(root / src).resolve()}"
            try:
                await capture_url(page, diagram_url, diagram_out, width)
                print(f"  [{width}] {diagram_id} → {diagram_out.relative_to(root)}")
            except Exception as e:
                print(f"  [{width}] {diagram_id} FAILED: {e}")

        await context.close()

async def main():
    root = Path(__file__).resolve().parents[3]  # portfolio-site/
    screenshots_dir = root / "working/mobile-audit/screenshots"

    target = sys.argv[1] if len(sys.argv) > 1 else None

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for case_file, case_slug in CASES.items():
            if target and case_slug != target:
                continue
            print(f"\n=== {case_slug} ===")
            await process_case(browser, root, case_file, case_slug, screenshots_dir)
        await browser.close()

    print(f"\nDone. Screenshots in: {screenshots_dir.relative_to(root)}")

if __name__ == "__main__":
    asyncio.run(main())
