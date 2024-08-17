#!/usr/bin/env python3

from flask import Flask, render_template
from flask_cors import CORS

app = Flask(
    __name__,
    template_folder = 'static/html'
)

CORS(app)


@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000
    )
