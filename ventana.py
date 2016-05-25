
import sys, time, serial
import time
import serial
import os
import RPi.GPIO as GPIO
Ventana=0
boton=0
while True:
 try:
  f=open("lluvia.txt")
  sensa=f.read()
  f.close()
  print sensa
  if(sensa==''):
   error=0
  elif (int(sensa) > 500):
   boton=0
   if(Ventana==1):
    #Activacion
    Ventana=0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23,GPIO.OUT)
    GPIO.output(23, GPIO.HIGH)
    #IZQ
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24,GPIO.OUT)
    GPIO.output(24, GPIO.LOW)
    #DER
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25,GPIO.OUT)
    GPIO.output(25, GPIO.HIGH)
    time.sleep(.5)
    #Apaga
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    GPIO.output(25,GPIO.LOW)
    time.sleep
    GPIO.cleanup()
  else:
   if(boton==1):
    if(Ventana==0):
     Ventana=1
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(23,GPIO.OUT)
     GPIO.output(23, GPIO.HIGH)
     #IZQ
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(24,GPIO.OUT)
     GPIO.output(24, GPIO.HIGH)
     #DER
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(25,GPIO.OUT)
     GPIO.output(25, GPIO.LOW)
     time.sleep(.33)
     #Apaga
     GPIO.output(23,GPIO.LOW)
     GPIO.output(24,GPIO.LOW)
     GPIO.output(25,GPIO.LOW)
     time.sleep
     GPIO.cleanup()
   if(boton==0):
    if(Ventana==1):
     Ventana=0
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(23,GPIO.OUT)
     GPIO.output(23, GPIO.HIGH)
     #IZQ
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(24,GPIO.OUT)
     GPIO.output(24, GPIO.LOW)
     #DER
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(25,GPIO.OUT)
     GPIO.output(25, GPIO.HIGH)
     time.sleep(.5)
     #Apaga
     GPIO.output(23,GPIO.LOW)
     GPIO.output(24,GPIO.LOW)
     GPIO.output(25,GPIO.LOW)
     time.sleep
     GPIO.cleanup()

 except KeyboardInterrupt:
  boton=not boton
  print boton


