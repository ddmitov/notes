/*
 Broadcast Address Finder, v. 0.1

 This program is free software;
 you can redistribute it and/or modify it under the terms of the
 GNU General Public License, as published by the Free Software Foundation;
 either version 3 of the License, or (at your option) any later version.
 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 Dimitar D. Mitov, 2014, ddmitov (at) yahoo (dot) com
*/

// http://www.qtcentre.org/threads/19583-How-To-Get-System-Network-Interface-List-in-using-qt4-5
// http://stackoverflow.com/questions/12927273/how-to-get-local-ip-address-of-a-computer-using-qt

#include <QCoreApplication>
#include <QtNetwork/QNetworkInterface>
#include <QDebug>

int main (int argc, char **argv)
{

    QCoreApplication application (argc, argv);

    qDebug() << " ";
    qDebug() << "Broadcast Address Finder, v. 0.1";
    qDebug() << " ";

    QList<QNetworkInterface> list = QNetworkInterface::allInterfaces();
    foreach (QNetworkInterface iface, list) {
        QList<QNetworkAddressEntry> interfaceEntries = iface.addressEntries();
        foreach (QNetworkAddressEntry entry, interfaceEntries) {
            if (entry.ip() != QHostAddress::LocalHost and
                    entry.broadcast().toString().length() > 0) {
                qDebug() << "MAC:" << iface.hardwareAddress();
                qDebug() << "Interface:" << iface.name();
                qDebug() << "IP address:" << entry.ip().toString();
                qDebug() << "Netmask:" << entry.netmask().toString();
                qDebug() << "Prefix length:" << entry.prefixLength();
                qDebug() << "Broadcast address:" << entry.broadcast().toString();
                qDebug() << " ";
            }
        }

    }

    exit(0);

    return application.exec();

}

