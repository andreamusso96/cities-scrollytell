import type { LoadEvent } from "@sveltejs/kit";
import type { PageLoad } from "./$types";


async function loadJson(fetch: LoadEvent["fetch"], path: string) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Failed to load ${path}: ${response.status}`);
  }
  return response.json();
}


export const load: PageLoad = async ({ fetch }) => {
  const [figure02, figure03, figure07, figure08, figure09, figure11, figure12, figure13] =
    await Promise.all([
    loadJson(fetch, "/data/figures/figure-02.json"),
    loadJson(fetch, "/data/figures/figure-03.json"),
    loadJson(fetch, "/data/figures/figure-07.json"),
    loadJson(fetch, "/data/figures/figure-08.json"),
    loadJson(fetch, "/data/figures/figure-09.json"),
    loadJson(fetch, "/data/figures/figure-11.json"),
    loadJson(fetch, "/data/figures/figure-12.json"),
    loadJson(fetch, "/data/figures/figure-13.json")
    ]);

  return {
    generatedFigures: {
      figure02,
      figure03,
      figure07,
      figure08,
      figure09,
      figure11,
      figure12,
      figure13
    }
  };
};
