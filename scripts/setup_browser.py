#!/usr/bin/env python3
"""Set up the persistent Playwright browser environment used for screenshots.

Creates a user-local virtual environment, installs the pinned Playwright
version, and ensures a Chromium browser is available. Safe to re-run; the
environment is reused and nothing is reinstalled when already up to date.
"""

import argparse
import subprocess
import sys
from pathlib import Path

PINNED_PLAYWRIGHT = "1.60.0"


def venv_dir() -> Path:
    """Persistent, user-local location of the screenshot browser environment."""
    return Path.home() / ".local" / "share" / "science-simulations" / "browser-venv"


def venv_python() -> Path:
    """Interpreter inside the persistent venv (handles the Windows layout)."""
    if sys.platform == "win32":
        return venv_dir() / "Scripts" / "python.exe"
    return venv_dir() / "bin" / "python"


def _run(cmd) -> None:
    print("+ " + " ".join(str(part) for part in cmd), flush=True)
    subprocess.run([str(part) for part in cmd], check=True)


def _installed_version(python: Path):
    """Return the Playwright version installed in ``python``, or None."""
    code = "import importlib.metadata as m; print(m.version('playwright'))"
    result = subprocess.run([str(python), "-c", code], capture_output=True, text=True)
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)

    python = venv_python()
    try:
        if not python.exists():
            print(f"Creating virtual environment at {venv_dir()}", flush=True)
            _run([sys.executable, "-m", "venv", str(venv_dir())])

        if _installed_version(python) != PINNED_PLAYWRIGHT:
            print(f"Installing playwright=={PINNED_PLAYWRIGHT}", flush=True)
            _run([python, "-m", "pip", "install", f"playwright=={PINNED_PLAYWRIGHT}"])

        print("Ensuring Chromium browser is installed", flush=True)
        _run([python, "-m", "playwright", "install", "chromium"])
    except subprocess.CalledProcessError as error:
        print(f"\nSetup failed: {error}", file=sys.stderr)
        return 1

    print(f"\nSetup complete. Venv interpreter: {python}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
