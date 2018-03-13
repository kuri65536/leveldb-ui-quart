# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import Dict, Iterable, Iterator, Optional, Text, Tuple
import json
from leveldb import LevelDB
from quart import Quart, abort, render_template, request

Dict, Iterable, Iterator, Optional, Text, Tuple
app = Quart(__name__)
db = None  # type: Optional[LevelDB]


@app.route('/conn.local')
async def conn_local():
    # type: () -> Text
    global db
    path = request.args.get("dir")
    path = path.replace("%2F", "/")
    db = LevelDB(path, create_if_missing=True)
    ret = dict(key_encoding="utf-8",
               val_encoding="json",
               cache_size=1,
               create_if_missing=True,
               error_if_exists=False,
               compression=False)
    print("LevelDB opened: {}".format(db))
    return json.dumps(ret)


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
    try:
        ___v = json.loads(v)
        __v = json.dumps(___v)
    except:
        __v = v
    _k = k.encode("utf-8")  # TODO: encoding by settings
    _v = __v.encode("utf-8")  # TODO: encoding by settings
    db.Put(_k, _v)

    ret = dict(k=k, v=__v)
    print("LevelDB put: {}".format(ret))
    return json.dumps(ret)


@app.route('/query_part')
async def query_part():  # route {{{1
    # type: () -> bytes
    '''TODO: hold iterator, return the token, continue iterator with token.
    '''
    global db
    if db is None:
        abort(404)
        return ""
    u = request.args.get("u", "")
    l = request.args.get("l", "")
    n = request.args.get("n", "100")

    if l == "":
        l = chr(255)
    try:
        _n = int(n)
    except ValueError:
        _n = 100

    ret = ('{"u": "' + u + '", "l": "' + l + '", "n":' + str(_n) +
           ', "records": [')
    i = 0
    for k in db.RangeIter(u.encode("utf-8"), l.encode("utf-8"),
                          include_value=False):
        i += 1
        if i > _n:
            continue
        if i > 1:
            ret += ", "
        ret += '{"key": "' + k.decode("utf-8") + '"}'
    ret += "]}"
    print(ret)
    return ret.encode("utf-8")


@app.route('/query_stream')
async def query_stream():  # route {{{1
    # type: () -> Tuple[Iterable[bytes], int, Dict[Text, Text]]
    global db
    if db is None:
        abort(404)
        return ""
    u = request.args.get("u", "")
    l = request.args.get("l", "")
    n = request.args.get("n", "100")

    if l == "":
        l = chr(255)
    try:
        _n = int(n)
    except ValueError:
        _n = 100

    async def stream(u, l, n):
        # type: (Text, Text, int) -> Iterable[byte]
        ret = ('{"u": "' + u + '", "l": "' + l + '", "n":' + str(n) +
               ', "records": [')
        yield ret.encode("utf-8")

        i = 0
        for k, v in db.RangeIter(u.encode("utf-8"), l.encode("utf-8")):
            i += 1
            if i > n:
                break
            if i > 1:
                yield ",".encode("utf-8")
            ret = '{"key": "' + k.decode("utf-8") + '", "val": '
            try:
                _v = json.loads(v.decode("utf-8"))  # TODO: encode by settings
                ret += _v.dumps()
            except json.decoder.JSONDecodeError:
                _v = v.decode("utf-8")
                ret += '"{}"'.format(_v)
            ret += "}"
            yield ret.encode("utf-8")
        yield "]}".encode("utf-8")
    return stream(u, l, _n), 200, {'X-Something': 'value'}


@app.route('/')
async def root():  # {{{1
    # type: () -> Text
    return await render_template("index.html")


@app.route('/readme')
async def readme():  # {{{1
    # type: () -> Text
    import markdown
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
