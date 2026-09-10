# AGENT.md

## What this repo is

Static educational site hosting interactive science simulations (no build step, no framework). The homepage/catalogue is `index.html`, backed by the JSON catalogue at `data/simulations.json`. See `README.md` for structure and usage.

## How simulations work

- Each simulation is an **independent, standalone HTML file** under subject directories, e.g. `simulations/biology/micro-ecosystem.html`, `simulations/physics/optics-and-wave-motion/refraction.html`.
- Preserve this independence: simulations must not depend on each other or on shared scripts. Do not introduce shared abstractions/helpers unless explicitly required.
- Use **kebab-case** for filenames and catalogue IDs (id matches filename without extension).
- Simulations are **bilingual (en-US / zh-HK)**, with a language toggle and support for the existing `?lang=en-US` / `?lang=zh-HK` URL parameter.

## Catalogue and screenshots

- Register each new simulation in `data/simulations.json` (id, bilingual category/title/description, contributors, `simulationUrl`, `screenshotUrl`, dates).
- Save a matching **1280x720** screenshot as `screenshots/<filename>.png`.

## Verification

- Serve locally with `python3 -m http.server` in the repo root, then open `http://localhost:8000`.
- Validate JSON syntax and check for duplicate IDs manually (see `.agent/workflows/finalize-simulation.md` for the exact validation commands).
- Manually confirm the homepage renders the simulation, the screenshot loads, and both languages work on homepage and simulation.

## Working in this repo

- Avoid unrelated changes and files outside the task scope.
- Preserve pre-existing worktree modifications that are not part of your task.
