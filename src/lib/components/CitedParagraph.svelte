<script lang="ts">
  type CitationRef = {
    ref: number;
  };

  type ParagraphToken = string | CitationRef;

  export let paragraph: string | ParagraphToken[];

  $: tokens = typeof paragraph === "string" ? [paragraph] : paragraph;
</script>

<p>
  {#each tokens as token}
    {#if typeof token === "string"}
      {token}
    {:else}
      <sup class="citation">
        <a href={`#reference-${token.ref}`} aria-label={`Reference ${token.ref}`}>{token.ref}</a>
      </sup>
    {/if}
  {/each}
</p>

<style>
  p {
    margin: 0 0 1.1em;
    color: #ddd4c8;
  }

  .citation {
    margin-left: 0.12em;
    font-family: Arial, sans-serif;
    font-size: 0.56em;
    font-weight: 700;
    line-height: 0;
    vertical-align: super;
  }

  .citation a {
    color: #67e0cc;
    text-decoration: none;
  }

  .citation a:hover,
  .citation a:focus-visible {
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 2px;
  }
</style>
