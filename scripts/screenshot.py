#!/usr/bin/env python3
"""Capture a 1280x720 screenshot of a URL for the catalogue.

Uses the persistent browser environment created by ``setup_browser.py`` and
re-executes into its interpreter automatically when needed.
"""

import argparse
import os
import sys
from pathlib import Path
from urllib.parse import urlparse

import setup_browser


def _running_in_venv() -> bool:
    return Path(sys.prefix).resolve() == setup_browser.venv_dir().resolve()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Page URL to capture (http, https or file)")
    parser.add_argument("output", help="Destination PNG path")
    args = parser.parse_args(argv)

    parsed = urlparse(args.url)
    if parsed.scheme in ("http", "https"):
        if not parsed.hostname:
            parser.error(f"URL must include a hostname: {args.url!r}")
    elif parsed.scheme != "file":
        parser.error(f"unsupported URL scheme: {args.url!r} (use http, https or file)")

    output = Path(args.output)
    if output.suffix.lower() != ".png":
        parser.error(f"output must be a .png file: {args.output!r}")

    setup_hint = (
        "py scripts\\setup_browser.py"
        if sys.platform == "win32"
        else "python3 scripts/setup_browser.py"
    )
    python = setup_browser.venv_python()
    if not _running_in_venv():
        if not python.exists():
            print(
                "Browser environment not found. Run this first:\n"
                f"  {setup_hint}",
                file=sys.stderr,
            )
            return 1
        os.execv(str(python), [str(python), __file__, args.url, args.output])

    try:
        from playwright.sync_api import Error as PlaywrightError
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "Playwright is missing from the browser environment. Run:\n"
            f"  {setup_hint}",
            file=sys.stderr,
        )
        return 1

    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                page = browser.new_page(
                    viewport={"width": 1280, "height": 720},
                    device_scale_factor=1,
                )
                response = page.goto(args.url)
                if response is not None and response.status >= 400:
                    print(
                        f"Failed to load {args.url}: HTTP {response.status}",
                        file=sys.stderr,
                    )
                    return 1
                page.wait_for_load_state("load")
                page.wait_for_timeout(3000)
                page.screenshot(path=str(output), type="png", full_page=False)
            finally:
                browser.close()
    except PlaywrightError as error:
        reason = str(error).splitlines()[0] if str(error) else repr(error)
        print(
            f"Browser capture failed: {reason}\n"
            f"If Chromium is missing, run: {setup_hint}",
            file=sys.stderr,
        )
        return 1
    except OSError as error:
        print(f"Could not write screenshot: {error}", file=sys.stderr)
        return 1

    print(f"Screenshot saved to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
