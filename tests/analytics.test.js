import { existsSync, readFileSync } from "node:fs";
import test from "node:test";
import assert from "node:assert/strict";

const appHtml = readFileSync(new URL("../src/app.html", import.meta.url), "utf8");

test("installs the Google Analytics page-view tag", () => {
  assert.match(appHtml, /https:\/\/www\.googletagmanager\.com\/gtag\/js\?id=G-ZRFBSC3J9P/);
  assert.match(appHtml, /window\.dataLayer = window\.dataLayer \|\| \[\];/);
  assert.match(appHtml, /gtag\('config', 'G-ZRFBSC3J9P'\);/);
});

test("places the Google tag immediately after the head opens", () => {
  const headStart = appHtml.indexOf("<head>");
  const googleTagStart = appHtml.indexOf("<!-- Google tag (gtag.js) -->");
  const firstMetaStart = appHtml.indexOf("<meta charset");

  assert.notEqual(headStart, -1);
  assert.notEqual(googleTagStart, -1);
  assert.notEqual(firstMetaStart, -1);
  assert.equal(googleTagStart > headStart, true);
  assert.equal(googleTagStart < firstMetaStart, true);
});

test("installs the city favicon", () => {
  assert.match(appHtml, /<link rel="icon" type="image\/png" href="\/city_png\.png" \/>/);
  assert.equal(existsSync(new URL("../static/city_png.png", import.meta.url)), true);
});
