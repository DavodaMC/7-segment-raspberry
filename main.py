#
# SCRIPT EN MICROPYTHON PARA ENCENDER PINES DE RASPBERRY PI PICO
#
#
# Scripted by: Davoda
#

#
# IMPORTS
#
from machine import Pin
import time
import random
#

#
# DECLARAMOS LAS VARIABLES DE LOS PINES
#
led12 = Pin(12, Pin.OUT)
led13 = Pin(13, Pin.OUT)
led14 = Pin(14, Pin.OUT)
led15 = Pin(15, Pin.OUT)
led16 = Pin(16, Pin.OUT)
led17 = Pin(17, Pin.OUT)
led18 = Pin(18, Pin.OUT)
led19 = Pin(19, Pin.OUT)
#

#
# DEFINIMOS LA FUNCIÓN PARA APAGAR TODOS
#
def apagartodos():
    led12.off()
    led13.off()
    led14.off()
    led15.off()
    led16.off()
    led17.off()
    led18.off()
    led19.off()
def numero0():
    led12.on()
    led13.on()
    led14.off()
    led15.on()
    led16.on()
    led17.on()
    led18.off()
    led19.on()
def numero1():
    led12.off()
    led13.on()
    led14.off()
    led15.off()
    led16.off()
    led17.off()
    led18.off()
    led19.on()
def numero2():
    led12.on()
    led13.on()
    led14.on()
    led15.off()
    led16.on()
    led17.on()
    led18.off()
    led19.off()
def numero3():
    led12.on()
    led13.on()
    led14.on()
    led15.off()
    led16.on()
    led17.off()
    led18.off()
    led19.on()
def numero4():
    led12.off()
    led13.on()
    led14.on()
    led15.on()
    led16.off()
    led17.off()
    led18.off()
    led19.on()
def numero5():
    led12.on()
    led13.off()
    led14.on()
    led15.on()
    led16.on()
    led17.off()
    led18.off()
    led19.on()
def numero6():
    led12.on()
    led13.off()
    led14.on()
    led15.on()
    led16.on()
    led17.on()
    led18.off()
    led19.on()
def numero7():
    led12.on()
    led13.on()
    led14.off()
    led15.off()
    led16.off()
    led17.off()
    led18.off()
    led19.on()
def numero8():
    led12.on()
    led13.on()
    led14.on()
    led15.on()
    led16.on()
    led17.on()
    led18.off()
    led19.on()
def numero9():
    led12.on()
    led13.on()
    led14.on()
    led15.on()
    led16.off()
    led17.off()
    led18.off()
    led19.on()
#

#
# FUNCIÓN PARA DIBUJAR EL NÚMERO SOLICITADO
#
def pedirnumero(numero):
    if numero > 9:
        print('No te pases de largo, un número del 0 al 9, imbécil.')
    if numero < 0:
        print('No te quedes corto, un número del 0 al 9, imbécil.')
    if numero is 0:
        numero0()
    if numero is 1:
        numero1()
    if numero is 2:
        numero2()
    if numero is 3:
        numero3()
    if numero is 4:
        numero4()
    if numero is 5:
        numero5()
    if numero is 6:
        numero6()
    if numero is 7:
        numero7()
    if numero is 8:
        numero8()
    if numero is 9:
        numero9()
#

#
# RANDOM NUMBER GENERATOR DADOS
#
def randomnumberdados():
    apagartodos()
    led19.on
    time.sleep(1)
    led19.off
    time.sleep(1)
    led19.on
    time.sleep(1)
    led19.off
    time.sleep(1)
    led19.on
    time.sleep(1)
    led19.off
    
    num_random = random.randint(0, 9)
    
    pedirnumero(num_random)
    print('Ha salido como primer número: ', int(num_random))
    time.sleep(3)
    apagartodos()
    time.sleep(3)
    
    num_random2 = random.randint(0, 9)
    
    pedirnumero(num_random2)
    print('Ha salido como segundo número: ', int(num_random2))
    
    if num_random > num_random2:
        print('El primer número ', int(num_random), ' es el ganador.')
    else:
        print('El segundo número ', int(num_random2), ' es el ganador.')
#

#
# DEFINIMOS LA FUNCIÓN MAIN (PRINCIPAL)
#
def main():
    apagartodos()
    num=int(input('Introduce un número del 0 al 9: '))
    pedirnumero(num)
#

#
if __name__ == "__main__":
    main()