# Cities Scrollytell Architecture

## Purpose

This document records the architectural decisions for the scrollytelling piece before implementation starts.

The goal is to lock the main technical choices now, so that future prototype work in `src/mock` and later production work do not keep reopening the same framework questions.

## Project Shape

- This repo is currently effectively greenfield from an app perspective.
- There is no existing frontend scaffold that we need to preserve or migrate.
- That means we should choose the stack that best fits an editorial scrollytell, not the stack that best fits an existing codebase.
- The piece should be designed **mobile-first**.
- Assume the overwhelming majority of readers are on phones.
- Desktop matters, but desktop is a secondary adaptation, not the primary design target.

## Chosen Stack

### App framework

- Use **SvelteKit** as the main application framework.

Why:

- It is a strong fit for editorial, interactive, stateful visual stories.
- It keeps component code lighter than a React setup for this kind of work.
- It gives us a proper app shell, static deployment options, routing if needed, and a clean component model.
- Since there is no existing React app in the repo, React would add overhead without giving us a decisive advantage.

### Scrollytelling engine

- Use **Scrollama** as the primary scrollytelling engine.

Why:

- It is still the cleanest step-based scrollytelling engine.
- It uses `IntersectionObserver` rather than raw scroll event bookkeeping.
- It works well with CSS `position: sticky`, which is the right base pattern for this piece.
- It is lightweight and widely used in editorial interactive work.

### Animation layer

- Use **state-driven scene changes** as the default animation model.
- Use **GSAP ScrollTrigger only optionally**, and only for a few hero sequences if we later find that they genuinely need scrubbed or pinned timeline behavior.

Why:

- We do not want ScrollTrigger to become the core scrollytelling framework.
- ScrollTrigger is powerful, but it is better as a local animation tool than as the main narrative engine for this project.
- Scrollama should own chapter activation. Visual components should react to chapter state.

## Current Figure Framework

This section records the framework we are actually using in the mocks in
`src/mock` right now.

### Prototype medium

- Build each mock figure as a **standalone HTML file** in `src/mock`.
- Use **plain HTML + CSS + vanilla JS** for the mock stage.
- Do not pull the full app framework into early visual prototyping.

Why:

- It keeps iteration fast while the figure grammar is still changing.
- It makes each scene easy to open, inspect, and compare in isolation.
- It lets us settle pacing, mobile layout, and visual hierarchy before wiring
  figures into a full app.

### Prototype scroll model

- Use **CSS sticky sections** plus lightweight manual scroll-progress logic.
- A typical mock structure is:
  - prose above
  - one sticky figure section
  - prose below
- Inside the sticky section, scroll progress maps to a small number of
  **discrete scene states**.

Implication:

- The current mocks are **not** using Scrollama yet.
- Scrollama remains the planned production scrolly engine.
- The mock logic is deliberately simpler: sticky stage + progress thresholds +
  state changes.

### Default figure anatomy

- Each figure should occupy a **full mobile viewport** while pinned.
- The visual should get the full stage.
- Use **one top scene card** for the active text state.
- Keep the bottom of the figure available for a compact legend when needed.
- Avoid extra floating labels, cards, or annotation boxes over the map/chart
  unless they are truly necessary.

### Current text pattern inside figures

- Prefer a **single top text box** rather than multiple scrolling overlay cards.
- That box should swap only:
  - kicker
  - title
  - short body copy
  - accent color when relevant
- If the figure already has a legend, do not duplicate that information with
  extra on-figure label cards.

### Current rendering choice

- Use **SVG first** for the current mocks.
- Use HTML overlays only for text that must remain large and readable on
  mobile.
- Keep camera motion minimal. For map scenes, prefer **fixed camera reveals**
  over zoom choreography unless motion is essential to the point.

## Chosen Interaction Model

### Default model: stateful chapters

- Scroll should primarily choose the active **chapter / scene state**.
- Each text step activates a new visual state.
- The visual can animate into that state, but the state itself is discrete and stable.

Examples:

- Map flies to a new location and then settles.
- A chart highlights a new comparison and then holds.
- A layer turns on, labels update, and the scene pauses while the user reads.

### Not the default: heavy scrub

- Do **not** build the piece as a continuously scroll-scrubbed timeline by default.
- Scroll should not directly drive every animation frame of every visual.

Why:

- It is harder to implement and tune.
- It is more fragile on mobile and touch devices.
- It competes with reading.
- It raises performance costs, especially for maps, canvases, and dense visuals.

### Allowed exception: local scrub

- Some hero sequences may still use scrubbed progress inside a chapter.
- This should be rare and intentional.

Good candidates for local scrub:

- satellite image -> built-up grid -> city boundary
- a globe / world-to-city transition
- a carefully designed future-scenario interpolation

## Narrative Layout Pattern

- The core layout pattern should be:
  - foreground text steps
  - sticky visual stage
  - chapter-based state transitions

- In practice this should be interpreted as:
  - article text above and below the sticky figure
  - one persistent **top scene card** inside the figure
  - optional compact legend near the bottom edge
  - minimal obstruction of the visual area
  - text sizes and figure pacing tuned first for phone screens
  - desktop layouts derived from the mobile pattern, not invented separately

- This is close to the Mapbox storytelling pattern:
  - text drives chapter changes
  - the sticky visual updates scene by scene
  - the user reads inside stable visual beats rather than fighting a constantly moving graphic

- The Mapbox scrollytelling example is a **reference pattern**, not a full architecture choice.
- The relevant lesson from it is:
  - chapter-based camera / scene transitions are the right direction
  - not that the whole project should be a map-first app

## Visual Technology Policy

- Use **SVG** for simpler charts, explanatory diagrams, and low-mark-count scenes.
- Use **Canvas** for denser animations, larger particle/point counts, and possibly some map-like layers if performance requires it.
- Use **D3** mainly for scales, layout math, axes, projections, and data transforms.
- Do not let D3 own the whole rendering model by default.

Current practical interpretation for mocks:

- `src/mock/figure-01-city-comparison.html`: SVG dot-pile scene with a single
  top card and discrete metric states
- `src/mock/figure-02-futures.html`: SVG block histogram with fixed unit grammar
  for incoming population and a single top card
- `src/mock/figure-03-paris-boundaries.html`: fixed-camera SVG basemap with
  traced boundaries, faded fills, bottom legend, and one top state card

Implication:

- Component state should live in Svelte.
- D3 should be a utility layer, not the overall application framework.

## Visual Density Decision

For a piece of roughly **2,000 words**:

- Target **8 to 10 meaningful visual moments**
- Aim for roughly **200 to 250 words per major visual**
- Use **3 to 4 full-bleed hero visuals at most**

Do not count every chart variant as a separate visual.

Rules:

- If two charts make the same argument in one section, they should usually be one visual chapter.
- Prefer fewer, stronger, more legible visuals over many smaller ones.
- A visual should earn its existence by advancing the story, not by merely varying presentation.

## Current Practical Conclusion

- `src/outline4.md` is still denser in visual slots than the final build should be.
- Before implementation, the outlined visual beats should be merged into roughly **8 to 10 real scene components**.
- Those components can contain internal sub-states, but they should not behave like 20 disconnected mini-viz blocks.

## Options Considered And Rejected As Primary Architecture

### React + react-scrollama

Rejected as default.

Why:

- Good ecosystem, but unnecessary overhead here.
- No existing React app in the repo.
- Does not offer enough upside over SvelteKit for this editorial piece.

### Plain Vite + Scrollama

Rejected as default.

Why:

- Simpler at first, but becomes less ergonomic once the visuals become stateful and ambitious.
- We want a real component framework for a project of this complexity.

### GSAP ScrollTrigger as the main scrollytelling framework

Rejected as default.

Why:

- Best used selectively for hero interactions, not as the main narrative controller.
- Too easy to drift into over-scrubbed, over-animated, brittle behavior.

### `@sveltejs/svelte-scroller`

Not chosen as the core engine.

Why:

- Elegant, but narrower.
- Scrollama is the more proven and flexible base for this particular piece.

## Implementation Principles Going Forward

- Build the story as **scene components**, not as a pile of one-off charts.
- Keep the visual model **chapter-based by default**.
- Only introduce scrub when a specific scene clearly benefits from it.
- Prototype mock visuals in `src/mock` before building polished production versions.
- Keep the story text-led. Visuals should support reading, not dominate it.
- Default design decisions should be made for **phone reading**:
  - text must remain readable while the figure is visible
  - interactions must tolerate touch scrolling and uneven scroll velocity
  - labels should be sized for mobile first, even if they feel slightly large on desktop
  - labels, callouts, and legends should avoid requiring desktop hover behavior
  - side-by-side desktop-only compositions should not be the default pattern
  - avoid covering the map/chart with extra annotation cards when a top scene box and bottom legend are enough

## Locked Decisions

- Framework: **SvelteKit**
- Scrolly engine: **Scrollama**
- Mock figure framework: **standalone HTML/CSS/JS in `src/mock`**
- Mock scroll model: **sticky section + manual progress thresholds**
- Default interaction: **stateful chapters**
- Scrub policy: **rare, local, opt-in**
- Layout model: **sticky stage + prose above/below + one top scene card**
- Primary target: **mobile-first**
- Rendering mix: **Svelte + SVG/Canvas + D3 utilities**
- Visual density: **8-10 major visual moments for ~2,000 words**
