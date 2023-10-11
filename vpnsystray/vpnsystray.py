# import vpn
import sys
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction
import os
from vpn import VPN
from functools import partial


def vpnsystray(on_icon_path, off_icon_path, err_icon_path):
    app = QApplication(sys.argv)
    provider = "nordvpn"

    on_icon = QIcon(on_icon_path)
    off_icon = QIcon(off_icon_path)
    err_icon = QIcon(err_icon_path)
    vpn = VPN(provider, on_icon, off_icon, err_icon)

    tray = QSystemTrayIcon()
    vpn.reflect_status(tray)

    tray.setVisible(True)

    menu = QMenu()
    menu_build(menu, vpn, tray)


    QUIT = QAction("Quit", menu)
    QUIT.triggered.connect(app.quit)
    menu.addAction(QUIT)
    tray.setContextMenu(menu)
    sys.exit(app.exec())

def menu_build(menu: QMenu, vpn, systray):
    connect = QAction("Connect", menu)
    disconnect = QAction("Disconnect", menu)

    connect.triggered.connect(vpn.connect)
    disconnect.triggered.connect(vpn.disconnect)
    
    # check status
    connect.triggered.connect(partial(vpn.reflect_status, systray))
    disconnect.triggered.connect(partial(vpn.reflect_status, systray))


    menu.addAction(connect)
    menu.addAction(disconnect)

def main():
    dir_name = os.path.dirname(os.getcwd()) + "/icons/"
    on_icon_path = dir_name + "vpn_on.png"
    off_icon_path = dir_name + "vpn_off.png"
    err_icon_path = dir_name + "vpn_err.png"
    vpnsystray(on_icon_path, off_icon_path, err_icon_path)

if __name__ == '__main__':
    main()