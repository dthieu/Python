# D:\HIEU\PYTHON_WORLD\relayControl\Scripts> .\qt5-tools.exe designer
# .\Scripts\pyuic5.exe -o main_window_ui.py relay_control.ui



from os import stat


ICON_RED_LED = "./assets/icon/led-red.png"
ICON_GREEN_LED = "./assets/icon/green-led.png"
RELAY_COMMAND_PATH = "./USBLRB 0"

# The icon can activated like this:
# self.ui.labelStatusFan1.setPixmap(QtGui.QPixmap(ICON_RED_LED))
# Also, by using signals, the icon can be activated based on some condition:
# self.pixmap_signal_fan1.emit(ICON_RED_LED if fans_rpm[0] == 0 or fans_voltage[0] == 0 else ICON_GREEN_LED)

# 0 0 0 0  0 0 0 0
# 8 pins relay

# Common function
def setRelayPin1(state, relay_pos):
    state = state | (1 << (relay_pos - 1))
    print("[setRelayPin1] DEBUG: state = ", bin(state)[2:])
    return state

def setRelayPin0(state, relay_pos):
    state = state & ~ (1 << (relay_pos - 1))
    print("[setRelayPin0] DEBUG: state = ", bin(state)[2:])
    return state

# Given a number n, check if the Kth bit of n is set or not.
def isKthBitSet(n, k):
    '''
    Input:
    * n: number
    * k: kth bit
    '''
    return n & (1 << (k - 1))

import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from main_window_ui import Ui_MainWindow
from functools import partial

class Relay_Pin:
    VBUS = 1
    WD_OFF = 3
    MOD_0 = 4
    IGN = 6
    ACC = 7
    BAT = 8

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(823, 705)
        self.setupUi(self)
        self.updateRelayLabel()
        self.connectSignalsSlots()

    def updateRelayLabel(self):
        self.lblNum1.setText("VBUS")
        self.lblNum3.setText("WD_OFF")
        self.lblNum4.setText("MOD_0")
        self.lblNum6.setText("IGN")
        self.lblNum7.setText("ACC")
        self.lblNum8.setText("BAT")

    def connectSignalsSlots(self):
        self.txtCurrentState.textChanged.connect(self.updateCurrentState)
        self.cb1.stateChanged.connect(partial(self.clickBoxRelayPin, Relay_Pin.VBUS))
        

    def updateCurrentState(self):
        try:
            # Get current state
            state = int(self.txtCurrentState.text())
            # Convert int -> binary and display on LCD
            self.lcdBinState.display(format(state, '08b')) # display 8 bit
        except ValueError as err:
            self.txtLog.appendPlainText("Value of current state is invalid! \
                accept number only and valid range is [0, 255]). Detail error: " + str(err))
    
    def clickBoxRelayPin(self, state, relay_pos):
        print("state: ", state)
        current_state = int(self.txtCurrentState.text())
        if state == QtCore.Qt.Checked:
            current_state = setRelayPin1(current_state, relay_pos)
        else:
            current_state = setRelayPin0(current_state, relay_pos)
        
        self.txtCurrentState.setText(str(current_state))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())



# from functools import partial

# def calluser(name):
#     print name

# def Qbutton():
#     button = QtGui.QPushButton("button",widget)
#     name = "user"
#     button.setGeometry(100,100, 60, 35)
#     button.clicked.connect(partial(calluser,name))


