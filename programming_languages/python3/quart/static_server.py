#!/usr/bin/env python3

from quart import Quart
from quart import render_template
from quart_cors import cors

app = Quart(__name__)
app = cors(app, allow_origin="*")


@app.route('/', methods=['GET'])
async def root():
    return await render_template('index.html')


if __name__ == '__main__':
    try:
        app.run(
            host='localhost',
            port=5000
        )
    except (KeyboardInterrupt, SystemExit):
        print('\n')
        exit(0)
