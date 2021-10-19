SHELL=/bin/bash

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = ../.


## help: Display list of commands (from gazr.io)
.PHONY: help
help: Makefile
	@sed -n 's|^##||p' $< | column -t -s ':' | sed -e 's|^| |'

.PHONY: init
init:
	pipenv install --dev

## html: build the docs as html to serve on Github Pages
.PHONY: html
html:
	pipenv run $(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) || true
	mv $(BUILDDIR)/html/_static/* $(BUILDDIR)/html/static/ || true
	sed -i 's/_static/static/' $(BUILDDIR)/html/*.html

## livehtml: Build the doc as html with live reloading for local purpose
.PHONY: livehtml
livehtml:
	pipenv run sphinx-autobuild $(SOURCEDIR) $(BUILDDIR)/html
	mv $(BUILDDIR)/html/_static $(BUILDDIR)/html/static
	sed -i '' 's/_static/static/' $(BUILDDIR)/html/*.html

## autodoc: Autogenerate module documentation skeleton
.PHONY: autodoc
autodoc:
	pipenv run sphinx-apidoc -o $(SOURCEDIR)/api_reference ../encartaexport
