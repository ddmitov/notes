////////////////////////////////////////

// Conditional include:
#if QT_VERSION < QT_VERSION_CHECK(5, 6, 0)
#include "webkit-main-window.h"
#endif

#if QT_VERSION > QT_VERSION_CHECK(5, 5, 0)
#include "webengine-main-window.h"
#endif

////////////////////////////////////////

// Command-line arguments:
QStringList commandLineArguments = QCoreApplication::arguments();

////////////////////////////////////////

// MD5 sum of a file:
QFile script (scriptFullFilePath);
QByteArray scriptFileArray;

if (script.open (QIODevice::ReadOnly)) {
    scriptFileArray = script.readAll();
}

QString scriptMd5sum = QString (
    QCryptographicHash::hash (
        (scriptFileArray),
        QCryptographicHash::Md5
    ).toHex()
);

////////////////////////////////////////

// Screen resolution:
int screenWidth = QDesktopWidget().screen()->rect().width();
int screenHeight = QDesktopWidget().screen()->rect().height();

////////////////////////////////////////

// Translation:
QTranslator translator;
translator.load("bg_BG", ":/translations");

application.installTranslator(&translator);

////////////////////////////////////////

// Logging:
void customMessageHandler(QtMsgType type,
                          const QMessageLogContext &context,
                          const QString &message)
{
    Q_UNUSED(context);

    QString dateAndTime =
            QDateTime::currentDateTime().toString("dd/MM/yyyy hh:mm:ss");

    QString text = QString("[%1] ").arg(dateAndTime);

    switch (type) {
#if QT_VERSION >= 0x050500
    case QtInfoMsg:
        text += QString("{Log} %1").arg(message);
        break;
#endif
    case QtDebugMsg:
        text += QString("{Log} %1").arg(message);
        break;
    case QtWarningMsg:
        text += QString("{Warning} %1").arg(message);
        break;
    case QtCriticalMsg:
        text += QString("{Critical} %1").arg(message);
        break;
    case QtFatalMsg:
        text += QString("{Fatal} %1").arg(message);
        abort();
        break;
    }

    // A separate log file is created for every browser session.
    // Application start date and time are appended to the binary file name.
    QFile logFile(qApp->property("logDirFullPath").toString()
                    + "/"
                    + QFileInfo(QApplication::applicationFilePath()).baseName()
                    + "-started-at-"
                    + qApp->property("applicationStartDateAndTime").toString()
                    + ".log"
                );

    logFile.open(QIODevice::WriteOnly | QIODevice::Append | QIODevice::Text);

    QTextStream textStream(&logFile);
    textStream << text << endl;
}

int main(int argc, char **argv)
{
    // If 'logs' directory is found in the resources directory,
    // all program messages will be redirected to log files,
    // otherwise no log files will be created and
    // program messages may be seen inside Qt Creator during development.
    QString logDirFullPath = resourcesDirectory + "/logs";

    QDir logDir(logDirFullPath);
    if (logDir.exists()) {
        application.setProperty("logDirFullPath", logDirFullPath);

        // Application start date and time for logging:
        QString applicationStartDateAndTime =
                QDateTime::currentDateTime().toString("yyyy-MM-dd--hh-mm-ss");

        application.setProperty(
            "applicationStartDateAndTime",
            applicationStartDateAndTime
        );

        // Install message handler for redirecting all messages to a log file:
        qInstallMessageHandler(customMessageHandler);
    }
}

////////////////////////////////////////
