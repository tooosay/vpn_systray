from nordvpn import NordVPN
from vpninterface import VPNClientInterface


class VPN(VPNClientInterface):
    def __init__(self, provider, on_icon, off_icon, err_icon) -> None:
        self.on = on_icon
        self.off = off_icon
        self.err = err_icon
        self.provider = provider
        self.server = ""
        if provider == "nordvpn":
            self.vpn = NordVPN()

    
    def connect(self):
        self.vpn.connect(server=self.server)
    
    def disconnect(self):
        self.vpn.disconnect()
        
    def connected(self):
        return self.vpn.connected()
    
    def status(self):
        return self.vpn.satus()
    
    def reflect_status(self, systray):
        if self.connected():
            systray.setIcon(self.on)
        elif not self.connected():
            systray.setIcon(self.off)
        else: #error is not implemented
            systray.setIcon(self.err)
            print("something went wrong")
        
    def list_servers(self)->[]:
        return self.vpn.serverlist
    
    def setServer(self, server):
        self.server = server

    def change_provider(self, provider):
        if self.provider == provider:
            return
        if provider == "nordvpn":
            self.vpn = NordVPN()