from PyQt5 import QtWidgets as qt
from PyQt5 import QtCore as core
from PyQt5 import QtGui as gui
import sys
from .welcome import Welcome


class QPDFGui(qt.QTabWidget):
    # Initialize Window
    def __init__(self):
        # Create App
        self.app = qt.QApplication(sys.argv)

        # Set HiDPI
        self.app.setAttribute(core.Qt.AA_UseHighDpiPixmaps)

        # Initialize parent class
        super().__init__()

        # Define Window Attributes
        self.setWindowTitle('QPDF Gui')

        # Initial Window Geometry
        self.setGeometry(100, 100, 1024, 768)\

        # define Ui
        self.build_ui()

    def build_ui(self):
        # Add tabs for windows
        self.addTab(Welcome(), ' Welcome ')

    def run(self):
        # Show Window
        self.show()
        sys.exit(self.app.exec_())
