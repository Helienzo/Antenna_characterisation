from subprocess import call
import time

call(["nmcli", "device", "disconnect", "wlan0"])
time.sleep(1)
call(["nmcli", "d" ,"wifi", "list"])
ssid = raw_input("What wifi do you want to connect to? \n")
passw = raw_input("What is the network key? (if no key, write na) \n")

if passw == "na":
    call(["nmcli", "d", "wifi", "connect", ssid])
else:
    call(["nmcli", "d", "wifi", "connect", ssid, "password", passw]) 
    
