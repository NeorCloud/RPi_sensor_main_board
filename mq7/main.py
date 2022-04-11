from machine import Pin,PWM
import machine
import utime


line_1 = machine.ADC(1)

inp_1 =  Pin(28, Pin.OUT, value=1)


while True:
    adc_num = line_1.read_u16()
    print(adc_num)
    utime.sleep_us(50)

