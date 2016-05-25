
import sys, time, serial
import time
import serial
import os
import RPi.GPIO as GPIO
Cortina=0
while True:
 entre=0
 f=open("luz.txt")
 sensa=f.read()
 f.close()
 print sensa
 if(sensa==''):
  error=0
 elif (int(sensa) > 500):
   if (Cortina==0):
    #Activacion
    Cortina=1
    entre=1
    print entre
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)
    #IZQ
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(27, GPIO.LOW)
    #DER
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22,GPIO.OUT)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(.5)
    #Apaga
    GPIO.output(17,GPIO.LOW)
            GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
    time.sleep
    GPIO.cleanup()
 if(sensa==''):
  error=0
 elif(int(sensa)<500):
   if(Cortina==1):
      Cortina=0
      #Activacion
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(17,GPIO.OUT)
      GPIO.output(17, GPIO.HIGH)
      #IZQ
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(27,GPIO.OUT)
      GPIO.output(27, GPIO.HIGH)
      #DER
            GPIO.setmode(GPIO.BCM)
      GPIO.setup(22,GPIO.OUT)
      GPIO.output(22, GPIO.LOW)
      time.sleep(.5)
      #Apaga
      GPIO.output(17,GPIO.LOW)
      GPIO.output(27,GPIO.LOW)
      GPIO.output(22,GPIO.LOW)
      time.sleep
      GPIO.cleanup()
