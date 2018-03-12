# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
import json
from leveldb import LevelDB
from quart import Quart, abort, render_template, request

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
async def put_record():  # {{{1
    # type: () -> Text
    global db
    if db is None:
        abort(404)
    k = request.args.get("key")
    v = request.args.get("val")
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


@app.route('/')
async def root():
    return await render_template("index.html")

app.run()
# vi: ft=python:et:ts=4:nowrap:fdm=marker
