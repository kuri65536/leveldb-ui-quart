# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import List, Text

List, Text

url_host = "http://localhost:5000"

key_encoding = "utf-8"
val_encoding = "json"
cache_size = 1
compression = True
create_if_missing = True
error_if_exists = False


def url(*text):
    # type: (List[Text]) -> Text
    ret = url_host
    for i in text:
        i = i.replace("/", "%2F")
        ret += "/" + i
    return ret

# vi: ft=python:et:ts=4:nowrap:fdm=marker
