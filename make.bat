@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=.
set BUILDDIR=_build

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help
if "%1" == "build_lang" goto build_lang
if "%1" == "build_all" goto build_all

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:build_lang
python3 scripts/build.py --dir=%2
python3 scripts/dedup.py --dir=%2
python3 scripts/create_pwa.py
goto end
@REM build_lang:
@REM 	python3 scripts/build.py --dir=$(DIR)
@REM 	python3 scripts/dedup.py --dir=$(DIR)
@REM 	python3 scripts/create_pwa.py
@REM # python will fail if not in venv

:build_all
set DIRS=workshops/pioneer_line_follow homepage workshops/assemble workshops/ros2_intro workshops/nlt
(for %%a in (%DIRS%) do (
   echo %%a
   call make.bat build_lang %%a
))
copy scripts\index.html _build\html\index.html
goto end
@REM build_all:
@REM 	@for dir in $(DIRS); do \
@REM 		$(MAKE) build_lang DIR=$$dir; \
@REM 	done
@REM 	cp scripts/index.html _build/html/index.html


:end
popd
