<script lang="ts">
  import { browser } from "$app/environment";
  import { onMount, tick } from "svelte";
  import scrollama from "scrollama";

  type Step = {
    id: string;
    kicker: string;
    title: string;
    body: string;
    accentColor?: string;
  };

  export let sceneId: string;
  export let steps: Step[] = [];
  export let ariaLabel = "";
  export let pinDurationVh = 280;
  export let tailHoldVh = 68;

  let activeStepIndex = 0;
  let stepProgress = 0;

  const domId = `scene-${sceneId}`;
  const stepHeightVh = steps.length > 0 ? pinDurationVh / steps.length : pinDurationVh;

  function clamp(value: number, min = 0, max = 1) {
    return Math.min(Math.max(value, min), max);
  }

  onMount(() => {
    if (!browser) {
      return;
    }

    let scroller: ReturnType<typeof scrollama> | undefined;
    const handleResize = () => scroller?.resize();

    void tick().then(() => {
      scroller = scrollama();

      scroller
        .setup({
          step: `#${domId} .scene-step`,
          offset: 0.6,
          progress: true
        })
        .onStepEnter((event) => {
          activeStepIndex = event.index;
          stepProgress = 0;
        })
        .onStepProgress((event) => {
          if (event.index === activeStepIndex) {
            stepProgress = clamp(event.progress);
          }
        });

      window.addEventListener("resize", handleResize);
    });

    return () => {
      window.removeEventListener("resize", handleResize);
      scroller?.destroy();
    };
  });
</script>

<section id={domId} class="sticky-scene" aria-label={ariaLabel}>
  <div class="sticky-stage">
    <div class="sticky-frame">
      <div class="scene-shell">
        <div
          class="scene-card scene-box"
          style={`--scene-accent: ${steps[activeStepIndex]?.accentColor ?? "#67e0cc"}`}
        >
          <div class="scene-kicker">{steps[activeStepIndex]?.kicker}</div>
          <div class="scene-title">{steps[activeStepIndex]?.title}</div>
          <div class="scene-body">{steps[activeStepIndex]?.body}</div>
        </div>

        <div class="scene-canvas">
          <slot
            activeStep={steps[activeStepIndex]}
            activeStepIndex={activeStepIndex}
            {stepProgress}
          />
        </div>

        <div class="scene-legend">
          <slot name="legend" {activeStepIndex} />
        </div>
      </div>
    </div>
  </div>

  <div class="step-stack" aria-hidden="true">
    {#each steps as step (step.id)}
      <div class="scene-step" style={`height: ${stepHeightVh}svh;`}></div>
    {/each}
    <div class="scene-tail" style={`height: ${tailHoldVh}svh;`}></div>
  </div>
</section>

<style>
  .sticky-scene {
    position: relative;
    margin: 0 calc(50% - 50vw) 4svh;
  }

  .sticky-stage {
    position: sticky;
    top: 0;
    height: 100svh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 10px;
  }

  .sticky-frame {
    width: min(100%, 550px);
  }

  .scene-shell {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 0 8px;
  }

  .scene-box {
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    background: var(--card);
    box-shadow: var(--shadow);
  }

  .scene-card {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    width: 100%;
    min-height: clamp(136px, 18svh, 184px);
    padding: 12px 14px 13px;
    border-left: 4px solid var(--scene-accent, #67e0cc);
  }

  .scene-kicker {
    margin-bottom: 8px;
    color: color-mix(in srgb, var(--scene-accent, #67e0cc) 56%, var(--muted));
    font-family: Arial, sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  .scene-title {
    font-size: 24px;
    font-weight: 700;
    line-height: 1;
  }

  .scene-body {
    margin-top: 10px;
    color: var(--muted);
    font-size: 15px;
    line-height: 1.42;
  }

  .scene-canvas {
    position: relative;
    width: 100%;
    aspect-ratio: 4 / 3;
    background: transparent;
    overflow: visible;
  }

  .scene-legend {
    min-height: clamp(44px, 6svh, 60px);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .step-stack {
    position: relative;
  }

  .scene-step {
    width: 100%;
  }

  .scene-tail {
    width: 100%;
  }

  @media (max-width: 720px) {
    .sticky-stage {
      padding: 0 6px;
    }

    .sticky-frame {
      width: 100%;
    }

    .scene-shell {
      gap: 6px;
      padding: 0 6px;
    }

    .scene-card {
      min-height: clamp(122px, 16svh, 160px);
      padding: 10px 12px 11px;
    }

    .scene-title {
      font-size: 20px;
    }

    .scene-body {
      font-size: 14px;
    }
  }
</style>
