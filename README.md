# Proyecto: Sistema Embebido de Control de Puerta mediante PIN

## Descripción General
Este proyecto implementa un sistema de control de acceso mediante un teclado 4x4 para ingresar un PIN, validarlo y accionar un LED y un servo motor simulando la apertura de una puerta. La interfaz visual para el usuario se realiza mediante un display LCD 16x2 conectado por I2C.

## Hardware utilizado
- Raspberry Pi 4B
- Teclado matricial 4x4
- LED con resistencia de 220Ω
- Servo motor SG90
- Display LCD 16x2 con adaptador I2C

## Software
- Python 3
- Librerías:
  - RPi.GPIO
  - RPLCD
  - smbus2
  - adafruit-matrixkeypad
## Estructura de Carpetas
mi_proyecto_embebido/ ├── Documentacion/ │ ├── justificacion.txt │ ├── requisitos_sistema.txt │ ├── requisitos_modulos.txt │ └── diseno_diagramas/ │ ├── diagrama_bloques.png │ └── diagrama_flujo.png ├── Implementacion/ │ ├── proyecto_final.py │ ├── lcd_test.py │ ├── led_test.py │ ├── servo_test.py ├── Simulaciones/ │ └── diagramas de conexiones ├── README.md

## Instrucciones de uso
1. Activar entorno virtual.
2. Ejecutar `proyecto_final.py`.
3. Seguir instrucciones en el LCD para ingresar PIN.

## Autores
- José Carlos Jacal Juarez - Sebastián Enríquez Roque - Brayan Medel Medina - Leonardo Dorantes Ordoñes  
- Universidad Cuauhtémoc Querétaro
