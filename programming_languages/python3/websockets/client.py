#!/usr/bin/env python3

import asyncio
import websockets


async def receiver():
    while True:
        uri = 'ws://localhost:5678'

        async with websockets.connect(uri) as websocket:
            message = await websocket.recv()
            print(message)


loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(receiver())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print('\n')
    loop.close()
