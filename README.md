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
Bitcoin **< 1FTBAUaVdeGG9EPsGMD5j2SW8QHNc5HzjT >**
or Ether **< 0xd7Dc5cd13BD7636664D6bf0Ee8424CFaF6b2FA8f >** .

![Donate Bitcoin](data:image/png;base64,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)
![Donate Ether](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAACWCAYAAAA8AXHiAAAEqklEQVR4nO3TQZLkMAhE0br/pac3vZoulYWSBOz6RHgnKRF6fr1er3+TPrUcZ2ZnO2bU/W5vvvYGgAUsYGVkAwtYlmxgAcuS/bWwqmoarMje7AdXa9o7AutwL7A+ZwPrcC+wPmcD63AvsD5nA+twL7A+Z2/D2h1QZHCO7M562izFM2c1pGZ31tNmCSxgjcsGVmI9bZbAAta4bGAl1tNm+bWwlFKhZs9Cvfe0dwQWsIAFLGABC1izGlIHvFvAAlZZTiRbqWyAqzOVbGABa3mmkg0sYC3PVLKBBazlmUo2sIC1PFPJLoPlqCpYypmO3h017R2BBSxLNrCAZckGFrAs2cACliX7LazOL9D49trsdXfJbv7aG3j043ZmA+vBj9uZDawHP25nNrAe/Lid2a3f2y6HVWTAypmOPrPXZfRZUbfoEljAshSwgGUpYAHLUsC6ISz1ktlfsHl7dtV+taa9D7CABSx3T2qGsl+tae8DLGABy92TmqHsV2va+wALWB5Y05qMXEa6eBFqpSp/ivRZZDcELGABC1jAUtdm7o3MSClgAQtY2bB29yvrQhcqGHrlz1NRljuqQbv7lXXqQNQ7AgtYwDooYB32qd4RWMAC1kG1wnI0pWbv1rQzHfiVbPW9365TNkcvD6zYXmABC1j/r1M2Ry8PrNheYAELWH/X1QQpl1RhVp2XXVWwHAUsYKX3/ZsDLGDlF7CAld73bw6wgJVf27Acj2G60HGPndlqP+o77mYHzgAWsIB1NGBlXVU2sIBlyQYWsCzZj4OlDCgSrjQ5se7QZ2ePwDqsO/QJLGBZCljAshSwgGUpYAHLUo+DJTXUiHp3nXpmJKfqPrt9b+comx0FLGBZCljAshSwgGUpYD0YVqShzkt2Zj8Jm5r99lODlAsBK34XYAErtE7psTsbWInZ0x63MxtYidnTHrcze/FpD6k0WnjJVGxVOY75Ot4bWMAC1kbjwDqYL7CuGwfWwXyBdd04sA7mOw6WOkz1zM7BKb13VtWPssgG1kkB6zIbWCcFrMtsYJ0UsC6zgXVSwLrM1mApl1T2TnxIpaoQqDML5ABrQgELWJYCFrAsBSxgWeprYamVPaDIJbP7UR8ye2/3t+gdWMAC1uWZFf0AC1iWfoAFLEs/wAKWpR9gbfS+/RKNpT5GZU8ViCr6ls+UuiwqYAHLUsAClqWABSxLAeuGsJQBOT61lDOrenfkZAOO9L5Y148JWMACFrCANeHBq3KABazvhVVV2cNwYVV6cty7q+/IfmAl9g4sYFl6BxawLL0DC1iW3oF1AMvxuFXZDmwV/TjuXZgNrJO6yeMCC1g19waWecBq3eRxgQWsmnsDayNbqSqAFT2q8zX1BCxgWXoCFrAsPQELWJaegAUsS0/AOjnvrv2o7xjIARawgHW7h5zWD7A2spUCFrCAlbgfWBvZSgFrCCxHTRtmVVU9rpId2b9YN2vAjv3AimdH9i/WzRqwYz+w4tmR/Yt1swbs2A+seHZk/2LdrAE79gMrnh3Zv1iXf8nsATn2K+uiPVWgrpp5oJ9+TMACFrAOegLWgE8d2u5+ZV20J2AN+NSh7e5X1kV7+kZYP9HC0TVFFRz3AAAAAElFTkSuQmCC)


<!--
 vi: ft=markdown:et:ts=4:nowrap:fdm=marker
 -->
