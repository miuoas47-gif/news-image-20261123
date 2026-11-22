"""Copy the entry image to the output directory.

The image (entry.png, a JPEG by content) sums up the world news of
Monday 23 November 2026. This program takes no arguments, needs no
network, and writes the same bytes on every run.
"""

import os
import shutil
import sys


def main():
    # The bundled image sits next to this file; the sandbox mounts the
    # repository read-only, so we only ever read it and write the copy.
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
