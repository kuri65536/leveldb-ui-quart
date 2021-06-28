LevelDB UI by python
==============================================
this is [levelui](https://github.com/0x00A/levelui) clone
by python with [Quart framework](https://gitlab.com/pgjones/quart) .

I did not use levelui actually, just see screenshots
and made this program.


License
------------------
my codes were licensed with Mozzila Public License 2.0.

some of levelui works were licensed with MIT license.


Installation
------------------

```
$ git clone https://github.com/who/...
$ cd ...
$ python -m venv venv  # or virtualenv, as you prefered
$ make setup           # install quart leveldb markdown
$ make launch
```


Screenshots
------------------
### Database Open

![open db](https://user-images.githubusercontent.com/11357613/37623173-1be24e8c-2c07-11e8-811c-930c433cf7c9.png)

### Query

![query flat](https://user-images.githubusercontent.com/11357613/37623184-2403a070-2c07-11e8-89a3-f4ffbf0f67fe.png)

![query fold](https://user-images.githubusercontent.com/11357613/37623187-25a82b4e-2c07-11e8-82f4-77b54bf3a655.png)

### Put

![put](https://user-images.githubusercontent.com/11357613/37623189-27bdee6e-2c07-11e8-8a23-a5942f712221.png)

### Settings

![settings](https://user-images.githubusercontent.com/11357613/37623193-29857988-2c07-11e8-830c-9caf548941d1.png)


TODO
------------------
### 2.0.0
- beautiful markdown CSS
- refactor design
- save settings to db
- network db, (I don't known how do I open it?)
- db query with streaming.

### 1.1.0
- close and re-poen database
- react open database
- react put record
- value encode by python-pickle (decoding?)


Change
------------------
### 1.0.0
- readme: take screenshots
- classify list-uped keys.

### 0.3.0
- key encode from menu
- value encode from menu
- enable to reverse in query

### 0.2.0
- value encode by settings
- key encode by settings
- serve README.md as /readme

### 0.1.0
- change framework to [Quart framework](https://gitlab.com/pgjones/quart)
- change language to python
- setup script in Makefile:setup

  - use leveldb
  - use transcrypt


Donate
------------------
If you are feel to nice for this software,
please donation to my

- Bitcoin **| 19AyoXxhm8nzgcxgbiXNPkiqNASfc999gJ |**
- Ether **| 0x3a822c36cd5184f9ff162c7a55709f3d6d861608 |**
- or librapay, I'm glad from smaller (about $1)

<!--
 vi: ft=markdown:et:ts=4:nowrap:fdm=marker
 -->
