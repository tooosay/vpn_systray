import vpnsystray as app
import os

def main():
    dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/icons/"
    on_icon_path = dir_name + "vpn_on.png"
    off_icon_path = dir_name + "vpn_off.png"
    err_icon_path = dir_name + "vpn_err.png"

    app.vpnsystray(on_icon_path, off_icon_path, err_icon_path)

if __name__ == "__main__":
    main()