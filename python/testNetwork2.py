import network
import machine
from machine import Pin
import socket

ssid = 'Estilos  H. '
password = 'estilosh'

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to WiFi')
    print('IP address:', wlan.ifconfig()[0])

def handle_request(request):
    if 'GET /toggle' in request:
        toggle_pin()

def toggle_pin():
    pin = Pin(2, Pin.OUT)
    pin.value(not pin.value())
    print('Pin toggled:', pin.value())

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 80))
    server.listen(5)
    print('Server listening on port 80')

    while True:
        client, addr = server.accept()
        print('Client connected from:', addr)

        request = client.recv(1024)
        print('Received request:')
        print(request.decode('utf-8'))

        handle_request(request.decode('utf-8'))

        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>ESP32 - HABLA RATON!</h1>"
        client.send(response.encode('utf-8'))
        client.close()

connect_to_wifi()
run_server()