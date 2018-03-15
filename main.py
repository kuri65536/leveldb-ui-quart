# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import (Any, AsyncGenerator, Dict,
                    Iterable, Iterator, Optional, Text, Tuple)
import pickle
import json
from leveldb import LevelDB  # type: ignore
from quart import Quart, abort, render_template, request  # type: ignore

import configs as cfg

Any, AsyncGenerator, Dict, Iterable, Iterator, Optional, Text, Tuple
app = Quart(__name__)
db = None  # type: Optional[LevelDB]


def json_dbcfg():  # {{{1
    # type: () -> Text
    ret = dict(key_encoding=cfg.key_encoding,
               val_encoding=cfg.val_encoding,
               compression=cfg.compression,
               cache_size=cfg.cache_size,
               create_if_missing=cfg.create_if_missing,
               error_if_exists=cfg.error_if_exists)
    return json.dumps(ret)


def valdec_text(src):  # {{{1
    # type: (bytes) -> Text
    if cfg.val_encoding.lower().endswith("latin-1"):
        enc = "latin-1"
    else:
        enc = "utf-8"
    return src.decode(enc)


def valdec_bytes(src):  # {{{1
    # type: (bytes) -> Any
    if cfg.val_encoding.lower().startswith("json"):
        _ret = valdec_text(src)
        try:
            ret = json.loads(_ret)
        except json.decoder.JSONDecodeError:
            ret = _ret
        return ret
    elif cfg.val_encoding.lower().startswith("raw"):
        pass
    elif cfg.val_encoding.lower().startswith("pickle"):
        ret = pickle.loads(src)
        return ret
    return valdec_text(src)


def valenc_text(src):  # {{{1
    # type: (Text) -> bytes
    if cfg.val_encoding.lower().endswith("latin-1"):
        enc = "latin-1"
    else:
        enc = "utf-8"
    return src.encode(enc)


def valenc_raw(src):  # {{{1
    # type: (Text) -> bytes
    return valenc_text(src)


def valenc_json(src):  # {{{1
    # type: (Text) -> bytes
    try:
        _src = json.loads(src)
    except:
        _src = src
    return valenc_text(_src)


def valenc_pickle(src):  # {{{1
    # type: (Text) -> bytes
    try:
        dat = valenc_text(src)
        return pickle.pickle(dat)  # type: ignore
    except:
        pass
    return valenc_text(src)


@app.route('/conn.local')
async def conn_local():
    # type: () -> Text
    global db
    path = request.args.get("dir")
    path = path.replace("%2F", "/")
    db = LevelDB(path, cfg.create_if_missing)
    print("LevelDB opened: {}".format(db))
    return json_dbcfg()


@app.route('/conn.network')
async def conn_network():
    # type: () -> Text
    path = request.args.get("url")
    if path == "":
        abort(404)
    # TODO: implement, I do not have server of LevelDB.
    ret = dict(key_encoding="utf-8",
               val_encoding="json",
               cache_size=2,
               create_if_missing=True,
               error_if_exists=False,
               compression=False)
    print("LevelDB opened(as network): ...")
    return json.dumps(ret)


@app.route('/settings')
async def settings():  # route {{{1
    # type: () -> Text
    if request.args.get("query", "false") == "true":
        pass
    else:
        _dat = request.args.get("data", "")
        dat = json.loads(_dat)
        ke = dat["key_encoding"]
        ve = dat["val_encoding"]
        cs = dat["cache_size"]
        cm = dat["compression"]
        ci = dat["create_if_missing"]
        ei = dat["error_if_exists"]
        if "" in (ke, ve, cs, cm, ci, ei):
            abort(404)
            return ""
        cm = True if cm == "on" else False
        ci = True if ci == "on" else False
        ei = True if ei == "on" else False
        # TODO: error check more strictly
        cfg.key_encoding = ke
        cfg.val_encoding = ve
        cfg.compression = cm
        cfg.cache_size = cs
        cfg.create_if_missing = ci
        cfg.error_if_exists = ei
    return json_dbcfg()


@app.route('/get')
async def get_record():  # route {{{1
    # type: () -> Text
    global db
    if db is None:
        abort(404)
        return ""
    k = request.args.get("key", "")
    if k == "":
        abort(404)
        return ""
    _k = k.encode(cfg.key_encoding)
    try:
        v = db.Get(_k)
    except KeyError:
        abort(404)
        return ""

    _v = valdec_bytes(v)
    ret = dict(k=k, v=str(_v))
    print("LevelDB put: {}".format(ret))
    return json.dumps(ret)


@app.route('/put')
async def put_record():  # route {{{1
    # type: () -> Text
    global db
    if db is None:
        abort(404)
        return ""
    k = request.args.get("key", "")
    v = request.args.get("val", "")
    if k == "" or v == "":
        abort(404)
        return ""
    if cfg.val_encoding.lower().startswith("json"):
        _v = valenc_json(v)
    elif cfg.val_encoding.lower().startswith("pickle"):
        _v = valenc_pickle(v)
    else:
        _v = valenc_text(v)
    _k = k.encode(cfg.key_encoding)
    db.Put(_k, _v)

    ret = dict(k=k, v=valdec_text(_v))
    print("LevelDB put: {}".format(ret))
    return json.dumps(ret)


@app.route('/query_part')
async def query_part():  # route {{{1
    # type: () -> Text
    '''TODO: hold iterator, return the token, continue iterator with token.
    '''
    global db
    if db is None:
        abort(404)
        return ""
    u = str(request.args.get("u", ""))
    l = str(request.args.get("l", ""))
    n = request.args.get("n", "100")

    if l == "":
        l = chr(255)
    try:
        _n = int(n)
    except ValueError:
        _n = 100

    ret = '{"u": "' + u + '", "l": "' + l + '", "n":' + str(_n) + \
          ', "records": ['
    i = 0
    _u = u.encode(cfg.key_encoding)
    _l = l.encode(cfg.key_encoding)
    for k in db.RangeIter(_u, _l, include_value=False):
        assert isinstance(k, bytearray), "??? key type is {}".format(type(k))
        i += 1
        if i > _n:
            continue
        if i > 1:
            ret += ", "
        ret += '{"key": "' + k.decode(cfg.key_encoding) + '"}'
    ret += "]}"
    print(ret)
    return ret


@app.route('/query_stream')
async def query_stream():  # route {{{1
    # type: () -> Tuple[AsyncGenerator[bytes, None], int, Dict[Text, Text]]
    global db
    u = str(request.args.get("u", ""))
    l = str(request.args.get("l", ""))
    _n = request.args.get("n", "100")

    if l == "":
        l = chr(255)
    try:
        n = int(_n)
    except ValueError:
        n = 100

    async def stream(u, l, n):
        # type: (Text, Text, int) -> AsyncGenerator[bytes, None]
        if db is None:
            return
        ret = ('{"u": "' + u + '", "l": "' + l + '", "n":' + str(n) +
               ', "records": [')
        yield ret.encode("utf-8")

        i = 0
        _u = u.encode(cfg.key_encoding)
        _l = l.encode(cfg.key_encoding)
        for k, v in db.RangeIter(_u, _l):
            i += 1
            if i > n:
                break
            if i > 1:
                yield ",".encode("utf-8")
            ret = '{"key": "' + k.decode(cfg.key_encoding) + '", "val": '
            _v = valdec_bytes(v)
            ret += '"{}"}'.format(str(_v))
            yield ret.encode("utf-8")
        yield "]}".encode("utf-8")

    ret = 200 if db is not None else 500
    return stream(u, l, n), ret, {'X-Something': 'value'}


@app.route('/')
async def root():  # type: ignore  # mypy error: syntax error ? {{{1
    return await render_template("index.html")


@app.route('/readme')
async def readme():  # {{{1
    # type: () -> Text
    import markdown  # type: ignore  # no type stub
    ret = ""
    with open("templates/index.html", "rt") as fp:
        for line in fp:
            ret += line
            if "<body" in line:
                break
    with open("README.md", "rt") as fp:
        src = fp.read()  # TODO: await?
    ret += markdown.markdown(src)  # TODO: await?
    ret += "</body> </html>"
    return ret


app.run()
# vi: ft=python:et:ts=4:nowrap:fdm=marker
