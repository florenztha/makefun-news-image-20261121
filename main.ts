// Entry point for the news-image-20261121 make.fun bounty.
//
// The poster itself is baked ahead of time: poster/generate.py builds the
// page from Saturday 21 November 2026's stories and poster/render.py renders
// it in a real browser to entry.png beside this file. Baking the image
// (instead of drawing it here) is what makes the two grader runs trivially
// identical: this program only publishes the baked bytes, byte for byte, to
// the output directory, /output on the grader, or MAKEFUN_OUTPUT_DIR
// locally.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const bakedPoster = new URL("./entry.png", import.meta.url);

copyFileSync(bakedPoster, join(outputDir, "entry.png"));
