# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import Any, Callable, Text
import configs as cfg
from jsutils import jq, json, urlencode
import jsutils  # type: ignore

Any, Callable, Text

# __pragma__('skip')
if False:
    this = Any
    alert = document = window = None
    Math = parseFloat = isFinite = isNaN = None
    RegExp = None
# __pragma__('noskip')

host_text = port_text = ""


def conn_failed():
    # type: () -> None
    pass


def conn_succeed(_dat):  # {{{1
    # type: (Any) -> None
    dat = json.parse(_dat)
    jq(".keyEncoding").val(dat.key_encoding)
    jq(".valEncoding").val(dat.val_encoding)
    jq("#compression").prop("checked", dat.compression)
    jq("#cacheSize").val(dat.cache_size)
    jq("#createIfMissing").prop("checked", dat.create_if_missing)
    jq("#errorIfExists").prop("checked", dat.error_if_exists)
    if host_text is not None:
        jq("#host").val(host_text)
    if port_text is not None:
        jq("#port").val(port_text)


def conn_local():
    # type: () -> bool
    global host_text
    host_text = path = jq(".path").val()
    # port_text = ""
    jsutils.ajax(cfg.url("conn.local?dir=" + path)) \
        .then(conn_succeed, conn_failed)
    return True


def conn_network():
    # type: () -> bool
    global host_text
    global port_text
    host_text = url = jq(".host").val()
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


def get_succeed(dat):  # {{{1
    # type: (Text) -> bool
    _dat = json.parse(dat)
    jq("#value textarea").val(_dat.v)
    return False


def get_failed():  # {{{1
    # type: () -> bool
    'TODO: show failure messages to user'
    return False


def get_record(ev):  # {{{1
    # type: (Any) -> bool
    _key = jq(this).text()  # type: ignore
    key = urlencode(_key)
    jsutils.ajax("/get?key=" + key) \
        .then(get_succeed, get_failed)
    return False


def query_succeed(_dat):  # {{{1
    # type: (Any) -> None
    try:
        dat = json.parse(_dat)
    except:
        return
    jq(".keys select").empty()
    for i in dat.records:
        cnt = '<option class="key">{}</option>'.format(i.key)
        jq(".keys select").append(cnt)
    jq(".key").on("dblclick", get_record)
    # for i in dat.records:
    #     cnt = ('<li><input id="tree-{0}" type="checkbox" value="{0}" />' +
    #            '<label for="tree-{0}">{0}</label></li>').format(i.key)
    #     jq(".root").append(cnt)


def query_failed():  # {{{1
    # type: () -> None
    pass  # TODO: error handling


def query_sublevels():  # {{{1
    # type: () -> bool
    u = jq(".upperbound").val()
    l = jq(".lowerbound").val()
    n = jq(".limit").val()
    r = "&r=on" if jq(".reverse").val() == "up" else ""
    n = "&n=" + n if n != "" else ""
    jsutils.ajax("/query_part?u=" + u + "&l=" + l + n + r)  \
        .then(query_succeed, query_failed)
    return True


def query_toggle_rev():  # {{{1
    # type: () -> bool
    btn = jq(".reverse")
    if btn.val() == "down":
        btn.val("up")
    else:
        btn.val("down")
    return True


def query_enable_select(ev):  # {{{1
    # type: (Any) -> bool
    # jq(ev.target).prev().val("").focus().trigger("input")
    # jq(ev.target).prev().val("").focus().trigger("click")
    jq(ev.target).prev().val("").focus().click()
    return True


def query_enable_dummy(ev):
    # tyype: (Any) -> bool
    return False


def settings_apply():  # {{{1
    # type: () -> bool
    ke = jq("#settings_keyenc").val()
    ve = jq("#settings_valenc").val()
    cs = jq("#cacheSize").val()
    cm = jq("#compression").val()
    ci = jq("#createIfMissing").val()
    ei = jq("#errorIfExists").val()
    _dat = json.stringify(dict(key_encoding=ke, val_encoding=ve,
                               compression=cm, cache_size=cs,
                               create_if_missing=ci,
                               error_if_exists=ei))
    dat = urlencode(_dat)
    jsutils.ajax("/settings?save=true&data=" + dat)  \
        .then(conn_succeed, conn_failed)
    return True


def settings_cancel():  # {{{1
    # type: () -> bool
    jsutils.ajax("/settings?query=true") \
        .then(conn_succeed, conn_failed)
    return True


def init():  # {{{1
    # type: () -> bool

    # menus
    btn = jq("#keyenc_list")
    for i in cfg.key_encodings:
        opt = '<option value="{0}">{0}</option>'.format(i)
        btn.append(opt)
    btn = jq("#valenc_list")
    for i in cfg.val_encodings:
        opt = '<option value="{0}">{0}</option>'.format(i)
        btn.append(opt)
    jq(".keyEncoding").on("click", query_enable_dummy)
    jq(".valEncoding").on("click", query_enable_dummy)

    # events
    jq(".openDirectory").on("click", conn_local)
    jq(".openConnection").on("click", conn_network)
    jq(".clear").on("click", put_clear)
    jq(".save").on("click", put_save)
    jq(".sublevels").on("click", query_sublevels)
    jq(".reverse").on("click", query_toggle_rev)
    jq("#settings_apply").on("click", settings_apply)
    jq("#settings_cancel").on("click", settings_cancel)
    return False

# vi: ft=python:et:ts=4:nowrap:fdm=marker
