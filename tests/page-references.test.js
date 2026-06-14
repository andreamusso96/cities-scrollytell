import { readFileSync } from "node:fs";
import test from "node:test";
import assert from "node:assert/strict";

const pageSource = readFileSync(new URL("../src/routes/+page.svelte", import.meta.url), "utf8");

test("renders data references instead of the placeholder", () => {
  assert.doesNotMatch(pageSource, /Still have to add the references here/);
  assert.doesNotMatch(pageSource, /Boundaries & population of cities/);
  assert.doesNotMatch(pageSource, /10\.5281\/zenodo\.17315337/);
  assert.match(pageSource, /Large cities lose their growth advantage as countries urbanize/);
  assert.match(pageSource, /10\.48550\/arXiv\.2510\.12417/);
  assert.match(pageSource, /GHSL Data Package 2023/);
  assert.match(pageSource, /10\.2760\/098587/);
  assert.match(pageSource, /IPUMS ancestry full count data: Version 4\.0/);
  assert.match(pageSource, /10\.18128\/D014\.V4\.0/);
  assert.match(pageSource, /IPUMS National Historical Geographic Information System: Version 19\.0/);
  assert.match(pageSource, /10\.18128\/D050\.V19\.0/);
  assert.match(pageSource, /The census place project: A method for geolocating unstructured place names/);
  assert.match(pageSource, /10\.1016\/j\.eeh\.2022\.101477/);
  assert.match(pageSource, /Growth, innovation, scaling, and the pace of life in cities/);
  assert.match(pageSource, /10\.1073\/pnas\.0610172104/);
  assert.match(pageSource, /Increasing Returns and Economic Geography/);
  assert.match(pageSource, /10\.1086\/261763/);
  assert.match(pageSource, /An evolutionary theory for interpreting urban scaling laws/);
  assert.match(pageSource, /10\.4000\/cybergeo\.2519/);
});

test("adds in-text citation markers for referenced sources", () => {
  for (const referenceNumber of [1, 2, 3, 4, 5, 6, 7, 8]) {
    assert.match(pageSource, new RegExp(`cite\\(${referenceNumber}\\)`));
  }
});
