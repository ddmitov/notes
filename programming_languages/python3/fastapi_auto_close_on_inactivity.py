#! /usr/bin/env python3

import datetime
import os
import signal
import threading
import time

from fastapi import FastAPI
import uvicorn

PERIODIC_CHECK_SECONDS = 3
MAXIMAL_INACTIVITY_SECONDS = 30

app = FastAPI()
last_activity = time.time()


@app.get('/')
def root():
    global last_activity
    last_activity = time.time()

    return {'message': 'Hello, World!'}


def periodic_check():
    global last_activity

    thread = threading.Timer(
        PERIODIC_CHECK_SECONDS,
        periodic_check
    )

    thread.daemon = True

    thread.start()

    if time.time() - last_activity > MAXIMAL_INACTIVITY_SECONDS:
        print(f'Initiating shutdown sequence at: {datetime.datetime.now()}')

        # os.system("pkill -f 'uvicorn main:app'")
        os.kill(os.getpid(), signal.SIGINT)
    else:
        print(f'Activity check at: {datetime.datetime.now()}')


if __name__ == '__main__':
    periodic_check()

    try:
        uvicorn.run(
            app,
            host='127.0.0.1',
            port=8000
        )
    except (KeyboardInterrupt, SystemExit):
        print('\n')

        exit(0)
