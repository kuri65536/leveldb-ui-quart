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
    jq("#keyEncoding").text(dat.key_encoding)
    jq("#valueEncoding").text(dat.val_encoding)
    jq("#compression").prop("checked", dat.compression)
    jq("#cacheSize").text(dat.cache_size)
    jq("#createIfMissing").prop("checked", dat.create_if_missing)
    jq("#errorIfExists").prop("checked", dat.error_if_exists)
    jq("#host").text(host_text)
    jq("#port").text(port_text)


def conn_local():
    global host_text
    host_text = path = jq(".path").text()
    port_text = ""
    jsutils.ajax(cfg.url("conn.local", path)) \
        .then(conn_succeed, conn_failed)


def conn_network():
    global host_text
    global port_text
    host_text = url = jq(".host").text();
    port_text = url.split(":")[-1]
    jsutils.ajax(cfg.url("conn.network", url)) \
        .then(conn_succeed, conn_failed)


def init():
    # type: () -> bool

    # hide sections
    jq(".openDirectory").on("click", conn_local)
    jq(".openConnection").on("click", conn_network)
    return False

