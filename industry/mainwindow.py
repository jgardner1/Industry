import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Industry")

    @Slot()
    def exit_app(self, checked):
        sys.exit()


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
