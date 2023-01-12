#ADC CON PWM
import machine
from machine import Pin, PWM, ADC
import time
import dht

d = dht.DHT22(machine.Pin(33))
pwm0 = PWM(Pin(14), freq = 60, duty=0)
#bitup = Pin(12, Pin.IN, Pin.PULL_UP)
led0 = Pin(2,Pin.OUT)
pulse = 0
adc0 = ADC(Pin(34))
adc0.atten(ADC.ATTN_0DB)
adc0.width(ADC.WIDTH_12BIT)
ldrvalue = 0
while(True):
    time.sleep(5)
    d.measure()
    ldrvalue = adc0.read()
    #print(int(ldrvalue))
    print('T: ', d.temperature())
    print('H: ', d.humidity())
    if ldrvalue >= 3000:
        led0.on()
    else:
        led0.off()
    pwm0.duty(int(ldrvalue/4))