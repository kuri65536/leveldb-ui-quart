release:=

ifeq (x$(release),x)
  uipy := ui.js
else
  uipy := ui.min.js
endif

build: download static/ui.min.js

setup:
	python3.6 -m venv venv
	./venv/bin/pip install quart
	./venv/bin/pip install leveldb
	./venv/bin/pip install transcrypt
	./venv/bin/pip install markdown

download: static/jquery.min.js

static/jquery.min.js:
	wget -O $@ https://code.jquery.com/jquery-3.3.1.min.js

static/ui.min.js: ui.py jsutils.py connections.py configs.py
	./venv/bin/transcrypt $<
	cp __javascript__/$(uipy) $@

