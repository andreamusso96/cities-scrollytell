<script lang="ts">
  export let label = "Figure placeholder";
  export let note = "Mock pending";
</script>

<div class="placeholder">
  <div class="placeholder-inner">
    <div class="placeholder-label">{label}</div>
    <div class="placeholder-note">{note}</div>
  </div>
</div>

<style>
  .placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background:
      radial-gradient(circle at 50% 45%, rgba(103, 224, 204, 0.08), transparent 24%),
      linear-gradient(180deg, rgba(11, 16, 22, 0.92), rgba(11, 16, 22, 0.94));
  }

  .placeholder-inner {
    width: min(82%, 420px);
    padding: 24px 20px;
    border: 1px dashed rgba(255, 255, 255, 0.12);
    border-radius: 18px;
    text-align: center;
  }

  .placeholder-label {
    color: var(--ink);
    font-family: Arial, sans-serif;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }

  .placeholder-note {
    margin-top: 10px;
    color: var(--muted);
    font-size: 18px;
    line-height: 1.4;
  }

  @media (max-width: 720px) {
    .placeholder-inner {
      width: min(88%, 360px);
      padding: 20px 16px;
    }

    .placeholder-label {
      font-size: 19px;
    }

    .placeholder-note {
      font-size: 16px;
    }
  }
</style>
