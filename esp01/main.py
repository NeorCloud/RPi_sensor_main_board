from machine import Pin
from esp8266 import ESP8266
import time, sys

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("RPi-Pico MicroPython Ver:", sys.version)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

## Create On-board Led object
led=Pin(25,Pin.OUT)

## Create an ESP8266 Object
esp01 = ESP8266()
esp8266_at_ver = None

print("StartUP",esp01.startUP())
print("Echo-Off",esp01.echoING())
print("\r\n")

'''
Print ESP8266 AT comand version and SDK details
'''
esp8266_at_ver = esp01.getVersion()
if(esp8266_at_ver != None):
    print(esp8266_at_ver)

'''
set the current WiFi in SoftAP+STA
'''
print("WiFi Current Mode:",esp01.setCurrentWiFiMode())
  
print("\r\n\r\n")

'''
Connect with the WiFi
'''
print("Try to connect with the WiFi..")
while (1):
    if "WIFI CONNECTED" in esp01.connectWiFi("Irancell-Z6000","@9123214684@"):
        print("ESP8266 connect with the WiFi..")
        break;
    else:
        print(".")
        time.sleep(2)


print("\r\n\r\n")
print("Now it's time to start HTTP Get/Post Operation.......\r\n")

while(1):    
    led.toggle()
    time.sleep(1)
    
    '''
    Going to do HTTP Get Operation with www.httpbin.org/ip, It return the IP address of the connected device
    '''
    httpCode, httpRes = esp01.doHttpGet("www.httpbin.org","/ip","RaspberryPi-Pico", port=80)
    print("------------- www.httpbin.org/ip Get Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("-----------------------------------------------------------------------------\r\n\r\n")
    
    
    httpCode, httpRes = esp01.doHttpGet("api-server-iot-demo-lgyn.hamdam.0-1.neorcloud.com","/api/metrics","RaspberryPi-Pico", port=80)
    print("------------- NEOR Get Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("-----------------------------------------------------------------------------\r\n\r\n")
    
    
    
    '''
    Going to do HTTP Post Operation with www.httpbin.org/post
    '''
    post_json="{\"adc_num\":\"12\"}"
    httpCode, httpRes = esp01.doHttpPost("api-server-iot-demo-lgyn.hamdam.0-1.neorcloud.com","/api/metrics","RPi-Pico", "application/json",post_json,port=80)
    print("------------- NEOR Post Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("--------------------------------------------------------------------------------\r\n\r\n")

