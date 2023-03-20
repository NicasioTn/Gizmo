import pywifi
from pywifi import const

wifi = pywifi.PyWiFi() # Create an instance of the PyWiFi class
iface = wifi.interfaces()[0] # Get the first wireless interface

iface.scan() # Scan for nearby WiFi networks

networks = iface.scan_results() # Get a list of nearby WiFi networks
passwd = "********"

for network in networks:
    profile = pywifi.Profile() # Create a new profile for the network
    profile.ssid = network.ssid # Set the SSID of the profile to the network's SSID
    iface.connect(profile) # Connect to the network using the profile
    print("Connected to", network.ssid, "password: ", passwd) # Print the SSID of the connected network
    iface.disconnect() # Disconnect from the network
