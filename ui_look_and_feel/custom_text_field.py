from PyQt6.QtWidgets import QTextBrowser
from PyQt6.QtCore import QRect, Qt, QSize

class customtextfield(QTextBrowser):
    def __init__(
        self,
        dimensions,
        fixed_size = None
    ):
        super(customtextfield, self).__init__()
        self.setGeometry(QRect(*dimensions))  # x, y, width, height
        self.setPlainText("")
        if fixed_size:
            self.setFixedSize(QSize(*fixed_size))
        self.setStyleSheet("""
            QTextBrowser {
                background-color: #FAFAFA; /* Light background */
                color: #212121;            /* Dark text */
                border: 1px solid #E0E0E0; /* Light gray border */
                border-radius: 8px;        /* Rounded corners */
                padding: 4px;             /* Comfortable padding */
                font-family: 'Trebuchet MS', sans-serif; /* Material font */
                font-size: 12px;           /* Comfortable text size */
                line-height: 1;          /* Adequate line spacing */
            }
        """)