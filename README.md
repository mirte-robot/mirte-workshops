# mirte-workshops

This repository contains the code for the MIRTE website on https://workshops.mirte.org.

## Build preparations

In order to build and run you need to have installed Python3.10+.

### Linux

```sh
$ python3 -m venv docs-env
$ source docs-env/bin/activate
(docs-env)$ pip install -r requirements.txt
```

### Windows

```sh
> python3 -m venv docs-env
> docs-env\Scripts\activate.bat
(docs-env)> pip install -r requirements.txt
```

## Build

```
(docs-env)$ make build_all
(docs-env)$ python3 -m http.server -d _build/html

# Open a browser to https://localhost:8000
``

## Language support

The command 'make build_lang' will invoke scripts/build.py. This will run sphinx-build for every language in the _static/js/articles.json file. /{lang.shortcode}/ for all except default, / for default language.
Then all the static and images folders are deleted from the non-default folders. All html files are rewritten to link to the original ones.

## Add language

Add it to _static/js/articles.json
Add all translations in the docs folder. Every article that is translated, is stored as {name}.{lang.shortcode}.rst. Just before compiling, they are copied to {name}.rst.
