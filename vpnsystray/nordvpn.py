from vpninterface import VPNClientInterface as VPN
from subprocess import call, check_output, run
# from os import environ

class NordVPN(VPN):
    def __init__(self):
        self.cmd = "LANG=en_US.UTF-8 nordvpn"
        # environ["LANG"] = "en_US.UTF-8"
        self.serverlist = []
        self.list_servers()
    
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
    
    def list_servers(self):
        cmd1 = self.cmd + " " + "countries"
        cmd2 = self.cmd + " " + "groups"
        status1 = check_output(cmd1, shell=True)
        status2 = check_output(cmd2, shell=True)
        skipread = False
        status = [status1, status2]
        for status in status:
            for server in status.decode("utf-8").split():
                if server == "-" and not skipread:
                    skipread = True
                    continue
                elif skipread and server == "-":
                    skipread = False
                    continue
                elif skipread:
                    continue
                else:
                    self.serverlist.append(server)