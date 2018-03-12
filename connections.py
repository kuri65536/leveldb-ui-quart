# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
import configs as cfg
import jsutils

__pragma__('skip')      # noqa
if False:
    jq = None
    this = alert = document = window = None
    Math = parseFloat = isFinite = isNaN = None
    JSON = RegExp = None
    __pragma__ = None
    jump_js     # use by html
__pragma__('noskip')
__pragma__('alias', 'jq', '$')

host_text = port_text = ""


def conn_failed():
    pass


def conn_succeed(dat):
    # type: (Any) -> None
    jq("#keyEncoding").text(dat.key_encoding)
    jq("#valueEncoding").text(dat.val_encoding)
    jq("#compression").prop("checked", dat.compression)
    jq("#cacheSize").text(dat.cache_size)
    jq("#createIfMissing").prop("checked", dat.create_if_missing)
    jq("#errorIfExists").prop("checked", dat.error_if_exists)
    jq("#host").text(host_text)
    jq("#port").text(port_text)


def conn_local():
    # type: () -> bool
    global host_text
    host_text = path = jq(".path").val()
    port_text = ""
    jsutils.ajax(cfg.url("conn.local?dir=" + path)) \
        .then(conn_succeed, conn_failed)
    return True


def conn_network():
    # type: () -> bool
    global host_text
    global port_text
    host_text = url = jq(".host").val();
    port_text = url.split(":")[-1]
    jsutils.ajax(cfg.url("conn.network?url=" + url)) \
        .then(conn_succeed, conn_failed)
    return True


def put_succeed(dat):  # {{{1
    # type: (Any) -> None
    pass


def put_failed():  # {{{1
    # type: () -> None
    pass  # TODO: error handling


def put_clear():  # {{{1
    # type: () -> bool
    ke = jq("#keyEncoding").val()
    ve = jq("#valEncoding").val()
    jq(".keyEncoding").val(ke)
    jq(".valEncoding").val(ve)
    return True


def put_save():  # {{{1
    # type: () -> bool
    k = jq(".key textarea").val()
    v = jq(".value textarea").val()
    jsutils.ajax("/put?key=" + k + "&val=" + v) \
        .then(put_succeed, put_failed)
    return True


def init():
    # type: () -> bool

    # hide sections
    jq(".openDirectory").on("click", conn_local)
    jq(".openConnection").on("click", conn_network)
    jq(".clear").on("click", put_clear)
    jq(".save").on("click", put_save)
    return False

# vi: ft=python:et:ts=4:nowrap:fdm=marker
