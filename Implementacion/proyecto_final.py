# Proyecto: Sistema Embebido de Control de Puerta mediante PIN en Raspberry Pi
# Descripción: Control de acceso mediante teclado 4x4, LED, Servo SG90 y LCD 16x2 I2C.

# --- Importación de Librerías ---
import RPi.GPIO as GPIO
import time
import board
import busio
import digitalio
from RPLCD.i2c import CharLCD
import adafruit_matrixkeypad

# --- Configuración de Pines ---
# Definición de GPIOs
PIN_LED = 17              # GPIO para el LED indicador
PIN_SERVO = 18            # GPIO para el servo (PWM)

# Configuración de pines del teclado
rows = [digitalio.DigitalInOut(board.D5), digitalio.DigitalInOut(board.D6),
        digitalio.DigitalInOut(board.D13), digitalio.DigitalInOut(board.D19)]

cols = [digitalio.DigitalInOut(board.D12), digitalio.DigitalInOut(board.D16),
        digitalio.DigitalInOut(board.D20), digitalio.DigitalInOut(board.D21)]

keys = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

# --- Configuración de LCD ---
i2c = busio.I2C(board.SCL, board.SDA)
lcd = CharLCD('PCF8574', 0x27)  # Asegurarse que la dirección es 0x27

# --- Configuración Inicial de GPIO ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_SERVO, GPIO.OUT)

# Inicializar PWM para el servo
servo = GPIO.PWM(PIN_SERVO, 50)  # 50Hz
servo.start(0)
time.sleep(2)

# --- Parámetros del Sistema ---
PIN_CORRECTO = "1234"  # PIN configurado para acceso

# --- Definición de Funciones ---

def mover_servo_apertura():
    """Mover el servo para simular apertura de la puerta."""
    servo.ChangeDutyCycle(7)  # Aproximadamente 90 grados
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

def mover_servo_cierre():
    """Mover el servo para cerrar la puerta."""
    servo.ChangeDutyCycle(2.5)  # Aproximadamente 0 grados
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

def prender_led():
    """Encender el LED."""
    GPIO.output(PIN_LED, GPIO.HIGH)

def apagar_led():
    """Apagar el LED."""
    GPIO.output(PIN_LED, GPIO.LOW)

def mostrar_mensaje_lcd(mensaje):
    """Mostrar un mensaje en el LCD."""
    lcd.clear()
    lcd.write_string(mensaje)

def capturar_pin():
    """Captura de PIN a través del teclado."""
    pin_ingresado = ""
    while len(pin_ingresado) < 4:
        teclas = keypad.pressed_keys
        if teclas:
            tecla = teclas[0]
            if tecla not in ["A", "B", "C", "D", "*", "#"]:
                pin_ingresado += tecla
                lcd.write_string("*")
                print("*", end="", flush=True)
            time.sleep(0.3)
    return pin_ingresado

# --- Programa Principal ---

try:
    while True:
        mostrar_mensaje_lcd("Ingrese PIN:\n")
        print("\nEsperando PIN...")
        pin = capturar_pin()
        print("\nPIN ingresado:", pin)

        if pin == PIN_CORRECTO:
            print("Acceso permitido.")
            mostrar_mensaje_lcd("Acceso\nPermitido")
            prender_led()
            mover_servo_apertura()
            time.sleep(5)
            apagar_led()
            mover_servo_cierre()
        else:
            print("PIN incorrecto.")
            mostrar_mensaje_lcd("PIN\nIncorrecto")
            time.sleep(2)
        
        lcd.clear()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")

finally:
    lcd.clear()
    servo.stop()
    GPIO.cleanup()
