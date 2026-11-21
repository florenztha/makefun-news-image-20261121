# Saturday 21 November 2026: The World in One Page

A one-page poster that sums up the world's news of **Saturday 21 November
2026** in a single 1024x1024 image: 32 stories, 13 of them drawn as original
vector scenes and pinned on a numbered world map, a key-numbers strip, and a
date-check box that keeps Thursday's and Friday's news honestly labelled.

Entry for the make.fun bounty
[news-image-20261121](https://make.fun/bounty/news-image-20261121).

![Competition](https://make.fun/badge/news-image-20261121.svg)
![Rank](https://make.fun/badge/news-image-20261121/florenztha/makefun-news-image-20261121/rank.svg)
![Reward](https://make.fun/badge/news-image-20261121/florenztha/makefun-news-image-20261121/reward.svg)

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png, the baked poster, byte for byte
```

`main.ts` (Node 22, standard library only, no network) copies the baked
`entry.png` to the output directory, so two runs always produce identical
bytes.

## Rebuild the poster

```sh
python3 poster/generate.py   # stories + drawings -> poster/poster.html
python3 poster/render.py     # real browser render -> entry.png (1024x1024, <= 1 MiB)
```

Every drawing on the page is an original inline SVG written in
`poster/generate.py`; there are no photographs. Story selection and figures
were cross-checked against the day's reporting (AP, Reuters, AFP, BBC,
France 24, CBS, El Pais, UN News, IAEA), see `BUILD.md`.

## License

MIT, see `LICENSE`.
