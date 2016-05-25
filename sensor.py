
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys, time, serial
import threading
serialPort ='/dev/ttyACM0'
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import time
import serial
import os
import RPi.GPIO as GPIO

# Iniciando conexión serial
arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
flagCharacter = 'K'
# Retardo para establecer la conexión serial
time.sleep(1.8)
while True:
 f1 = open('luz.txt', 'w')
 f2 = open('lluvia.txt', 'w')
 arduinoPort.write(flagCharacter)
 getSerialValue = arduinoPort.readline()
 getF=arduinoPort.readline()
 getL=arduinoPort.readline()
 #getSerialValue = arduinoPort.read()
 #getSerialValue = arduinoPort.read(20)
 print '\nValor retornado de Arduino: %s' % (getSerialValue)
 print '\nValor de foto resistencia: %s' % (getF)
 print '\nValor de LLuvia : %s' % (getL)
 f1.write(getF)
 f2.write(getL)
 f1.close()
 f2.close()
 arduinoPort.flushInput()
 arduinoPort.setDTR()
 time.sleep(0.3)

