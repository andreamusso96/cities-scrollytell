import { readFileSync } from "node:fs";
import test from "node:test";
import assert from "node:assert/strict";

const pageSource = readFileSync(new URL("../src/routes/+page.svelte", import.meta.url), "utf8");

test("renders data references instead of the placeholder", () => {
  assert.doesNotMatch(pageSource, /Still have to add the references here/);
  assert.match(pageSource, /10\.5281\/zenodo\.17315337/);
  assert.match(pageSource, /GHSL Data Package 2023/);
  assert.match(pageSource, /10\.2760\/098587/);
  assert.match(pageSource, /IPUMS ancestry full count data: Version 4\.0/);
  assert.match(pageSource, /10\.18128\/D014\.V4\.0/);
  assert.match(pageSource, /IPUMS National Historical Geographic Information System: Version 19\.0/);
  assert.match(pageSource, /10\.18128\/D050\.V19\.0/);
  assert.match(pageSource, /The census place project: A method for geolocating unstructured place names/);
  assert.match(pageSource, /10\.1016\/j\.eeh\.2022\.101477/);
});
