# led_test.py
# Prueba básica de encendido y apagado de un LED

import RPi.GPIO as GPIO
import time

# --- Configuración ---
PIN_LED = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

# --- Programa Principal ---
try:
    while True:
        GPIO.output(PIN_LED, GPIO.HIGH)  # LED encendido
        print("LED encendido")
        time.sleep(1)
        GPIO.output(PIN_LED, GPIO.LOW)   # LED apagado
        print("LED apagado")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPrueba interrumpida.")

finally:
    GPIO.cleanup()
