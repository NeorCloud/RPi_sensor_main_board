from machine import Pin,PWM
import utime
inp_3 = Pin(25, Pin.OUT, value=1)


eng_1_1 = Pin(18, Pin.OUT, value=1) #24
eng_1_2 = Pin(19, Pin.OUT, value=1) #25
eng_2_1 = Pin(20, Pin.OUT, value=1) #26
eng_2_2 = Pin(21, Pin.OUT, value=1) #27

s_1 = Pin(10, Pin.IN, Pin.PULL_UP) #14
s_2 = Pin(11, Pin.IN, Pin.PULL_UP) #15
s_3 = Pin(12, Pin.IN, Pin.PULL_UP) #16
s_4 = Pin(13, Pin.IN, Pin.PULL_UP) #17

while True:
    print ("s1:", s_1.value())
    print ("s2:", s_2.value())
    print ("s3:", s_3.value())
    print ("s4:", s_4.value())
    utime.sleep(1)
    print ("-----")

