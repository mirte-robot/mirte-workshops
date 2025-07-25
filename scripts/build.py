import json, os, shutil, argparse

parser = argparse.ArgumentParser(description="Build script")
parser.add_argument('--dir', required=True, help='Directory to the workshop directory (located in docs/workshops) to build')
parser.add_argument('--lang', required=False, help='Language to build (default: all)')
args = parser.parse_args()

# Add symlinks to all the modules
cwd = os.getcwd()
os.system(f'ln -s {cwd}/docs/modules ./docs/{args.dir}')
os.system(f'ln -s {cwd}/_static ./docs/{args.dir}')
os.system(f'ln -s {cwd}/_templates ./docs/{args.dir}')
os.system(f'ln -s {cwd}/conf.py ./docs/{args.dir}')
#TODO: include conf.py locally so author can be overridden


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
    os.system(f'sphinx-build "./docs/{args.dir}" "_build/html/{lang["short"]}/{dir}" -t lang_{lang["short"]}')

shutil.copyfile('scripts/index.html', '_build/html/index.html')

# Remove symlink to all modules
os.system(f'rm ./docs/{args.dir}/modules')
os.system(f'rm ./docs/{args.dir}/_static')
os.system(f'rm ./docs/{args.dir}/_templates')
os.system(f'rm ./docs/{args.dir}/conf.py')
