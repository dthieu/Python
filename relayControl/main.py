# D:\HIEU\PYTHON_WORLD\relayControl\Scripts> .\qt5-tools.exe designer
# .\Scripts\pyuic5.exe -o main_window_ui.py relay_control.ui

ICON_RED_LED = "./assets/icon/led-red.png"
ICON_GREEN_LED = "./assets/icon/green-led.png"

# The icon can activated like this:
# self.ui.labelStatusFan1.setPixmap(QtGui.QPixmap(ICON_RED_LED))
# Also, by using signals, the icon can be activated based on some condition:
# self.pixmap_signal_fan1.emit(ICON_RED_LED if fans_rpm[0] == 0 or fans_voltage[0] == 0 else ICON_GREEN_LED)

import os
import sys
from turtle import update
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from main_window_ui import Ui_MainWindow
from functools import partial
from relay_lib import Relay


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(823, 705)
        self.setupUi(self)
        self.loadRelayLabel()
        self.connectSignalsSlots()
        self.myRelay = Relay()
        self.txtCurrentState.setText(str(self.myRelay.curr_state))

    def loadRelayLabel(self):
        self.lblNum1.setText("VBUS")
        self.lblNum3.setText("WD_OFF")
        self.lblNum4.setText("MOD_0")
        self.lblNum6.setText("IGN")
        self.lblNum7.setText("ACC")
        self.lblNum8.setText("BAT")

    def connectSignalsSlots(self):
        self.txtCurrentState.textChanged.connect(self.updateCurrentState)
        self.rbNone.toggled.connect(self.checkedNone)
        self.rbNormalMode.toggled.connect(self.checkedNormalMode)
        self.rbAurixMode.toggled.connect(self.checkedAurixMode)
        self.rbAndroidMode.toggled.connect(self.checkedAndroidMode)
        self.connectButtons()
        self.connectRelayPins()

    def connectButtons(self):
        self.btnTargetOff.clicked.connect(self.turnOffTarget)
        self.btnTargetRestart.clicked.connect(self.restartTarget)
        self.btnACC_IGN_on.clicked.connect(self.turnOnACC_IGN)

    def connectRelayPins(self):
        self.cb1.stateChanged.connect(self.VBUSStateChanged)
        self.cb3.stateChanged.connect(self.WD_OFFStateChanged)
        self.cb4.stateChanged.connect(self.MOD_0StateChanged)
        self.cb6.stateChanged.connect(self.IGNStateChanged)
        self.cb7.stateChanged.connect(self.ACCStateChanged)
        self.cb8.stateChanged.connect(self.BATStateChanged)

    def updateCurrentState(self):
        try:
            # Get current state
            state = self.myRelay.curr_state
            # Convert int -> binary and display on LCD
            self.lcdBinState.display(format(state, '08b')) # display 8 bit
        except ValueError as err:
            self.log("Value of current state is invalid! \
                accept number only and valid range is [0, 255]). Detail error: " + str(err))
    
    def VBUSStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectVBUS()
        else:
            self.myRelay.disconnectVBUS()
        self.updateState()
    
    def WD_OFFStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectWD_OFF()
        else:
            self.myRelay.disconnectWD_OFF()
        self.updateState()
    
    def MOD_0StateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectMOD_0()
        else:
            self.myRelay.disconnectMOD_0()
        self.updateState()
    
    def IGNStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectIGN()
        else:
            self.myRelay.disconnectIGN()
        self.updateState()
    
    def ACCStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectACC()
        else:
            self.myRelay.disconnectACC()
        self.updateState()
    
    def BATStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectBAT()
        else:
            self.myRelay.disconnectBAT()
        self.updateState()

    def updateState(self):
        self.txtCurrentState.setText(str(self.myRelay.curr_state))

    def clearAllRelayPins(self):
        self.cb1.setChecked(False)
        self.cb2.setChecked(False)
        self.cb3.setChecked(False)
        self.cb4.setChecked(False)
        self.cb5.setChecked(False)
        self.cb6.setChecked(False)
        self.cb7.setChecked(False)
        self.cb8.setChecked(False)
        self.log("Reset all pins to unchecked status")

    def checkedNone(self):
        self.clearAllRelayPins()
        self.log("None!")

    def checkedNormalMode(self):
        # BAT:8, ACC:7, IGN:6, WD_OFF:3 on
        self.clearAllRelayPins()
        self.cb8.setChecked(True)
        self.cb7.setChecked(True)
        self.cb6.setChecked(True)
        self.cb3.setChecked(True)
        self.log("Switch to Normal mode")
    
    def checkedAurixMode(self):
        # VBUS:1, BAT:8, ACC:7, IGN:6 on
        self.clearAllRelayPins()
        self.cb1.setChecked(True)
        self.cb8.setChecked(True)
        self.cb7.setChecked(True)
        self.cb6.setChecked(True)
        self.log("Switch to Aurix flashing mode")
    
    def checkedAndroidMode(self):
        # BAT:8, ACC:7, IGN:6, WD_OFF:3, MOD_0:4 on
        self.clearAllRelayPins()
        self.cb8.setChecked(True)
        self.cb7.setChecked(True)
        self.cb6.setChecked(True)
        self.cb3.setChecked(True)
        self.cb4.setChecked(True)
        self.log("Switch to Android flashing mode")

    def restartTarget(self):
        self.myRelay.turnOffAllRelay()
        self.clearAllRelayPins()
        self.myRelay.connectBAT()
        self.cb8.setChecked(True)
        self.myRelay.connectACC()
        self.cb7.setChecked(True)
        self.myRelay.connectIGN()
        self.cb6.setChecked(True)
        self.updateState()
    
    def turnOffTarget(self):
        self.myRelay.turnOffAllRelay()
        self.clearAllRelayPins()
        self.updateState()
    
    def turnOnACC_IGN(self):
        self.myRelay.connectACC()
        self.cb7.setChecked(True)
        self.myRelay.connectIGN()
        self.cb6.setChecked(True)
        self.updateState()
    
    def log(self, message):
        self.txtLog.appendPlainText(message)
        

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


