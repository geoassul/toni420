#ADC CON PWM - IOT
from machine import Pin, PWM, ADC
import time
import network
wlan = network.WLAN(network.STA_IF) #se crea interfaz de conexion wifi
wlan.active(True) #se activa la interfaz
wlan.scan() # se busca un AP
wlan.connect('toni','Gogogogo2020') #se conecta a un AP
print('ip: ', wlan.ifconfig())

pwm0 = PWM(Pin(14), freq = 60, duty=0)
#bitup = Pin(12, Pin.IN, Pin.PULL_UP)
led0 = Pin(2,Pin.OUT)
pulse = 0
adc0 = ADC(Pin(34))
adc0.atten(ADC.ATTN_0DB)
adc0.width(ADC.WIDTH_12BIT)
ldrvalue = 0
while(True):
    time.sleep_ms(200)
    ldrvalue = adc0.read()
    #print(int(ldrvalue))
    if ldrvalue >= 3000:
        led0.on()
    else:
        led0.off()
    pwm0.duty(int(ldrvalue/4))
    