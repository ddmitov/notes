#!/usr/bin/env python3.9

import asyncio
import datetime


async def to_do():
    while True:
        time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        print('')
        print(f'{time} - TO DO:')
        print('KEEP CALM AND KEEP LEARNING')
        print('KEEP CALM AND KEEP IMPROVING')

        await asyncio.sleep(1)


def main():
    loop = asyncio.get_event_loop()

    try:
        asyncio.ensure_future(to_do())
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        exit(0)


if __name__ == '__main__':
    main()
