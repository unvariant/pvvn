import os
import sys
from pathlib import Path

for dirpath, directories, files in os.walk(sys.argv[1]):
    parent = Path(dirpath)
    for file in files:
        orig = parent / file
        if "?" in file:
            file = file[:file.index("?")]
            new = parent / file
            if new.exists():
                orig.unlink()
            else:
                orig.rename(new)

import re

fixup = [
    "/login",
    "/sensai",
    "/sensei",
    "/register",
    "/belts",
    "/dojo/welcome",
    "/dojos/create",
]

for dirpath, directories, files in os.walk(sys.argv[1]):
    parent = Path(dirpath)
    for file in files:
        if ".html" not in file:
            continue
        f = parent / file
        with open(f) as fp:
            content = fp.read()
        for pat in fixup:
            content = re.sub(f"href=\"{pat}.*?\"", f"href=\"{pat}.html\"", content)
        with open(f, "w") as fp:
            fp.write(content)