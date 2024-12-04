from PyQt6.QtWidgets import QWidget, QProgressBar, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import QCoreApplication


class progressBox(QWidget):
    def __init__(
        self,
        initialProgress,
        internalTextStr,
        titleTextStr,
        cssStyleSheetStr=None
    ):
        super(progressBox, self).__init__()
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(initialProgress)
        if not cssStyleSheetStr:
            self.progress_bar.setStyleSheet("""
                #progress_bar {
                    height: 20px;
                    background-color: #fff;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }

                #progress_bar .progress {
                    height: 100%;
                    background-color: #00f;
                    border-radius: 5px;
                }
            """)
        else:
            self.progress_bar.setStyleSheet(cssStyleSheetStr)
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        self.text_label = QLabel(internalTextStr)
        layout.addWidget(self.text_label)
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.close)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)
        self.setWindowTitle(titleTextStr)

    def displayPlease(self):
        self.text_label.setText("Please Wait..., Appreciate your patience")
        self.show()
        self.ok_button.hide()
        QCoreApplication.processEvents()

    def updateProgressBar(self, newProgressValue):
        self.progress_bar.setValue(int(newProgressValue))
        QCoreApplication.processEvents()
        self.raise_()

    def updateInternalText(self, newText):
        self.text_label.setText(newText)
        QCoreApplication.processEvents()

    def updateProgressBarAndStatusText(self, newProgressValue, newText):
        self.progress_bar.setValue(int(newProgressValue))
        self.text_label.setText(newText)
        QCoreApplication.processEvents()

    def unhideOkButton(self):
        self.ok_button.show()
        QCoreApplication.processEvents()
