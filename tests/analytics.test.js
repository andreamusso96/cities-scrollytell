import { readFileSync } from "node:fs";
import test from "node:test";
import assert from "node:assert/strict";

const appHtml = readFileSync(new URL("../src/app.html", import.meta.url), "utf8");

test("installs the Google Analytics page-view tag", () => {
  assert.match(appHtml, /https:\/\/www\.googletagmanager\.com\/gtag\/js\?id=G-ZRFBSC3J9P/);
  assert.match(appHtml, /window\.dataLayer = window\.dataLayer \|\| \[\];/);
  assert.match(appHtml, /gtag\('config', 'G-ZRFBSC3J9P'\);/);
});
