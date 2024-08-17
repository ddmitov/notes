
#include "download-manager.h"

DownloadManager::DownloadManager(const QUrl &url)
{
    QObject::connect(&manager, SIGNAL(finished(QNetworkReply*)),
                     this, SLOT(downloadFinished(QNetworkReply*)));

    QNetworkRequest request(url);
    QNetworkReply *reply = manager.get(request);

    QObject::connect(reply, SIGNAL(sslErrors(QList<QSslError>)),
                     this, SLOT(sslErrors(QList<QSslError>)));
}
