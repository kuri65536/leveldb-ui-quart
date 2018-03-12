release:=
venv:=./venv/bin/

ifeq (x$(release),x)
  uipy := ui.js
else
  uipy := ui.min.js
endif

launch: build
	$(venv)python3 main.py

build: download static/ui.min.js

setup:
	python3.6 -m venv venv
	$(venv)pip install quart
	$(venv)pip install leveldb
	$(venv)pip install transcrypt
	$(venv)pip install markdown

download: static/jquery.min.js

static/jquery.min.js:
	wget -O $@ https://code.jquery.com/jquery-3.3.1.min.js

static/ui.min.js: ui.py jsutils.py connections.py configs.py
	$(venv)transcrypt $<
	cp __javascript__/$(uipy) $@

