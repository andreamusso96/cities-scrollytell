# Cities Scrollytell Architecture

## Purpose

This document records the architecture we have actually built so far.

It is not a speculative design doc anymore. It is a high-level snapshot of the current app scaffold, the reusable pieces that exist, and the point the project has reached.

## Current Stack

- App framework: `SvelteKit`
- Scrollytelling engine: `Scrollama`
- Rendering approach: `SVG-first`
- Deployment target: static site
- Design priority: mobile first

The current build is intentionally simple. We are building the scrollytell one reusable scene family at a time instead of trying to design the entire system upfront.

## Current Page Model

At the moment, the app has two scene types:

- `ProseSection`
- `StickyScene`

The page alternates between normal prose blocks and full-screen sticky scenes.

This is the current reading rhythm:

1. prose
2. sticky scene
3. prose
4. sticky scene

That rhythm is deliberate. The sticky scene acts as a pause in the article where the reader stays with one visual while scrolling through its internal animation states.

## Sticky Scene Shell

The main reusable shell is [`StickyScene.svelte`](/Users/andrea/Desktop/PhD/scrollytell/cities-scrollytell/src/lib/components/StickyScene.svelte).

It currently provides:

- a centered full-viewport sticky stage
- a fixed three-box layout:
  - top card
  - middle canvas
  - bottom legend
- Scrollama step handling
- step progress
- a short invisible tail at the end so the final animation can finish before the scene unsticks

The visual layout is intentionally conservative for now. We stopped iterating on more complex card/canvas anchoring patterns and kept the simpler centered cluster because it is stable and good enough to build on.

## First Reusable Visual Family

The first real reusable renderer is [`XYGraphCanvas.svelte`](/Users/andrea/Desktop/PhD/scrollytell/cities-scrollytell/src/lib/components/xy-graph/XYGraphCanvas.svelte).

This is the common analytic chart grammar for the piece.

It currently supports:

- x and y axes
- `linear` and `log` scales
- large mobile-readable axis typography
- axis fade-in
- one or more line series
- line drawing with scroll progress
- point annotations tied to a curve
- endpoint labels for curves
- per-chart margins

The type definitions for this family live in [`types.ts`](/Users/andrea/Desktop/PhD/scrollytell/cities-scrollytell/src/lib/components/xy-graph/types.ts).

This is the first important abstraction in the app. It already covers a large share of the charts we want later.

## Current State Management

Right now the system is intentionally local and simple.

- Scene text is defined in [`+page.svelte`](/Users/andrea/Desktop/PhD/scrollytell/cities-scrollytell/src/routes/+page.svelte)
- Demo chart data is also defined there
- Graph configs are built with small helper functions in the page
- `StickyScene` exposes `activeStepIndex` and `stepProgress` through slots
- `XYGraphCanvas` receives a graph object and renders from it

So the current flow is:

`page state -> sticky scene step state -> graph config builder -> XY graph renderer`

There is no external data pipeline yet, and no global manifest system yet. That is intentional.

## Interaction Model

The current interaction model is:

- step-based
- scroll-driven
- mostly discrete

We are not building a heavily scrubbed global animation system.

Instead:

- axes fade in by step
- lines draw as the reader scrolls through a step
- annotations appear once a line reaches them
- the scene remains pinned long enough for the last state to complete

This is the right level of complexity for now. It keeps the piece readable and keeps the implementation controllable.

## Mobile-First Decisions

Several decisions are already locked in:

- chart typography should be as large as prose, or larger
- the sticky scene width is constrained on desktop so it still feels close to phone proportions
- labels and annotations are tuned for small screens first
- endpoint labels are kept inside the canvas with reserved gutters when necessary

This is important: the visual system is not being designed desktop-first and then adapted later.

## What Exists Today

The app currently has:

- the SvelteKit scaffold
- the prose component
- the sticky scene shell
- the reusable XY graph component
- demo scenes that prove:
  - axis fade-in
  - line drawing
  - point annotations
  - endpoint labels
  - sticky hold at the end of a scene

So the project is no longer at the mock-only stage. We now have a real app shell and one working reusable chart family.

## What Does Not Exist Yet

These pieces are not built yet:

- map / boundary reveal scene family
- globe scene family
- block histogram scene family
- dot-cluster comparison scene family
- real data ingestion pipeline
- scene manifest system

Those can come later. The current rule is simple: only abstract what we have already proven we need.

## Guiding Principle

The architecture is deliberately lean.

We are not trying to build a perfect generalized storytelling engine upfront.

Instead, the current approach is:

1. build the shared shell
2. build one reusable visual family
3. tune it until it feels right
4. add the next family only when needed

That is the point we have reached now.

## Immediate Next Step

The next phase is to add the next scene family on top of the same sticky shell.

The most likely candidates are:

- a layered map / boundary reveal scene
- a block-based histogram scene

But the important thing is that the scaffold is now in place and the first reusable graph system is working.
