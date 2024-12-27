from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QRect
from ui_look_and_feel.custom_font import customfont

class custombutton(QPushButton):
    def __init__(
        self, 
        buttontext,
        desired_font,
        dimensions,
        buttontext_colour,
        button_transparency,
    ):
        super(custombutton, self).__init__()
        self.setGeometry(QRect(*dimensions))   # x, y, width, height
        myfont = customfont(*desired_font)
        self.setFont(myfont)
        self.setText(buttontext)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: rgba(0, 0, 0, {button_transparency}); /* Semi-transparent black overlay */
                color: {buttontext_colour};                           /* button text text */
                border: none;                        /* No border */
                padding: 12px 20px;                  /* Material design padding */
                font-size: 14px;                     /* Slightly larger font */
                border-radius: 8px;                  /* Rounded corners for Material Design */
                transition: background-color 0.3s;   /* Smooth color transitions */
            }}
            QPushButton:hover {{
                background-color: rgba(0, 0, 0, 60); /* Darker black on hover */
            }}
            QPushButton:pressed {{
                background-color: rgba(0, 0, 0, 80); /* Even darker black on press */
            }}
        """
        )