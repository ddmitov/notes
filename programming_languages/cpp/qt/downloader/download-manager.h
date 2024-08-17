
#ifndef DOWNLOAD_MANAGER_H
#define DOWNLOAD_MANAGER_H

#include <QtNetwork>

class DownloadManager: public QObject
{
    Q_OBJECT

public slots:
    void sslErrors(const QList<QSslError> &sslErrors)
    {
        Q_UNUSED(sslErrors);
    }

    void downloadFinished(QNetworkReply *reply)
    {
        QUrl url = reply->url();
        if (reply->error()) {
            qDebug() << "Download failed:"
                     << url.toEncoded().constData();
            qDebug() << "Error string:"
                     << reply->errorString();
        } else {
            QString path = url.path();
            QString filename = QFileInfo(path).fileName();

            QFile file(filename);
            file.open(QFile::WriteOnly);
            file.write(reply->readAll());
            file.close();

            qDebug() << "Download successfull.";
        }

        reply->deleteLater();

        QCoreApplication::instance()->quit();
    }

private:
    QNetworkAccessManager manager;

public:
    DownloadManager(const QUrl &url);
};

#endif // DOWNLOAD_MANAGER_H
