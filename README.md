# Science Simulations

A collection of interactive science simulations for education.  
These simulations were originally conceptualized by a group of science teachers in Hong Kong and developed with the assistance of AI models.  
Our goal is to create an open platform where teachers can easily build, customize, and share science simulations for classroom use.


## Structure

Simulations are organized by subject:

*   **Biology**
*   **Chemistry**
*   **Physics**

The project originally began as a physics simulations collection, so physics includes several topic-based subfolders. As biology and chemistry expand, they can also adopt similar organization.


## Usage

Here is our production website:
https://ai-science-sims.github.io/science-simulations/

If you pull the repo and want to test it, 
you can do so by running `python3 -m http.server` in the root folder,
then open your browser to: http://localhost:8000.


## Screenshots (developer tooling)

Developer-only tooling for capturing the 1280x720 catalogue screenshots. It is
not part of the site, and the simulations do not depend on it. Run all commands
from the repository root.

**Prerequisites:** Python 3.9+ with `venv`/`pip`, plus network and disk access
for the one-time setup.

**One-time setup** (creates a persistent user-local environment; safe to
re-run):

```bash
python3 scripts/setup_browser.py    # macOS / Linux
py scripts\setup_browser.py         # Windows
```

This creates a virtual environment at
`~/.local/share/science-simulations/browser-venv`, installs the pinned
Playwright version, and ensures Chromium is present. Both the environment and
the standard Playwright browser cache persist between sessions, so no
installation happens on later runs:

- macOS: `~/Library/Caches/ms-playwright`
- Linux: `~/.cache/ms-playwright`
- Windows: `%LOCALAPPDATA%\ms-playwright`

Re-run setup after the pinned version changes, or if the venv or browser cache
is deleted (deleting the cache makes Chromium download again).

**Capture a screenshot** — start the local server in a separate terminal, then
run one of the following.

macOS / Linux:

```bash
python3 -m http.server
python3 scripts/screenshot.py \
  'http://localhost:8000/simulations/physics/optics-and-wave-motion/optics-bench.html?lang=en-US' \
  screenshots/optics-bench.png
```

Windows (PowerShell or Command Prompt, one line):

```bat
py -m http.server
py scripts\screenshot.py "http://localhost:8000/simulations/physics/optics-and-wave-motion/optics-bench.html?lang=en-US" screenshots\optics-bench.png
```

The screenshot script uses the persistent environment automatically; if that
environment is missing, run the setup step above first.

On Linux, Chromium may need system libraries, which are not installed
automatically (and may require administrator rights):

```bash
~/.local/share/science-simulations/browser-venv/bin/python -m playwright install-deps chromium
```


## Contributing

We welcome contributions from other science teachers!

*   **Found an issue?** Please [open an Issue](https://github.com/ai-science-sims/science-simulations/issues) to report bugs or suggest improvements.
*   **Want to collaborate?** If you have a simulation to share or want to help improve existing ones, feel free to submit a Pull Request, contact us via the Issues tab, or reach out directly if you already collaborate with us through teacher networks (e.g., WhatsApp).


## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.