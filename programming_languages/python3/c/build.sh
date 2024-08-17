#!/bin/sh

gcc snake.c -o snake -I /usr/include/python3.5m/ -lpython3.5m
python3-config --cflags
gcc -Wall snake.c -o snake -I/usr/include/python3.5m  -Wno-unused-result -Wsign-compare -g -fstack-protector-strong -Wformat -Werror=format-security -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -lpython3.5m
