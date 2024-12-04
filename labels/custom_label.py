from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QRect, Qt, QTimer
from ui_look_and_feel.custom_font import customfont
from random import choice

class customlabel(QLabel):
    def __init__(
        self,
        displaytext,
        dimensions,
        desired_font,
        stylised = False
    ):
        super(customlabel, self).__init__()
        self.setGeometry(QRect(*dimensions))  # x, y, width, height
        self.setFont(customfont(*desired_font))
        self.setText(displaytext)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.default_style = self.styleSheet()
        if stylised:
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.changeTextColor)

    def changeTextColor(self):
        colors = ["red", "blue", "green", "orange", "purple"]
        self.setStyleSheet(f"color: {choice(colors)};")
        
    def enterEvent(self, event):
        # Hover enter event
        if hasattr(self, 'timer'):
            self.timer.start(500)
        event.accept()

    def leaveEvent(self, event):
        # Hover leave event
        if hasattr(self, 'timer'):
            self.timer.stop()
            self.setStyleSheet(self.default_style) 
        event.accept()