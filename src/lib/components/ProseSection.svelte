<script lang="ts">
  import CitedParagraph from "./CitedParagraph.svelte";

  type CitationRef = {
    ref: number;
  };

  type ParagraphToken = string | CitationRef;
  type CitedParagraphValue = string | ParagraphToken[];

  export let heading: string | undefined = undefined;
  export let paragraphs: CitedParagraphValue[] = [];
</script>

<article class="article">
  {#if heading}
    <h2>{heading}</h2>
  {/if}
  <div class="prose">
    {#each paragraphs as paragraph}
      <CitedParagraph {paragraph} />
    {/each}
  </div>
</article>

<style>
  .article {
    max-width: 550px;
    margin: 0 auto;
    padding: 26px 18px 56px;
  }

  h2 {
    margin: 0 0 18px;
    font-size: clamp(28px, 6vw, 48px);
    line-height: 0.95;
    letter-spacing: -0.03em;
  }

  .prose {
    font-size: clamp(19px, 4.6vw, 24px);
    line-height: 1.52;
  }

  @media (max-width: 720px) {
    .article {
      padding: 20px 16px 54px;
    }
  }
</style>
