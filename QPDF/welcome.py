from PyQt5 import QtWidgets as qt
from PyQt5 import QtCore as core
from PyQt5 import QtGui as gui


class Welcome(qt.QWidget):
    def __init__(self):
        # Initialize Parent widget
        super().__init__()

        # Build Ui
        self.build_ui()

    def build_ui(self):
        # Define layout
        self.vlayout = qt.QVBoxLayout()
        self.hlayout = qt.QHBoxLayout()

        # Left Padding
        self.hlayout.addStretch()

        # Central text
        central_layout = qt.QVBoxLayout()
        header = gui.QFont()
        header.setBold(True)
        header.setPointSize(30)
        header_text = qt.QLabel('QPDF Gui')
        header_text.setFont(header)
        central_layout.addWidget(header_text)

        # Instruction
        text_row = qt.QHBoxLayout()
        prereq = qt.QLabel('Pre-requisite: ')
        textreq = qt.QLabel(
            'Install QPDF using following link for using this app')
        bold_text = gui.QFont()
        bold_text.setBold(True)
        prereq.setFont(bold_text)
        text_row.addWidget(prereq)
        text_row.addWidget(textreq)
        text_row.addStretch()
        central_layout.addLayout(text_row)

        # URL for QPDF CLI
        url_row = qt.QHBoxLayout()
        url = qt.QLabel(
            '<a href="https://github.com/qpdf/qpdf">https://github.com/qpdf/qpdf</a>')
        url.setOpenExternalLinks(True)
        url_row.addWidget(url)
        url_row.addStretch()
        central_layout.addLayout(url_row)

        # Set central widget in
        self.hlayout.addLayout(central_layout)

        # Right Padding
        self.hlayout.addStretch()

        # Set main layout
        self.vlayout.addStretch()
        self.vlayout.addLayout(self.hlayout)
        self.vlayout.addStretch()

        # Set main layout
        self.setLayout(self.vlayout)
