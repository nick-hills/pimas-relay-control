#!/usr/bin/python

from Adafruit_MCP230xx import Adafruit_MCP230XX
expander1 = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)
expander2 = Adafruit_MCP230XX(busnum = 1, address = 0x21, num_gpios = 16)

expander1.config(0,0)
expander1.config(1,0)
expander1.config(2,0)
expander1.config(3,0)
expander1.config(4,0)
expander1.config(5,0)
expander1.config(6,0)
expander1.config(7,0)
expander1.config(8,0)
expander1.config(9,0)
expander1.config(10,0)
expander1.config(11,0)
expander1.config(12,0)
expander1.config(13,0)
expander1.config(14,0)
expander1.config(15,0)

expander2.config(0,0)
expander2.config(1,0)
expander2.config(2,0)
expander2.config(3,0)
expander2.config(4,0)
expander2.config(5,0)
expander2.config(6,0)
expander2.config(7,0)
expander2.config(8,0)
expander2.config(9,0)
expander2.config(10,0)
expander2.config(11,0)
expander2.config(12,0)
expander2.config(13,0)
expander2.config(14,0)
expander2.config(15,0)

from Adafruit_PWM_Servo_Driver import PWM
from ola.ClientWrapper import ClientWrapper
import time

#set the e1.31 universe
universe = 6

#set the address of the PWM interface on the i2c bus
#pwm = PWM(0x40, debug=False)

#set the refresh rate
#pwm.setPWMFreq(60)

def NewData(data):
  #print (data)
  
  #write PWM RGB Outputs
  #pwm_write(0, data[0])
  #pwm_write(1, data[1])
  #pwm_write(2, data[2])
  
  #pwm_write(3, data[3])
  #pwm_write(4, data[4])
  #pwm_write(5, data[5])

  #pwm_write(6, data[6])
  #pwm_write(7, data[7])
  #pwm_write(8, data[8])

  #pwm_write(9, data[9])
  #pwm_write(10, data[10])
  #pwm_write(11, data[11])

  #pwm_write(12, data[12])
  #pwm_write(13, data[13])
  #pwm_write(14, data[14])

  # This is a standalone PWM output
 # pwm_write(15, data[15])
  
  #Now handle the GPIO outputs which control the relays
  relay_board1_write(0, 128, data[16])
  relay_board1_write(1, 128, data[17])
  relay_board1_write(2, 128, data[18])
  relay_board1_write(3, 128, data[19])
  relay_board1_write(4, 128, data[20])
  relay_board1_write(5, 128, data[21])
  relay_board1_write(6, 128, data[22])
  relay_board1_write(7, 128, data[23])
  relay_board1_write(8, 128, data[24])
  relay_board1_write(9, 128, data[25])
  relay_board1_write(10, 128, data[26])
  relay_board1_write(11, 128, data[27])
  relay_board1_write(12, 128, data[28])
  relay_board1_write(13, 128, data[29])
  relay_board1_write(14, 128, data[30])
  relay_board1_write(15, 128, data[31])

  relay_board2_write(0, 128, data[32])
  relay_board2_write(1, 128, data[33])
  relay_board2_write(2, 128, data[34])
  relay_board2_write(3, 128, data[35])
  relay_board2_write(4, 128, data[36])
  relay_board2_write(5, 128, data[37])
  relay_board2_write(6, 128, data[38])
  relay_board2_write(7, 128, data[39])
  relay_board2_write(8, 128, data[40])
  relay_board2_write(9, 128, data[41])
  relay_board2_write(10, 128, data[42])
  relay_board2_write(11, 128, data[43])
  relay_board2_write(12, 128, data[44])
  relay_board2_write(13, 128, data[45])
  relay_board2_write(14, 128, data[46])
  relay_board2_write(15, 128, data[47])


def pwm_write(pwm_channel, value):
    led_chunk = 4096 / 255            # divides the 12 bit value in to 255 levels
    led_level = led_chunk * value     # calculate the output level
    pwm.setPWM(pwm_channel, 0, led_level)

def relay_board1_write(gpio_channel, trigger_level, value):
    if value >= trigger_level:
	expander1.output(gpio_channel, 0)
    else:
	expander1.output(gpio_channel, 1)

def relay_board2_write(gpio_channel, trigger_level, value):
    if value >= trigger_level:
        expander2.output(gpio_channel, 0)
    else:
        expander2.output(gpio_channel, 1)


wrapper = ClientWrapper()
client = wrapper.Client()
client.RegisterUniverse(universe, client.REGISTER, NewData)
wrapper.Run()

