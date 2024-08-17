
TEMPLATE = app
TARGET = pof

DEPENDPATH += .
VERSION = 0.1

# Qt5 specific settings:
greaterThan (QT_MAJOR_VERSION, 4) {
  DEFINES += HAVE_QT5
}

QT += network
SOURCES += pof.cpp
