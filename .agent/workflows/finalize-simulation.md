---
description: Generate screenshot and register simulation in system
---

# Workflow: Finalize Simulation

**Purpose:** Generate standardized screenshot and register the simulation in `simulations.json`.

**When to use:** After completing `refactor-simulation.md` workflow and manually reviewing/fine-tuning the i18n implementation.

**Prerequisites:**
- ✅ Simulation file is in final location (e.g., `simulations/physics/optics-and-wave-motion/refraction.html`)
- ✅ i18n is tested and approved
- ✅ All translations are finalized
- ✅ File is ready for production

---

## Steps

### 1. Generate screenshot

**Requirements:**
- Viewport size: **1280x720** (16:9 aspect ratio)
- Wait for full page load and rendering
- Capture entire viewport
- Save to `screenshots/` directory

**Process:**
// turbo
```bash
# Use browser_subagent to:
# 1. Open the simulation file
# 2. Set viewport to 1280x720
# 3. Wait 3 seconds for rendering
# 4. Capture screenshot
# 5. Save to screenshots/[filename].png
```

**Naming convention:**
- Use the simulation filename with `.png` extension
- Example: `refraction.html` → `refraction.png`

### 2. Verify screenshot

**Check:**
- File exists in `screenshots/` directory
- File size is reasonable (typically 200-500KB)
- Dimensions are correct (may be 2x due to retina: 2560x1440)
- Visual quality is good

**If screenshot needs adjustment:**
- Adjust simulation layout/styling
- Re-run screenshot generation
- Repeat until satisfied

### 3. Register in simulations.json

**Location:** `data/simulations.json`

**Add new entry with:**

```json
{
    "id": "simulation-id",
    "category": {
        "en-US": "Category Name",
        "zh-HK": "類別名稱"
    },
    "title": {
        "en-US": "Simulation Title",
        "zh-HK": "模擬標題"
    },
    "description": {
        "en-US": "English description of what the simulation does.",
        "zh-HK": "模擬功能的中文描述。"
    },
    "contributors": [
        "Contributor Name"
    ],
    "simulationUrl": "simulations/[subject]/[category]/[filename].html",
    "screenshotUrl": "screenshots/[filename].png",
    "createdAt": "YYYY-MM-DD",
    "updatedAt": "YYYY-MM-DD"
}
```

**Field guidelines:**
- `id`: Kebab-case, matches filename (without extension)
- `category`: Use existing categories when possible
  - Physics categories: "Optics and Wave Motion", "Force and Motion", "Heat and Gases", "Quantum Physics", "Electricity and Magnetism", "Radioactivity and Nuclear Energy"
  - Other: "Biology", "Chemistry"
- `title`: Extract from simulation's `<h1>` or title
- `description`: Brief, informative summary (1-2 sentences)
- `contributors`: Extract from original filename or metadata
- `simulationUrl`: Relative path from project root
- `screenshotUrl`: Relative path from project root
- `createdAt`/`updatedAt`: Use current date (YYYY-MM-DD format)

### 4. Verify registration

**Checks:**
// turbo
```bash
# Validate JSON syntax
cat data/simulations.json | python3 -m json.tool > /dev/null && echo "✅ JSON is valid"

# Check for duplicate IDs
cat data/simulations.json | grep '"id"' | sort | uniq -d
```

**Manual verification:**
- No duplicate IDs
- All URLs are correct and accessible
- Screenshot URL matches actual file
- Bilingual content is complete

### 5. Test on homepage

**Verify:**
- Open `index.html` in browser
- Check simulation appears in correct category
- Screenshot displays properly
- Click through to simulation works
- Language switching works on both homepage and simulation

---

## ✅ Completion Checklist

- [ ] Screenshot generated at correct dimensions
- [ ] Screenshot saved to `screenshots/` directory
- [ ] Entry added to `simulations.json`
- [ ] JSON syntax is valid
- [ ] No duplicate IDs
- [ ] All URLs are correct
- [ ] Simulation appears on homepage
- [ ] Both languages work correctly

---

## Output
- ✅ High-quality screenshot in `screenshots/`
- ✅ Simulation registered in `simulations.json`
- ✅ Ready for production deployment
