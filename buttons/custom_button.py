from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QRect
from ui_look_and_feel.custom_font import customfont

class custombutton(QPushButton):
    def __init__(
        self, 
        buttontext,
        desired_font,
        dimensions
    ):
        super(custombutton, self).__init__()
        self.setGeometry(QRect(*dimensions))   # x, y, width, height
        myfont = customfont(*desired_font)
        self.setFont(myfont)
        self.setText(buttontext)