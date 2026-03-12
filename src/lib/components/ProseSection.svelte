<script lang="ts">
  export let heading: string;
  export let paragraphs: string[] = [];
</script>

<article class="article">
  <h2>{heading}</h2>
  <div class="prose">
    {#each paragraphs as paragraph}
      <p>{paragraph}</p>
    {/each}
  </div>
</article>

<style>
  .article {
    max-width: 720px;
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

  .prose p {
    margin: 0 0 1.1em;
    color: #ddd4c8;
  }

  @media (max-width: 720px) {
    .article {
      padding: 20px 16px 54px;
    }
  }
</style>
