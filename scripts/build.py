import json, os, shutil, argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Build script")
parser.add_argument('--dir', required=True, help='Directory to the workshop directory (located in docs/workshops) to build')
parser.add_argument('--lang', required=False, help='Language to build (default: all)')
args = parser.parse_args()

# Add symlinks to all the modules
cwd = os.getcwd()


# Cross-platform linkgin/copying of folders
# Windows dows not have symlinks (without admin)
def link_or_copy(src, dst):
    src_path = Path(src)
    dst_path = Path(dst)

    if dst_path.exists():
        if dst_path.is_dir():
            shutil.rmtree(dst_path)
        else:
            dst_path.unlink()

    if src_path.is_dir():
        shutil.copytree(src_path, dst_path)
    else:
        shutil.copyfile(src_path, dst_path)

link_or_copy(f'{cwd}/docs/modules', f'./docs/{args.dir}/modules')
link_or_copy(f'{cwd}/_static',       f'./docs/{args.dir}/_static')
link_or_copy(f'{cwd}/_templates',    f'./docs/{args.dir}/_templates')
link_or_copy(f'{cwd}/conf.py',       f'./docs/{args.dir}/conf.py')
#TODO: include conf.py locally so author can be overridden (or have conf read another conf.py/conf.json)


# Open the articles.json file
data = {}
if (not args.lang):
    with open('_static/js/articles.json') as file:
        # Parse the JSON data
        data = json.load(file)
else:
    data['languages'] = [{'short': args.lang}]

# the homepage should be placed at {lang}/ instead of {lang}/homepage
dir = args.dir if args.dir != "homepage" else ""

for lang in data['languages']:
    os.chdir(f'./docs/{args.dir}')
    found = any(f.suffixes == [f'.{lang["short"]}', '.rst'] for f in Path(".").rglob('*'))
    if (found):
        os.system(f'sphinx-build "." "{cwd}/_build/html/{lang["short"]}/{dir}" -t lang_{lang["short"]}')
    os.chdir(f'{cwd}')


def remove_path(path):
    p = Path(path)
    if p.exists():
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()
            
# Remove symlink to all modules
remove_path(f'./docs/{args.dir}/modules')
remove_path(f'./docs/{args.dir}/_static')
remove_path(f'./docs/{args.dir}/_templates')
remove_path(f'./docs/{args.dir}/conf.py')
