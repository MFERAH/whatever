import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt, QCoreApplication
from PySide2.QtQml import QQmlApplicationEngine

if __name__ == '__main__':

    app = QApplication(sys.argv)

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    engine = QQmlApplicationEngine()
    engine.load('./main_form.qml')
    engine.rootObjects()[0].show()

    sys.exit(app.exec_())