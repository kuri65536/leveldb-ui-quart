debug:=
venv:=./venv/bin/
uipy := ui.min.js

ifeq (x$(debug),x1)
  uipy := ui.js
else
  uipy := ui.min.js
endif

launch: build
	$(venv)python main.py

build: download static/ui.min.js

setup:
	# python3.6 -m venv venv
	$(venv)pip install quart
	$(venv)pip install leveldb
	$(venv)pip install markdown

setup-devel:
	$(venv)pip install transcrypt

download: static/jquery.min.js

static/jquery.min.js:
	wget -o $@ https://code.jquery.com/jquery-3.3.1.min.js

ifeq (x$(debug),x1)
static/ui.min.js: ui.py jsutils.py connections.py configs.py
	$(venv)transcrypt $<
	cp __javascript__/$(uipy) $@
else
static/ui.min.js:
	echo this is release, do not compile ui.min.js...
endif

