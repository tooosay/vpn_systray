from vpninterface import VPNClientInterface as VPN
from subprocess import call, check_output, run
# from os import environ

class NordVPN(VPN):
    def __init__(self):
        self.cmd = "LANG=en_US.UTF-8 nordvpn"
        # environ["LANG"] = "en_US.UTF-8"
    
    def execute(self, cmd):
        ok = call(cmd, shell=True)
        return ok == 0

    def connect(self, server=""):
        cmd = self.cmd + " "+ "connect" + server
        self.execute(cmd)

    def disconnect(self):
        cmd = self.cmd + " " + "disconnect"
        self.execute(cmd)

    def status(self):
        cmd = self.cmd + " " + "status"
        status = check_output(cmd, shell=True)
        return status.decode("utf-8")

    def connected(self):
        status = self.status()
        for line in status.splitlines():
            if line == "Status: Connected":
                return True
            elif line == "Status: Disconnected":
                return False