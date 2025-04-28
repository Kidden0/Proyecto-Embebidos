# servo_test.py
# Prueba básica del servo motor SG90

import RPi.GPIO as GPIO
import time

# --- Configuración ---
PIN_SERVO = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_SERVO, GPIO.OUT)

servo = GPIO.PWM(PIN_SERVO, 50)  # 50 Hz
servo.start(0)
time.sleep(2)

# --- Programa Principal ---
try:
    print("Moviendo a 0 grados")
    servo.ChangeDutyCycle(2.5)  # Aproximadamente 0°
    time.sleep(2)

    print("Moviendo a 90 grados")
    servo.ChangeDutyCycle(7)    # Aproximadamente 90°
    time.sleep(2)

    print("Moviendo a 180 grados")
    servo.ChangeDutyCycle(12)   # Aproximadamente 180°
    time.sleep(2)

    print("Regresando a 0 grados")
    servo.ChangeDutyCycle(2.5)
    time.sleep(2)

except KeyboardInterrupt:
    print("\nPrueba interrumpida.")

finally:
    servo.stop()
    GPIO.cleanup()
