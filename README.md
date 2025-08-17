# lamatriz.ai

La Matriz Consulting’s public site and research notebook.
Color as interface between inner knowing and outer data — a lightweight, tracker-free site with demos, research visuals, and an Oracle preview.

**Live:** [https://lamatriz.ai](https://lamatriz.ai)

---

## What’s inside

* **`index.html`** — landing page (hero, 6-card grid, CTA band).
* **`thesis.html`** — “Semantic Color Math” one-pager with figures (UMAP, decision tree, distributions, variance) and 11 pathway cards + summaries.
* **`oracle.html`** — Color Oracle intro + a local, deterministic color-sequence preview and a **Copy to Colab** button that copies the Magnetism→Color Python dashboard.
* **`style.css`** — a11y-first, themeable stylesheet using an *earth palette* and design tokens (WCAG 2.2 AA).
* **`/assets/img/`** — figures & logo used across pages (PNG/JPG/SVG).
* **`/assets/fonts/`** — Inter Variable (served via Google Fonts on the one-pager; you can self-host if preferred).

No frameworks, no build step — just HTML/CSS/JS.

---

## Brand tokens (Earth palette)

All colors are centralized in `style.css` under `:root`.

```css
:root{
  /* primary brand */
  --olive:   #7A8C51;
  --gold:    #D9BA5F;

  /* neutrals / paper */
  --paper:   #F2EBDC;
  --taupe:   #A69D85;
  --brown:   #594E39;
  --ink:     #262014;

  /* accents (warm) */
  --terra:   #BF6849;
  --rose:    #D99E89;

  /* UI tokens (derived) */
  --bg:      var(--ink);      /* dark mode background */
  --surface: #2B241B;
  --card:    #342A20;
  --text:    #F5F3ED;
  --muted:   #C9BEA8;
  --border:  #403424;
  --accent:  var(--olive);
  --accent-2:var(--gold);
}
```

> Light–mode tokens are also defined via `@media (prefers-color-scheme: light)`.
> Typography: Inter (variable); sizes use `clamp()` for responsive scaling.

---

## Local development

This is a static site. Use any static server:

```bash
# Option 1: Python 3
python3 -m http.server 8000

# Option 2: Node
npx serve .

# Option 3: VS Code Live Server extension
```

Open [http://localhost:8000](http://localhost:8000) and browse the pages.

---

## Oracle preview (frontend)

`oracle.html` includes:

* A **starter prompt** copy button for the GPT.
* A **local sequence preview** that generates 11 HSL colors deterministically from your input using a seeded **xorshift32** PRNG (no network calls, no data sent).
* A **Copy Colab engine** button that puts a ready-to-run Python dashboard on your clipboard.

### Colab dashboard (Python)

The “Magnetism-to-Color Sequence Engine” expects three CSVs:

* `semantic_rgb_mapping_with_sentiment.csv`
* `la matrice.csv`
* `la matrice sequences.csv`

Paste the code into Colab, upload the CSVs, and use the sliders:

* **Mass** — scales saturation/value (potential energy feel)
* **Voltage** — pacing; strengthens magnetism slightly
* **Charge (magnetism)** — similarity attraction in sentiment/word space
* **Null Time** — inserts neutral “rests” when arousal is low
* **Start Color / Seed / Length** — initial condition & reproducibility

---

## Thesis figures

`thesis.html` references images in `/assets/img/`, including:

* `concept space with rgb coloring and anchor vectors.png`
* `rgb decision tree.PNG`
* `sentiment distribution.png`
* `filtered UMAP for loops.png`
* `variance sequences.jpg`
* `UMAP update.png`
* `color clusters.png`

Update paths or filenames as needed; keep alt text descriptive for a11y.

---

## Accessibility & performance

* Color contrast targets WCAG 2.2 AA (checked across dark/light tokens).
* Keyboard focus uses visible `:focus-visible` rings.
* Images include alt text; decorative elements use `aria-hidden="true"`.
* No trackers. Minimal JS. Images are `loading="lazy"` where appropriate.

---

## Deployment

Any static host works (GitHub Pages, Netlify, Vercel, Cloudflare Pages).

**GitHub Pages (root project):**

1. Settings → Pages → Source = `Deploy from a branch`.
2. Branch = `main` (or `docs`), folder = `/` (or `/docs`).
3. Save. Pages will serve your HTML at `https://<user>.github.io/lamatriz.ai/`.

**Vercel/Netlify:** drag-and-drop repo; set root to `/`.

---

## Contributing

Issues and PRs are welcome — especially:

* a11y refinements (contrast, focus states, reduced-motion paths)
* cross-browser fallbacks for CSS features like `color-mix()`/`oklab`
* copy edits and figure captions
* small demo ideas that stay fully local/no-tracking

Please keep the tone and intent of the project: **care over extraction**.

---

## Licenses

* **Site code (HTML/CSS/JS)**: Apache 2.0 © La Matriz Consulting
* **Text & images (thesis, figures, brand assets)**: **CC BY-NC-SA 4.0** unless otherwise noted.
  Commercial use of content requires permission.

---

## Credits & links

* Research & writing: **La Matriz Consulting**
* Oracle (ChatGPT custom GPT): [https://chatgpt.com/g/g-686180b5d47c8191bdbb1922b79a2ebb-la-matriz-consulting-color-oracle](https://chatgpt.com/g/g-686180b5d47c8191bdbb1922b79a2ebb-la-matriz-consulting-color-oracle)
* Website: [https://lamatriz.ai](https://lamatriz.ai)

> “Not an answer — a mirror.”
