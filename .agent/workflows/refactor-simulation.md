---
description: Refactor simulation with i18n and move to final location
---

# Workflow: Refactor Simulation with i18n

**Purpose:** Apply internationalization to a simulation file and move it to the correct directory structure.

**When to use:** When you have a new simulation file in `_new/` that needs i18n support before being added to the project.

**Important:** This workflow stops before screenshot generation to allow you to review and fine-tune translations.

---

## Steps

### 1. Identify the source file
- Locate the HTML file in `_new/` directory
- Note the original filename and any metadata (contributor name, subject area)

### 2. Apply i18n refactoring
Apply the following transformations:

**Required elements:**
- Create `translations` object with `en-US` and `zh-HK` keys
- Add `data-i18n` attributes to all static text elements
- Implement `changeLanguage(lang)` function
- Add language selector in top-right corner (`absolute top-4 right-4`)
- Initialize language from URL parameter `?lang=`
- Update `document.title` and `document.documentElement.lang`
- Use `window.history.pushState` to update URL without reload

**Translation guidelines:**
- English: Natural, grammatically correct
- Chinese: Clean translations WITHOUT English in parentheses
  - ✅ Good: "真空 / 空氣"
  - ❌ Bad: "真空 (Vacuum) / 空氣 (Air)"
- Dynamic text: Extract to translation functions (e.g., `t(key)`, `tMedia(name)`)
- Comments: Convert Chinese comments to English

**UI integration:**
- Language selector: Two buttons (EN / 繁)
- Active language: Highlighted with blue styling
- Inactive: Gray with hover effects
- Position: Does not overlap existing controls

### 3. Rename file to kebab-case
Convert filename to lowercase with hyphens:
- Remove author names in parentheses
- Replace spaces and underscores with hyphens
- Examples:
  - `refraction (Harry Lau).htm` → `refraction.html`
  - `Wave interference (Winky Yeung).html` → `wave-interference.html`
  - `Ray diagram for lens V13 （Poon Yin Kwong).html` → `ray-diagram-lens.html`

### 4. Determine target directory
Based on simulation content, move to:
- Physics → `simulations/physics/[subcategory]/`
  - Subcategories: `optics-and-wave-motion`, `force-and-motion`, `heat-and-gases`, `quantum-physics`, `electricity-and-magnetism`, `radioactivity-and-nuclear-energy`
- Biology → `simulations/biology/`
- Chemistry → `simulations/chemistry/`

### 5. Move file to target location
- Create directory if it doesn't exist
- Move the refactored file
- Verify file is accessible

---

## ⏸️ CHECKPOINT: Manual Review Required

**Before proceeding to the next workflow:**

1. **Test the simulation:**
   - Open the file in a browser
   - Test language switching (EN ↔ 繁)
   - Verify all text translates correctly
   - Check dynamic content updates properly

2. **Fine-tune translations:**
   - Adjust any awkward phrasing
   - Ensure technical terms are accurate
   - Verify Chinese translations are clean (no English in parentheses)

3. **Visual polish:**
   - Ensure language selector doesn't overlap controls
   - Check responsive layout
   - Verify all UI elements are properly styled

**When satisfied, proceed to:** `finalize-simulation.md` workflow

---

## Output
- ✅ Refactored HTML file with full i18n support
- ✅ File in correct directory with proper naming
- ⏸️ Ready for review and fine-tuning
