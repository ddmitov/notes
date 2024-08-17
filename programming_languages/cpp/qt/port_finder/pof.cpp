
// https://stackoverflow.com/questions/24778939/get-next-open-tcp-port-in-windows

#include <QCoreApplication>
#include <QTcpSocket>
#include <QDebug>

int main (int argc, char **argv)
{
    QCoreApplication application (argc, argv);

    qint16 startPort = 8080;
    qint16 endPort = 9090;
    qint16 firstAvailablePort = startPort;

    QTcpSocket *socket = new QTcpSocket();

    while(!socket->bind(firstAvailablePort, QAbstractSocket::DontShareAddress)) {
        if (firstAvailablePort < endPort) {
            firstAvailablePort++;
        }
    }

    socket->close();
    socket->deleteLater();

    qDebug() << " ";
    qDebug() << "Port Finder, v.0.1";
    qDebug() << "First available port:" << firstAvailablePort;
    qDebug() << " ";
    exit(0);

    return application.exec();
}

