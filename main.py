from PyQt6.QtWidgets import QApplication
from gui import planningadmin_mainwindow, init_gui_elements
from behaviour import init_gui_behaviour
from settings import init_gui_settings
import os
import sys

if __name__ == "__main__":
    # try try
    # import subprocess
    # try:
    #     subprocess.run(['cscript', '//nologo', 'testfiles/script1.vbs'], check=True)
    # except subprocess.CalledProcessError as ee:
    #     print(f"some error: {ee}")
    # exit(0)
    # Switch to cwd and create new qt app
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    myApp = QApplication(sys.argv)

    # Create a mainwindow with all the GUI
    mainWindow = init_gui_elements()

    # Create the behaviours of the GUI
    init_gui_behaviour(mainWindow)

    # Load in settings of the GUI
    init_gui_settings(mainWindow)

    # Display the window
    mainWindow.show()
    myApp.exec()
    print("Finished")
