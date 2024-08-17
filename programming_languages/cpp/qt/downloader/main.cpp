// http://doc.qt.io/qt-5/qtnetwork-download-example.html

#include <QtCore>
#include "download-manager.h"

int main(int argc, char **argv)
{
    QCoreApplication app(argc, argv);
    QStringList args = QCoreApplication::instance()->arguments();

    QUrl url;
    url.setUrl(args[1]);

    DownloadManager downloadManager(url);
    Q_UNUSED(downloadManager);

    app.exec();
}
