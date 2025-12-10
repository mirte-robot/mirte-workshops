


# open all .html files in build/html/en and change "images/" to "../images/" and "_static/" to "../_static/"

import os, json, shutil, argparse

parser = argparse.ArgumentParser(description="Dedup script")
parser.add_argument('--dir', required=True, help='Directory to the workshop directory (located in docs/workshops) to build')
args = parser.parse_args()
args.dir = args.dir if args.dir != "homepage" else ""

script_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.abspath( f'{script_path}/../_static/js/articles.json')) as file:
    # Parse the JSON data
    articles_data = json.load(file)


def dedup_one(lang, default_lang = articles_data["default_language"]):

    default_folder_path = os.path.abspath( f'{script_path}/../_build/html/{default_lang}/{args.dir}')
    folder_path = os.path.abspath( f'{script_path}/../_build/html/{lang}/{args.dir}')
    html_files = []
    if os.path.isdir(folder_path) and os.path.isdir(default_folder_path):
        for root, dirs, files in list(os.walk(folder_path)):
            for file in files:
                if file.endswith('.html'):
                    html_files.append(os.path.join(root, file))

        # replace "images/" with "../images/" and "_static/" with "../_static/"
        for file in html_files:
            with open(file, 'r+') as f:
                t = f.read()
                t = t.replace("_images/", f"../../../{default_lang}/{args.dir}/_images/").replace("_static/", f"../../../{default_lang}/{args.dir}/_static/")
                f.seek(0)
                f.write(t)
                f.truncate()

        # delete _images and _static
        shutil.rmtree(f'{folder_path}/_images')
        shutil.rmtree(f'{folder_path}/_static')

for lang in articles_data["languages"]:
    if (lang["short"] != articles_data["default_language"]) and args.dir:
        dedup_one(lang["short"])