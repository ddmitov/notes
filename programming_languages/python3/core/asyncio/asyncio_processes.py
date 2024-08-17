#!/usr/bin/python3

import asyncio


async def run_command(*args):
    process = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    return stdout.decode().strip()


loop = asyncio.get_event_loop()

commands = asyncio.gather(
    run_command('uname'),
    run_command('date')
)

uname, date = loop.run_until_complete(commands)

print('uname: {}'.format(uname))
print('date: {}'.format(date))

loop.close()
