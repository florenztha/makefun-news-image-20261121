# Build notes: news-image-20261121

- **Day summed up:** Saturday 21 November 2026 (events that happened, or
  were first reported, that day in at least one time zone).
- **Stories:** 32 total: 3 leads and 10 more stories drawn as original
  vector scenes, plus 19 briefs. Region counts on the poster are computed
  from the story data in `poster/generate.py`, so the region bar always
  matches the stories printed.
- **Figures cross-checked while building** (21 Nov 2026 reporting): the
  overnight barrage on Ukraine at more than 400 drones and 110 missiles,
  at least 8 killed in Kyiv with bridges and stations damaged, about 20
  wounded in Kryvyi Rih, and two missiles plus a suspected drone down in
  Poland, which PM Tusk called a deliberate provocation (France 24, CBS,
  El Pais via the day's briefs); US stocks down 3.7% with the S&P 500 and
  Dow in correction; the ICJ finding Myanmar responsible for genocide
  against the Rohingya; the daraxonrasib pill trial (tumours undetectable
  in 1 in 12 patients); the UK-EU Brussels agreements on food exports,
  carbon markets and youth mobility; COP31 in Antalya in overtime.
- **Date discipline:** the Shenzhen leaders met on Thursday and Anthropic
  opened trading on Thursday; both are printed with their Saturday
  consequences (the joint declaration and Trump's defund-Ukraine call;
  the $2 trillion value inside Friday's sell-off story) and the DATE CHECK
  box on the poster says so plainly.
- **Render:** `poster/poster.html` is rendered by a headless Chromium at
  1024x1024 (`poster/render.py`); the flat-colour PNG lands well under the
  1 MiB gate without quantising.
- **Determinism:** `main.ts` only copies the baked `entry.png`; two local
  runs were compared with sha256 and are byte-identical.
- **V4 revision (2026-11-21, at the user's request after reviewing V3):**
  the map panel was narrowed (522 to 468 px) so it stops dominating the
  row, its ocean and land tones were deepened so the panel no longer reads
  as empty white space, and the lower sections were tightened (mini and
  brief line spacing, key numbers margin) so the footer text ends with a
  clear margin inside the frame. Story selection, figures and text are
  unchanged.
- **V3 revision (2026-11-21, at the user's request after reviewing V2):**
  the dot grid map was replaced by coastline polygons (new module
  `poster/worldmap.py`) drawn on an equirectangular projection at the
  panel's true display aspect, so continents keep their real shapes.
  Europe's four pins (The Hague, London, Brussels, Berlin) no longer stack:
  their numbered labels are lifted clear of the cluster and tied by leader
  lines to small dots at the true positions. Story selection, figures and
  text are unchanged.
- **V2 revision (2026-11-21, at the user's request after reviewing V1):**
  every art panel was redrawn to the wide banner aspect it is actually
  displayed at (leads 300x84, features 300x74), so the numbers and captions
  inside the art render at full size instead of being vertically squashed:
  the markets panel's -3.7% and Anthropic strip, the COP31 overtime line,
  and the pill panel's 1 IN 12 are now set as banner typography, and the
  ICJ GENOCIDE stamp no longer overlaps the court caption. Story selection,
  figures and text are unchanged from V1.
- **V1 (2026-11-21):** first build. Lead order Kyiv, Shenzhen, The Hague,
  following the day's own weight: the largest barrage of the war reaching
  NATO soil, the first three-way leaders' declaration, and the first
  state-genocide ruling from the world court. The AI story is held as a
  feature with its paradox intact (rout and record debut in one panel)
  rather than split across two slots.
