# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import Any, Callable, Text, Union


Any, Callable, Text, Union


# __pragma__('skip')
if False:
    _jq = JSON = Any
    this = alert = document = window = None
    Math = parseFloat = isFinite = isNaN = None
    JSON = RegExp = None
    encodeURIComponent = Any
# __pragma__('noskip')
# __pragma__('alias', '_jq', '$')


def ajax(url):  # {{{1
    # type: (Text) -> Any
    dat = dict(url=url)
    return _jq.ajax(dat)  # type: ignore


def jq(arg):  # {{{1
    # type: (Union[Text, Callable[[], Any]]) -> Any
    return _jq(arg)  # type: ignore


def urlencode(src):  # {{{1
    # type: (Text) -> Text
    return encodeURIComponent(src)  # type: ignore


class json(object):  # {{{1
    @classmethod
    def stringify(cls, obj):  # {{{1
        # type: (Any) -> Text
        return JSON.stringify(obj)  # type: ignore

    @classmethod
    def parse(cls, src):  # {{{1
        # type: (Text) -> Any
        return JSON.parse(src)  # type: ignore

# vi: ft=python:et:ts=4:nowrap:fdm=marker
