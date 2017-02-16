from readdht import monitor_dht_delay
from TransmitRF import transmit_code
from time import sleep
from datetime import datetime

b_on =  '0001100001011001110010101'
b_off = '0001010010011101011010101'

tscope = (21.5, 21.5)
hscope = (0, 100)
DHT_PIN = 4
repeat = 5
delay = 5
main_delay = 400

#transmit_code(b_on)

while True:
  print '--%s--' % str(datetime.now())
  tflag, hflag = monitor_dht_delay(DHT_PIN, tscope, hscope, repeat, delay)
  #print '\n WARNING: Finally get this: %d, %d' % (tflag, hflag)
  
  if tflag > 0:
    transmit_code(b_off)
    print 'turn OFF heater with switch B'
  if tflag < 0:
    transmit_code(b_on)
    print 'turn ON heater with switch B'
  
  sleep(main_delay)
