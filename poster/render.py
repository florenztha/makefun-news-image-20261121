#!/usr/bin/env python3
"""Render poster.html to ../entry.png at exactly 1024x1024 and <= 1 MiB.

Uses a headless Chromium for a real browser render, then Pillow to quantise
only if the flat-colour PNG still exceeds the 1 MiB gate. Deterministic: the
same poster.html always produces the same entry.png bytes.
"""
import pathlib
import subprocess

HERE = pathlib.Path(__file__).parent
REPO = HERE.parent
RAW = HERE / "entry_raw.png"
OUT = REPO / "entry.png"


def find_chrome():
    import glob
    import shutil
    candidates = sorted(glob.glob(str(pathlib.Path.home() /
          ".cache/ms-playwright/chromium_headless_shell-*/chrome-linux/headless_shell")))
    candidates += sorted(glob.glob(str(pathlib.Path.home() /
          ".cache/ms-playwright/chromium-*/chrome-linux/chrome")))
    candidates += ["chromium", "chromium-browser", "google-chrome"]
    for c in candidates:
        p = c if pathlib.Path(c).exists() else shutil.which(c)
        if p:
            return p
    raise SystemExit("no chromium binary found")


def main():
    chrome = find_chrome()
    subprocess.run(
        [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         "--force-device-scale-factor=1", "--window-size=1024,1024",
         f"--screenshot={RAW}", (HERE / "poster.html").as_uri()],
        check=True, capture_output=True, timeout=120)
    from PIL import Image
    im = Image.open(RAW)
    assert im.size == (1024, 1024), im.size
    im = im.convert("RGB")
    im.save(OUT, optimize=True)
    size = OUT.stat().st_size
    if size > 1_048_576:
        q = im.quantize(colors=224, method=Image.MEDIANCUT, dither=Image.FLOYDSTEINBERG)
        q.save(OUT, optimize=True)
        size = OUT.stat().st_size
    print("entry.png", size, "bytes")
    assert size <= 1_048_576, "still over the 1 MiB gate"
    RAW.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
