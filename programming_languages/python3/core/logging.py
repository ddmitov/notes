#!/usr/bin/env python

import logging

def get_logger():
    logging.basicConfig(
        # Possible logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL:
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
        filename='app.log',
        filemode='a'
    )

    logger = logging.getLogger()

    return logger


logger = get_logger()

log_message = ''

logger.info(f'Info: {log_message}')
logger.error(f'Error: {log_message}')
