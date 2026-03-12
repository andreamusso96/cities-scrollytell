<slot />

<style>
  :global(:root) {
    --bg: #050607;
    --ink: #f5efe5;
    --muted: #b8ada0;
    --line: #24303c;
    --card: rgba(12, 16, 23, 0.92);
    --shadow: 0 24px 72px rgba(0, 0, 0, 0.35);
  }

  :global(*) {
    box-sizing: border-box;
  }

  :global(html) {
    background:
      radial-gradient(circle at top left, rgba(26, 32, 40, 0.48), transparent 28%),
      radial-gradient(circle at bottom right, rgba(18, 22, 29, 0.56), transparent 24%),
      linear-gradient(180deg, #080a0d 0%, var(--bg) 100%);
    color: var(--ink);
  }

  :global(body) {
    margin: 0;
    min-height: 100vh;
    color: var(--ink);
    font-family: Georgia, "Times New Roman", serif;
    background: transparent;
  }
</style>
