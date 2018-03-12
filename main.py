# Copyright (c) 2018, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from quart import Quart, render_template

app = Quart(__name__)

@app.route('/')
async def root():
    return await render_template("index.html")

app.run()

