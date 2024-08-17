# Binary basics:
CONFIG += release
TEMPLATE = app
TARGET = downloader

# Network support:
QT = core network
CONFIG += console

# HTTPS support:
CONFIG += openssl-linked

SOURCES += main.cpp download-manager.cpp
HEADERS += download-manager.h

# Destination directory for the compiled binary:
DESTDIR = $$PWD/../

# Temporary folder:
MOC_DIR = tmp
OBJECTS_DIR = tmp
RCC_DIR = tmp
