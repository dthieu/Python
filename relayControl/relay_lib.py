import os

RELAY_COMMAND_PATH = "./USBLRB 0 "

class Relay:
    curr_state = 0
    # Relay pins
    VBUS = 1
    WD_OFF = 3
    MOD_0 = 4
    IGN = 6
    ACC = 7
    BAT = 8

    def debug_log_curr_state(self):
        print(f"Current state: {self.curr_state} ({bin(self.curr_state)[2:]})")

    # Set bit of relay_pos to 1
    def setRelayPin1(self, relay_pos):
        self.curr_state = self.curr_state | (1 << (relay_pos - 1))
        # relay_command = RELAY_COMMAND_PATH + str(self.curr_state)
        # os.system(relay_command)
        self.debug_log_curr_state()
    
    # Set bit of relay_pos to 0
    def setRelayPin0(self, relay_pos):
        self.curr_state = self.curr_state & ~ (1 << (relay_pos - 1))
        # relay_command = RELAY_COMMAND_PATH + str(self.curr_state)
        # os.system(relay_command)
        self.debug_log_curr_state()

    # Given a number curr_state, check if the Kth bit of curr_state is set or not.
    def isKthBitSet(self, kth_bit):
        '''
        Input:
        * n: number
        * k: kth bit
        Output:
        * True: set
        * False: not set yet
        '''
        return self.curr_state & (1 << (kth_bit - 1))
    
    def turnOffAllRelay(self):
        print("Turn off all relay pins")
        self.curr_state = 0
        # relay_command = RELAY_COMMAND_PATH + str(self.curr_state)
        # os.system(relay_command)
        self.debug_log_curr_state()
        
    def connectBAT(self):
        print("Connect BAT")
        if not self.isKthBitSet(self.BAT):
            self.setRelayPin1(self.BAT)
    
    def connectVBUS(self):
        print("Connect VBUS")
        if not self.isKthBitSet(self.VBUS):
            self.setRelayPin1(self.VBUS)

    def connectMOD_0(self):
        print("Connect MOD_0")
        if not self.isKthBitSet(self.MOD_0):
            self.setRelayPin1(self.MOD_0)

    def connectACC(self):
        print("Connect ACC")
        if not self.isKthBitSet(self.ACC):
            self.setRelayPin1(self.ACC)
    
    def connectIGN(self):
        print("Connect IGN")
        if not self.isKthBitSet(self.IGN):
            self.setRelayPin1(self.IGN)
    
    def connectACC_IGN(self):
        print("Connect ACC IGN")
        self.connectACC()
        self.connectIGN()

    def connectWD_OFF(self):
        print("Connect WD_OFF")
        if not self.isKthBitSet(self.WD_OFF):
            self.setRelayPin1(self.WD_OFF)

    def disconnectVBUS(self):
        print("Disconnect VBUS")
        if self.isKthBitSet(self.VBUS):
            self.setRelayPin0(self.VBUS)
    
    def disconnectMOD_0(self):
        print("Disconnect MOD_0")
        if self.isKthBitSet(self.MOD_0):
            self.setRelayPin0(self.MOD_0)

    def disconnectBAT(self):
        print("Disconnect BAT")
        if self.isKthBitSet(self.BAT):
            self.setRelayPin0(self.BAT)
    
    def disconnectACC(self):
        print("Disconnect ACC")
        if self.isKthBitSet(self.ACC):
            self.setRelayPin0(self.ACC)
    
    def disconnectIGN(self):
        print("Disconnect IGN")
        if self.isKthBitSet(self.IGN):
            self.setRelayPin0(self.IGN)

    def disconnectBAT_ACC_IGN(self):
        print("Disconnect BAT ACC IGN")
        self.disconnectBAT()
        self.disconnectACC()
        self.disconnectIGN()

    def disconnectWD_OFF(self):
        print("Disconnect WD_OFF")
        if self.isKthBitSet(self.WD_OFF):
            self.setRelayPin0(self.WD_OFF)