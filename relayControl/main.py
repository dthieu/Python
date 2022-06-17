# .\relayControl\Scripts> .\qt5-tools.exe designer
# .\Scripts\pyuic5.exe -o main_window_ui.py relay_control.ui

import sys
from turtle import update
from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from main_window_ui import Ui_MainWindow
from functools import partial
from relay_lib import Relay
from multiplexer_lib import Multiplexer


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(485, 705)
        self.setupUi(self)
        self.loadRelayLabel()
        self.connectSignalsSlots()
        self.myRelay = Relay()
        self.myMUX = Multiplexer()
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
        self.connectCommonMode()
        self.connectCommonFunc()
        self.connectRelayPins()
        self.connectMUXMode()

    def connectCommonMode(self):
        self.rbNone.toggled.connect(self.checkedNone)
        self.rbNormalMode.toggled.connect(self.checkedNormalMode)
        self.rbAurixMode.toggled.connect(self.checkedAurixMode)
        self.rbAndroidMode.toggled.connect(self.checkedAndroidMode)
    
    def connectCommonFunc(self):
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

    def connectMUXMode(self):
        self.rbMUXNormalMode.toggled.connect(self.checkedMUXNormalMode)
        self.rbMUXDLTMode.toggled.connect(self.checkedMUXDLTMode)

    def checkedMUXNormalMode(self):
        self.myMUX.switch_to_normal_mode()
        self.log("[Multiplexer] Switch to normal mode")

    def checkedMUXDLTMode(self):
        self.myMUX.swith_to_DLT_mode()
        self.log("[Multiplexer] Switch to DLT mode")

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
            self.lblNum1.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectVBUS()
            self.lblNum1.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateState()
    
    def WD_OFFStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectWD_OFF()
            self.lblNum3.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectWD_OFF()
            self.lblNum3.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateState()
    
    def MOD_0StateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectMOD_0()
            self.lblNum4.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectMOD_0()
            self.lblNum4.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateState()
    
    def IGNStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectIGN()
            self.lblNum6.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectIGN()
            self.lblNum6.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateState()
    
    def ACCStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectACC()
            self.lblNum7.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectACC()
            self.lblNum7.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateState()
    
    def BATStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectBAT()
            self.lblNum8.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectBAT()
            self.lblNum8.setStyleSheet("color: rgb(0, 0, 0);")
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

    def checkedNone(self):
        self.clearAllRelayPins()
        self.log("[Relay] None")

    def checkedNormalMode(self):
        # BAT:8, ACC:7, IGN:6, WD_OFF:3 on
        self.clearAllRelayPins()
        self.log("[Relay] Switch to Normal mode")
        self.cb8.setChecked(True)
        self.cb7.setChecked(True)
        self.cb6.setChecked(True)
        self.cb3.setChecked(True)
    
    def checkedAurixMode(self):
        # VBUS:1, BAT:8, ACC:7, IGN:6 on
        self.clearAllRelayPins()
        self.log("[Relay] Switch to Aurix flashing mode")
        self.cb1.setChecked(True)
        self.cb8.setChecked(True)
        self.cb7.setChecked(True)
        self.cb6.setChecked(True)
    
    def checkedAndroidMode(self):
        # BAT:8, ACC:7, IGN:6, WD_OFF:3, MOD_0:4 on
        self.clearAllRelayPins()
        self.log("[Relay] Switch to Android flashing mode")
        self.cb8.setChecked(True)
        self.cb7.setChecked(True)
        self.cb6.setChecked(True)
        self.cb3.setChecked(True)
        self.cb4.setChecked(True)

    def restartTarget(self):
        self.log("[Relay] Restart the target!")
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
        self.log("[Relay] Turn off the target!")
        self.myRelay.turnOffAllRelay()
        self.clearAllRelayPins()
        self.updateState()
    
    def turnOnACC_IGN(self):
        self.log("[Relay] Turn on ACC + IGN!")
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


# ===================================================
# from functools import partial

# def calluser(name):
#     print name

# def Qbutton():
#     button = QtGui.QPushButton("button",widget)
#     name = "user"
#     button.setGeometry(100,100, 60, 35)
#     button.clicked.connect(partial(calluser,name))

ICON_RED_LED = "./assets/icon/led-red.png"
ICON_GREEN_LED = "./assets/icon/green-led.png"

# The icon can activated like this:
# self.ui.labelStatusFan1.setPixmap(QtGui.QPixmap(ICON_RED_LED))
# Also, by using signals, the icon can be activated based on some condition:
# self.pixmap_signal_fan1.emit(ICON_RED_LED if fans_rpm[0] == 0 or fans_voltage[0] == 0 else ICON_GREEN_LED)
