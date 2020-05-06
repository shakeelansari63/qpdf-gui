from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
import sys


class App(QMainWindow):

    def __init__(self, *args, **kwargs):

        # Create an App Context
        self.app = QApplication(sys.argv)

        # Initialize parent
        super().__init__(*args, **kwargs)

        # Set Window Title
        self.setWindowTitle("QPDF Gui")

        # Display Text
        label = QLabel("Hello World!!!")

        # Set Central label
        label.setAlignment(Qt.AlignCenter)

        # Set Widget in center
        self.setCentralWidget(label)

    def run(self):

        # Show window
        self.show()

        # Execute App
        self.app.exec_()
