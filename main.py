"""main app"""
import sys
from PyQt5.QtWidgets import QApplication
import MainWindow


def main():
    """main app function"""
    app = QApplication(sys.argv)
    window = MainWindow.MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
