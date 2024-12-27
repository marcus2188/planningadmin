from PyQt6.QtWidgets import QRadioButton
from PyQt6.QtCore import QRect, Qt, QSize

class customradiobutton(QRadioButton):
    def __init__(
        self,
        dimensions,
        radio_text,
        checked,
        checkbox_colour,
        fixed_size = None
    ):
        super(customradiobutton, self).__init__()
        self.radio_text = radio_text
        self.setGeometry(QRect(*dimensions))  # x, y, width, height
        if fixed_size:
            self.setFixedSize(QSize(*fixed_size))
        self.setText("  " + radio_text)   # temp fix for margin css issues, haiya!
        self.setStyleSheet(f"""
            QRadioButton {{
                padding: 8px;                            /* Comfortable padding */
                font-family: 'Trebuchet MS', sans-serif;        /* Material font */
                font-size: 12px;                         /* Slightly larger font size */
                line-height: 1;                        /* Improved line spacing */
                margin-right: 10px;                      /* Margin to separate from text */
            }}

            QRadioButton::indicator {{
                width: 30px;
                height: 30px;
                border-radius: 5px;                  /* Circular indicator */
                transition: all 0.3s ease;           /* Smooth transition */
            }}

            QRadioButton::indicator:checked {{
                background-color: rgb{checkbox_colour};               /* Material Design blue for selected */
            }}

            QRadioButton::indicator:unchecked {{
                background-color: rgba(0, 0, 0, 48);               /* Light gray when unchecked */
            }}
        """) # follows sidebar color for checkbox indicator
        self.setChecked(checked)