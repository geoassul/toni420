import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Estilos H. ","estilosh")

while not wlan.isconnected():
    time.sleep(1)

print(wlan.ifconfig())
