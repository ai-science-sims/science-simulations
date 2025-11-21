**Task:** Refactor the provided HTML simulation file to implement single-file internationalization (i18n) supporting English (en-US) and Traditional Chinese (zh-HK).

**Strict Requirements:**

1.  **Single-File Structure:** Do not create external `.json` or `.js` files. Keep everything within the HTML file.
2.  **Languages:**
    *   **Default:** English (`en-US`).
    *   **Secondary:** Traditional Chinese (`zh-HK`).
3.  **Translation Logic:**
    *   Create a `const translations = { 'en-US': { ... }, 'zh-HK': { ... } };` object in the `<script>` section.
    *   Add `data-i18n="keyName"` attributes to all HTML elements that contain text.
    *   Implement a function that:
        *   Updates `document.documentElement.lang`.
        *   Updates `document.title`.
        *   Updates all elements with `data-i18n`.
        *   Updates the URL parameter `?lang=` without reloading the page (`window.history.pushState`).
    *   **Initialization:** On page load, check for a `?lang=` URL parameter. If present, use it; otherwise, default to `en-US`.
4.  **UI Components:**
    *   Add a language selector (EN / 繁) in the top-right corner (`absolute top-4 right-4`). Use the same Tailwind styling as the reference (white buttons with hover effects).
    *   Ensure the selector does not overlap existing header controls; integrate it within the layout as needed while keeping it visually aligned to the top-right.
5.  **Content Guidelines:**
    *   **English:** Ensure all text is natural and grammatically correct.
    *   **Chinese:** Provide "clean" translations. **Do not** include English words in parentheses (e.g., use "靜止", NOT "靜止 (Static)").
6.  **Dynamic Text:**
    *   If the simulation has JavaScript updating text dynamically (e.g., status messages like "Heating", "Boiling"), extract that logic into a function and use the `translations` object to fetch the correct string based on the current language.
7.  **Comments**
    *   If a comment in the source code is in Chinese, change it to English.

**Output:** Provide the full, updated HTML code.
