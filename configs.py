# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
url_host = "http://localhost:5000"


def url(*text):
    ret = url_host
    for i in text:
        i = i.replace("/", "%2F")
        ret += "/" + i
    return ret

