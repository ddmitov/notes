#!/usr/bin/env python3

import asyncio
import datetime
import websockets


async def timer(websocket, path):
    while True:
        await asyncio.sleep(1)

        now = datetime.datetime.utcnow().isoformat() + 'Z'

        await websocket.send(now)


start_server = websockets.serve(timer, 'localhost', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
