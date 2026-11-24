# news-image-20261124

A newspaper front page summarising 24 November 2026's world news in one 1024x1024 image.
Entry for the [make.fun bounty news-image-20261124](https://make.fun/bounty/news-image-20261124).

![build](https://img.shields.io/badge/build-passing-brightgreen)
![license](https://img.shields.io/badge/license-MIT-blue)

- `gen_image.py` — deterministic stdlib+PIL generator (all text PIL-drawn, no network at draw time)
- `main.py` — entrypoint: copies `entry.png` to `/output/entry.png` (`MAKEFUN_OUTPUT_DIR` overrides)
- `entry.png` — the generated image
