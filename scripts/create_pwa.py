import json, os, shutil
from pathlib import Path

BUILD_DIR = Path("_build/html")
BASE_URL = "./"  # Adjust if your site is served from a subpath

# File extensions you want to cache
EXTENSIONS = {'.html', '.js', '.css', '.png', '.svg', '.ico', '.woff2', '.mp4'}

urls = []

for file_path in BUILD_DIR.rglob("*"):
    if file_path.suffix.lower() in EXTENSIONS:
        # Compute the relative URL path from build dir
        relative_path = file_path.relative_to(BUILD_DIR).as_posix()
        url = BASE_URL + relative_path
        urls.append(url)

# TODO: copy these to sw.js
#print(urls);

# Save to _static so it gets copied by Sphinx
output_path = BUILD_DIR / "_static" / "precache-files.json"
output_path.parent.mkdir(parents=True, exist_ok=True)
with output_path.open("w") as f:
    json.dump(urls, f, indent=2)


# Copy PWA items to root
shutil.copyfile('scripts/sw.js', '_build/html/sw.js')
shutil.copyfile('scripts/manifest.webmanifest', '_build/html/manifest.webmanifest')
#shutil.copytree('_static/icons', '_build/html/_static/icons')
