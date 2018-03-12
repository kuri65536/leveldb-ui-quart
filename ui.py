# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
import connections

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


def section_activate():
    # type: () -> bool
    name = ""
    for i in jq(this).attr("class").split(" "):
        if i in ("active", "ss-icon"):
            continue
        name = i
        break
    else:
        return False
    jq("section").css("display", "none")
    jq("section." + i).css("display", "block")


def main():
    # type: () -> bool

    # hide sections
    jq("section").css("display", "none")
    jq("section.connections").css("display", "block")

    # active sections
    jq(".horizontal a").on("click", section_activate)

    connections.init()


jq(main);

