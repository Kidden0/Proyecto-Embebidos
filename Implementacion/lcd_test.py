# lcd_test.py
# Prueba básica de la pantalla LCD 16x2 I2C

import time
import board
import busio
from RPLCD.i2c import CharLCD

# --- Configuración de LCD ---
i2c = busio.I2C(board.SCL, board.SDA)
lcd = CharLCD('PCF8574', 0x27)  # Asegúrate que la dirección es 0x27

# --- Funciones ---
def mostrar_mensaje(mensaje):
    """Muestra un mensaje en la pantalla LCD."""
    lcd.clear()
    lcd.write_string(mensaje)

# --- Programa Principal ---
try:
    mostrar_mensaje("¡Hola Mundo!")
    time.sleep(2)
    mostrar_mensaje("Sistema Listo")
    time.sleep(5)
    lcd.clear()

except KeyboardInterrupt:
    print("\nPrueba interrumpida.")

finally:
    lcd.clear()
