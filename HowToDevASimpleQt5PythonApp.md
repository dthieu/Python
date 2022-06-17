# I. Create a virtual environment and start virtual environment
```bash
# Linux
$ cd <your project>
$ python -m venv .
$ source venv/bin/activate # Active virtual env

# Windows
$ cd <to your project>
$ python -m venv .
$ . Activate.ps1 # Active virtual env
```
# II. Install needed library
## Windows
```bash
(<your project>) $ pip install pyqt5 pyqt5-tools
```
## Linux
```bash
$ sudo apt install qttools5-dev-tools
```
# III. Create GUI 
## 1. Open Qt5 designer tool 
### Windows
`$ Script\qt5-tools.exe designer`
### Linux
```bash
..lib/python3.x/site-packages/qt5_applications/Qt/bin/designer
```
Design GUI app and save it as name `<name_ui>.ui` 
## 2. Generate GUI code 
`$ Scripts\pyuic5.exe -o <main_window_ui>.py <name_ui>.ui`
## 3. Import and using GUI code
Template code:
```python

from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from main_window_ui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(485, 705)
        self.setupUi(self)
        # TODO

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
```
## 4. Generate needed modules via virtual environment
```bash
$ pip freeze > requirements.txt
```



