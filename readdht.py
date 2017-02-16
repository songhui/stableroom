#!/usr/bin/python
import sys
import Adafruit_DHT
from time import sleep

DHT_PIN = 4
DHT_MODEL = 11


def read_dht_delay(pin, repeat = 5, delay = 3):
  # The reading has to be stable for $repeat times before an acceptable
  # result is returned

  curr_hum = 0
  curr_temp = 0

  count_down = repeat
  
  while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, pin)

    print 'Temp: %.2f C  Humidity: %.2f' % (temperature, humidity)

    if humidity == curr_hum and temperature == curr_temp:
      count_down = count_down - 1
    else:
      count_down = repeat

    curr_hum = humidity 
    curr_temp = temperature 

    #print count_down    

    if count_down <= 0:
      return (humidity, temperature)

    sleep(delay)

def get_flag(value, scope):
  if value < scope[0]:
    return -1
  if value > scope[1]:
    return 1
  else:
    return 0

def monitor_dht_delay(pin, tscope, hscope, repeat = 5, delay = 4):
  # The reading has to be stable for $repeat times before an acceptable
  # result is returned

  tflag, hflag = (0,0)
  
  while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, pin)

    print 'Temp: %.2f C  Humidity: %.2f' % (temperature, humidity)

    ctflag = get_flag(temperature, tscope)
    chflag = get_flag(humidity, hscope)

    if ctflag * tflag < 0 or ctflag == 0:
      tflag = 0
    else:
      tflag = tflag + ctflag

    if chflag * hflag < 0 or chflag == 0:
      hflag = 0
    else:
      hflag = hflag + chflag

    if abs(tflag) > repeat or abs(hflag) > repeat:
      if abs(tflag) < repeat: tflag = 0
      if abs(hflag) < repeat: hflag = 0
      return (tflag, hflag)

    #print 'tflag: %d, hflag: %d' % (tflag, hflag)
    sleep(delay)


#while True:
#  #humidity, temperature = read_dht_delay(DHT_PIN)
#  tflag, hflag = monitor_dht_delay(4, (24,25), (30,40), 5, 4)
#  print '\n== Finally get this: %d, %d' % (tflag, hflag)
